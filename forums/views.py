from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

from forums.models import (
    Forum,
    Discussion,
    Comment
)

from forums.sanitizers import slug_clean

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

class ForumCreateView(CreateView):
    model = Forum 
    template_name = 'forums/new.html'
    fields = ('name', )

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.name = form.instance.name.title()
        form.instance.slug = slug_clean(
            self.model,
            form.instance.name.lower()
        )
        return super().form_valid(form)

class DiscussionCreateView(CreateView):
    model = Discussion 
    template_name = 'discussion/new.html'
    fields = ('title', 'body', )

    def form_valid(self, form):
        form.instance.author = self.request.user 
        form.instance.slug = slug_clean(
            self.model,
            form.instance.title.lower()
        )
        form.instance.forum = Forum.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/add.html'
    fields = ('body', )

    def form_valid(self, form):
        form.instance.author = self.request.user 
        form.instance.discussion = Discussion.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)