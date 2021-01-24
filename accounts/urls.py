from django.urls import path 

from accounts.views import ForumLoginView, ForumSignUpView

urlpatterns = [ 
    path('login/', ForumLoginView.as_view(), name='login'),
    path('signup/', ForumSignUpView.as_view(), name='signup')
]