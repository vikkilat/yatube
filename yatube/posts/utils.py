from django.conf import settings
from django.core.paginator import Paginator


def paginator_func(posts, request):
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
