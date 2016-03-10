from django.http import HttpResponse

from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions

class GoogleAuthExceptionMiddleWare(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthCanceled'):
            return HttpResponse("I'm the pony %s" % exception)
        else:
            raise exception
