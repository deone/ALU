from .models import SimpleComment
from .forms import SimpleCommentForm

def get_model():
    return SimpleComment

def get_form():
    return SimpleCommentForm
