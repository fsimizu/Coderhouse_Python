from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "users"

urlpatterns = [
    path('', views.UserList.as_view(), name='index'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('upload-avatar/', views.upload_avatar, name='user-avatar'), # type: ignore
    path('<pk>/', views.UserDetail.as_view(), name='user-details'),
    path('<pk>/edit/', views.UserUpdate.as_view(), name='user-edit'),
    path('<pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

]

from django.conf.urls.static import static
from django.conf import settings

url_patterns_for_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + url_patterns_for_media
