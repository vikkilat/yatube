import datetime as dt


def year(request):
    now = dt.datetime.now()
    return {
        'now': now
    }
