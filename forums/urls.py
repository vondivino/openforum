from django.urls import path 

from forums.views import (
    DiscussionDetailView, ForumListView,
    ForumDetailView
)

urlpatterns = [ 
    path('f/all/', ForumListView.as_view(), name='forum-home'),
    path('f/<slug:slug>/', ForumDetailView.as_view(), name='forum-detail'),

    path('d/<slug:slug>/', DiscussionDetailView.as_view(), name='discussion-detail')
]