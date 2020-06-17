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
from django.urls import path, include
from django.views.generic import TemplateView

from pancar.views import (
                    ProcessView,
                    LoginSigninView,
                    SignupView,
                    UserLogoutView,
)
from user_account.views import (
                    AccountView,
                    AccountProfileView,
                    AccountCarView,
                    CarCreateView,
                    AccountServisesView,
                    AccountBasketView,
                    ProcessesView,
                    ProfileUpdateView,
                    CarDetailView,
                    # addToCart,

)


urlpatterns = [
    path('google_login', TemplateView.as_view(template_name='login/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', ProcessView.as_view(), name='index'),
    path('forma/', ProcessView.as_view(), name='forma'),
    path('login_signin/', LoginSigninView.as_view(), name='login_signin'),
    path('signin/', SignupView.as_view(), name='signin'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('user_car/', AccountCarView.as_view(), name='car'),
    path('car_create/', CarCreateView.as_view(), name='car_create'),
    path('car_details/<int:pk>/', CarDetailView.as_view(), name='car_details'),
    path('user_servises/', AccountServisesView.as_view(), name='servises'),
    path('processes/<int:category_id>', ProcessesView.as_view(), name='processes'),
    path('basket/', AccountBasketView.as_view(), name='basket'),
    ]