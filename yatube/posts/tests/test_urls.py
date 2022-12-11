from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from ..models import Group, Post

User = get_user_model()


class URLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='author')
        cls.group = Group.objects.create(
            title='Тестовый заголовок',
            slug='test-slug',
            description='Тестовый текст',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            group=cls.group,
            text='Тестовый заголовок',
        )

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_uses_correct_template(self):
        """Проверка status_code для авторизованного
        и неавторизованного пользователя."""
        templates_url_names = {
            self.authorized_client: {
                '/create/': 'posts/post_create.html',
                f'/post/{self.post.id}/edit': 'posts/post_create.html',
            },
            self.client: {
                '/': 'posts/index.html',
                f'/group/{self.group.slug}/': 'posts/group_list.html',
                f'/profile/{self.user}/': 'posts/profile.html',
                f'/post/{self.post.id}/': 'posts/post_detail.html',
            }
        }
        for client, dict in templates_url_names.items():
            for address, template in dict.items():
                with self.subTest(address=address):
                    response = client.get(address)
                    self.assertTemplateUsed(response, template)
                    self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_id_edit_url_redirect_anonymous(self):
        """Страница posts/post_id/edit/
        перенаправляет анонимного пользователя."""
        response = self.client.get(
            f'/posts/{self.post.id}/edit/', follow=True
        )
        self.assertRedirects(
            response, (f'/auth/login/?next=/posts/{self.post.id}/edit/')
        )

    def test_post_create_url_redirect_anonymous(self):
        """Страница /create/ перенаправляет анонимного пользователя."""
        response = self.client.get('/create/', follow=True)
        self.assertRedirects(response, ('/auth/login/?next=/create/'))

    def test_url_unexisting(self):
        """Запрос к странице unixisting_page вернет ошибку 404"""
        response = self.client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/': 'posts/index.html',
            f'/group/{self.group.slug}/': 'posts/group_list.html',
            f'/profile/{self.user.username}/': 'posts/profile.html',
            f'/posts/{self.post.id}/': 'posts/post_detail.html',
            '/create/': 'posts/post_create.html',
            f'/posts/{self.post.id}/edit/': 'posts/post_create.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)
