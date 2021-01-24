from django.views.generic import (
    ListView,
    DetailView
)

from forums.models import (
    Forum,
    Discussion,
    Comment
)

class ForumListView(ListView):
    model = Forum 
    template_name = 'forums/home.html'
    context_object_name = 'forums'

class ForumDetailView(DetailView):
    model = Forum 
    template_name = 'forums/detail.html'
    context_object_name = 'forum'

class DiscussionDetailView(DetailView):
    model = Discussion 
    template_name = 'discussion/detail.html'
    context_object_name = 'discussion'