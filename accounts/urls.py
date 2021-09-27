from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


app_name = 'account'

urlpatterns = [
    path('informationsClient/', views.informations, name='informations'),
    path('updateInfos/', views.UpdateInfos, name='UpdateInfos'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/pages/login.html', redirect_authenticated_user=True,
                                                authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/pages/logout.html', next_page='account:login'),
         name='logout'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/pages/passwordChangeDone.html'), name='password_change_done'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/pages/passwordChange.html', success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('favourite_add/<int:id>', views.favourite_add, name='favourite_add'),
    path('favourite_list/', views.favourite_list, name='favourite_list'),


    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='pages/password_change_done.html'),
    #      name='password_change_done'),
    #
    # path('password_reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_done.html'),
    #      name='password_reset_done'),
    #
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html'),
    #      name='password_reset_complete'),
]