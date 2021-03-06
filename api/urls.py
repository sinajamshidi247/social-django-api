from django.urls import path 
from . import views 

app_name =  'api'

urlpatterns = [
    path('posts/',views.Posts.as_view(),name = 'api_posts'),
    path('create_posts/',views.CreatePosts.as_view(),name = 'create_post'),
    path('add_reply/<int:post_id>/<int:comment_id>/',views.CommentCreate.as_view(),name='add_reply'),
    path('delete/<int:pk>/',views.DeletePost.as_view(),name = "delete_post"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    
]