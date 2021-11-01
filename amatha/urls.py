"""Amatha URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import handler500, handler404

import paiement.views

urlpatterns = [
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('administration/', include('administration.urls')),
    path('paiement/', include('paiement.urls')),

    # reset password urls + the email message is in accounts/templates/registrations/password_reset_email.html
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/pages/password_reset.html"),
         name="password_reset"),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/pages/password_reset_done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/pages/password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/pages/password_reset_complete.html"),
         name="password_reset_complete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler500 = 'paiement.views.handler500'

handler500 = paiement.views.handler500
handler404 = paiement.views.handler404

