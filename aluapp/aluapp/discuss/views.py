from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Topic
from .forms import NewTopicForm

@login_required
def index(request):
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'discuss/index.html', {'topics': topics})

@login_required
def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST, user=request.user)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('discuss:new_topic')
    else:
        form = NewTopicForm()

    return render(request, 'discuss/new_topic.html', {'form': form})

# @login_required
class TopicDetail(DetailView):
    model = Topic
    context_object_name = 'topic'
