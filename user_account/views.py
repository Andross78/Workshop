from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from pancar.models import User, Category, Process
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
    fields = ['first_name', 'last_name', 'phone', 'car', ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("profile")


class AccountHistoryView(View):
    template_name = 'account/history.html'
    def get(self, request):
        return render(request, self.template_name)


class AccountServisesView(View):
    template_name = 'account/servises.html'
    def get(self, request):
        categories = Category.objects.all()
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