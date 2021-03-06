from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework import permissions
from .serializers import UserSerializer

from .forms import MessageForm, UserCreateForm, UserLoginForm
from .models import Car, Process, Category, User


class ProcessView(View):
    form_class = MessageForm
    def get(self, request):
        form = self.form_class()
        category_basic = Category.objects.get(name='Główne roboty')
        basic_proc = category_basic.processes.all().order_by('name')
        front_suspension = Category.objects.get(name='Zawieszenie przednie')
        front_susp_proc = front_suspension.processes.all().order_by('name')[:10]
        rear_suspension = Category.objects.get(name='Zawieszenie tylne')
        rear_susp_proc = rear_suspension.processes.all().order_by('name')
        braking_system = Category.objects.get(name='Układ hamulcowy')
        brak_sys_proc = braking_system.processes.all().order_by('name')[:8]
        fuel_system = Category.objects.get(name='Układ paliwowy')
        fuel_sys_proc = fuel_system.processes.all().order_by('name')
        silencer = Category.objects.get(name='Układ wydechowy')
        silencer_proc = silencer.processes.all().order_by('name')
        sterring_system = Category.objects.get(name='Układ kierownicy')
        sterring_sys_proc = sterring_system.processes.all().order_by('name')
        engine = Category.objects.get(name='Naprawa silnika')
        engine_proc = engine.processes.all().order_by('name')[:10]
        transmission = Category.objects.get(name='Skrzynia biegów')
        trans_proc = transmission.processes.all().order_by('name')[:10]
        context = {
            'form': form,
            'category_basic': category_basic,
            'basic_proc': basic_proc,
            'front_susp_proc': front_susp_proc,
            'front_suspension': front_suspension,
            'rear_susp_proc': rear_susp_proc,
            'rear_suspension': rear_suspension,
            'brak_sys_proc': brak_sys_proc,
            'braking_system': braking_system,
            'fuel_sys_proc': fuel_sys_proc,
            'fuel_system': fuel_system,
            'silencer_proc': silencer_proc,
            'silencer': silencer,
            'sterring_sys_proc': sterring_sys_proc,
            'sterring_system': sterring_system,
            'engine_proc': engine_proc,
            'engine': engine,
            'trans_proc': trans_proc,
            'transmission': transmission,
        }
        return render(request, 'base.html', context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = 'Prosba o kontakt'
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = f'Wiadomosc od {name}\n {phone}\n'

            message += form.cleaned_data['info']
            send_mail(title,
                      message,
                      'wdsasha22@gmail.com',
                      ['wdsasha22@gmail.com'])

            return HttpResponseRedirect(reverse_lazy('index'))


class LoginSigninView(LoginView):
    template_name = 'pancar/login_v_3.html'


class UserLogoutView(LogoutView):
    ...


class SignupView(FormView):
    form_class = UserCreateForm
    success_url = '/login_signin'
    template_name = 'auth/registration.html'
    def form_valid(self, form):
        new_user = form.instance
        new_user.username = form.cleaned_data['email']
        password = form.cleaned_data["password"]
        new_user.set_password(password)
        new_user.is_active = False
        new_user.save()
        new_user.send_confirm_email(self.request)
        return super().form_valid(form)


class ConfirmView(View):
    def get(self, request, uid, token):
        from django.contrib.auth.tokens import default_token_generator
        from djoser.utils import decode_uid
        uid = int(decode_uid(uid))
        user = User.objects.get(id=uid)
        if default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            #login(self.request, user)
            success_url = reverse_lazy('profile')
        else:
            success_url = revese_lazy('login_signin')
        return HttpResponseRedirect(success_url)

class UserListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]