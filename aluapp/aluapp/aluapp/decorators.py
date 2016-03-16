from django.http import Http404

from functools import wraps

def must_be_staff(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        request = args[0]
        if request.user.usertype.user_type == 'STF':
            return func(*args, **kwargs)
        else:
            raise Http404
    return func_wrapper

def must_be_student(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        request = args[0]
        if request.user.usertype.user_type == 'STD':
            return func(*args, **kwargs)
        else:
            raise Http404
    return func_wrapper
