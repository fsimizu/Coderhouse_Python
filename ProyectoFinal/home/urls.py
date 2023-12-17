from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('post/<pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/<pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('post-new/', views.PostCreate.as_view(), name='post-new'),
    path('post/<pk>/edit/', views.PostUpdate.as_view(), name='post-edit'),
    path('filtered-posts/', views.FilteredPostList.as_view(), name='filtered-posts'),

]

from django.conf.urls.static import static
from django.conf import settings

url_patterns_for_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + url_patterns_for_media
