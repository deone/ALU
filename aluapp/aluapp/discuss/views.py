from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Topic
from .forms import NewTopicForm, CommentForm

@login_required
def index(request):
    topics = Topic.objects.all()
    return render(request, 'discuss/index.html', {'topics': topics})

@login_required
def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('discuss:topics')
    else:
        form = NewTopicForm()

    return render(request, 'discuss/new_topic.html', {'form': form})

@login_required
def topic_detail(request, pk, slug):
    topic = get_object_or_404(Topic, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.topic = topic
            comment.save()
            return redirect('discuss:topic', pk=pk, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'discuss/topic_detail.html', {'topic': topic, 'form': form})
