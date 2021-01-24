from django.urls import path 

from forums.views import (
    CommentCreateView, DiscussionDetailView, 
    ForumCreateView, 
    ForumListView,
    ForumDetailView,
    DiscussionCreateView
)

urlpatterns = [ 
    path('f/all/', ForumListView.as_view(), name='forum-home'),
    path('f/new/', ForumCreateView.as_view(), name='forum-new'),
    path('f/<slug:slug>/', ForumDetailView.as_view(), name='forum-detail'),

    path('d/<slug:slug>/new/', DiscussionCreateView.as_view(), name='discussion-new'),
    path('d/<slug:slug>/', DiscussionDetailView.as_view(), name='discussion-detail'),

    path('d/<slug:slug>/comment/add/', CommentCreateView.as_view(), name='comment-add')
]