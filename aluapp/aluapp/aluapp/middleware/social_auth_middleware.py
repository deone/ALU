from django.http import HttpResponse

from social.apps.django_app.middleware import SocialAuthExceptionMiddleware

class GoogleAuthExceptionMiddleWare(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if exception.__str__() == 'Authentication process canceled':
            return HttpResponse(exception.__str__())
        else:
            raise exception
