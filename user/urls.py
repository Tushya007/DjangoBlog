from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import user_registration_form,logoutView

urlpatterns = [
    path('add/user/', user_registration_form, name="create_user"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("logout/",logoutView,name='logout'),
]