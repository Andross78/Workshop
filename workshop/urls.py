"""workshop URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from pancar.views import (
                    ProcessView,
                    LoginSigninView,
                    SignupView,
                    UserLogoutView,
                    UserListCreateView,
                    UserDetailView,
                    ConfirmView,
)
from user_account.views import (
                    AccountView,
                    AccountProfileView,
                    UserUpdateView,
                    CarCreateView,
                    CarUpdateView,
                    CarDeleteView,
                    AccountServisesView,
                    AccountBasketView,
                    ProcessesView,
                    OrderMailView,
                    OrderedCartsView,
)


urlpatterns = [
    #-----RESET PASSWORD URLS------
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #------------DJOSER------------
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    #---------API ACCOUNTS---------
    #path("api/accounts/",include("accounts.urls")),
    #------------------------------
    path("all-profiles",UserListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",UserDetailView.as_view(),name="profile"),
    #---------SERIALIZER-----------
    path('google_login', TemplateView.as_view(template_name='login/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', ProcessView.as_view(), name='index'),
    path('forma/', ProcessView.as_view(), name='forma'),
    path('login_signin/', LoginSigninView.as_view(), name='login_signin'),
    path('signin/', SignupView.as_view(), name='signin'),
    path('logout/', UserLogoutView.as_view(), {'next_page': ''}, name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_orders/', OrderedCartsView.as_view(), name='user_orders'),
    path('car_create/', CarCreateView.as_view(), name='car_create'),
    path('car_details/<int:pk>/', CarUpdateView.as_view(), name='car_details'),
    path('car_delete/<int:pk>', CarDeleteView.as_view(), name='car_delete'),
    path('user_servises/', AccountServisesView.as_view(), name='servises'),
    path('processes/<int:category_id>', ProcessesView.as_view(), name='processes'),
    path('basket/', AccountBasketView.as_view(), name='basket'),
    path('order/', OrderMailView.as_view(), name='order'),
    path('activate/<uid>/<token>/', ConfirmView.as_view(), name='activate'),
    ]