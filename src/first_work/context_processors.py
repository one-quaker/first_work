from django.conf import settings


def settings_debug(request):
    return {'DEBUG': settings.DEBUG}


def settings_project(request):
    return {'TITLE': 'First work'}
