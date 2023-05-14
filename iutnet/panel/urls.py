from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='panel/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='panel/logout.html'), name='logout'),
    path('profile/', profile, name='users-profile'),

]