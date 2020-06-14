from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from pancar.models import User, Category, Process, Car
from .forms import CarCreateForm
# Create your views here.


class AccountView(View):
    template_name = 'account/account.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass


class AccountProfileView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("profile")


class AccountCarView(View):
    template_name = 'account/car.html'
    def get(self, request):
        return render(request, self.template_name)


class CarCreateView(FormView):
    form_class = CarCreateForm
    template_name = 'account/car_form.html'
    success_url = 'car_details'

    def form_valid(self, form):
        car = Car.objects.create(
            brand = form.cleaned_data['brand'],
            model = form.cleaned_data['model'],
            registration = form.cleaned_data['registration'],
            year = form.cleaned_data['year'],
            review_date = form.cleaned_data['review_date'],
            owner = User.objects.get(pk=self.request.user.id)
        )
        return HttpResponseRedirect(
            reverse(
                self.success_url,
                kwargs={
                    'pk': car.id,
                }
            )
        )


class CarDetailView(View):
    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        context = {
            'car': car
        }
        return render(request, 'account/car_detail.html', context)


class AccountServisesView(View):
    template_name = 'account/servises.html'
    def get(self, request):
        categories = Category.objects.all().order_by('name')
        process = Process.objects.all()
        context = {
            'categories': categories,
            'process': process,
        }
        return render(request, self.template_name, context)


class ProcessesView(View):
    template_name = 'account/processes.html'
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        processes = category.processes.all().order_by('name')
        context = {
            'processes': processes,
        }
        return render(request, self.template_name, context)


class AccountBasketView(View):
    template_name = 'account/basket.html'
    def get(self, request):
        return render(request, self.template_name)