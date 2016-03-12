from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Topic

@login_required
def index(request):
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'discuss/index.html', {'topics': topics})

# @login_required
class TopicDetail(DetailView):
    model = Topic
    context_object_name = 'topic'
