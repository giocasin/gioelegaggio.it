from . import views
from django.urls import path
urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('last_post/', views.LastPost.as_view(), name='last_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail")
]