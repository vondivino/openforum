from django.urls import path 

from forums.views import (
    ForumListView,
    ForumDetailView
)

urlpatterns = [ 
    path('', ForumListView.as_view(), name='forum-home'),
    path('f/<slug:slug>/', ForumDetailView.as_view(), name='forum-detail')
]