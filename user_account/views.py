from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pancar.models import User, Category, Process, Car, Cart, OrderedCart
from .forms import UserUpdateForm, CarCreateForm, OrderMailForm


class AccountView(View):
    template_name = 'account/account.html'
    def get(self, request):
        return render(request, self.template_name)


class AccountProfileView(View):
    form_class_car = CarCreateForm
    form_class_car_update = CarCreateForm
    form_class_user = UserUpdateForm
    template_name = 'account/profile.html'

    def get(self, request):
        user = self.request.user
        initial_user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone': user.phone,
            'email': user.email,
        }
        form_car_update = self.form_class_car_update
        form_car = self.form_class_car
        form_user = self.form_class_user(initial=initial_user_data)
        context = {
            'form_car': form_car,
            'form_user': form_user,
            'form_car_update': [form_car_update(instance=car) for car in user.cars.all()],
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form_user = self.form_class_user(request.POST)
    #     form_car = self.form_class_car(request.POST)
    #     # form_car_update = self.form_class_car(request.POST)
    #     if form_user.is_valid():
    #         user = self.request.user
    #         user.first_name = request.POST['first_name']
    #         user.last_name = request.POST['last_name']
    #         user.email = request.POST['email']
    #         user.phone = request.POST['phone']
    #         if user.first_name or user.last_name or user.email or user.phone:
    #             user.save()
    #             return render(request, self.template_name)
    #     if form_car.is_valid():
    #         Car.objects.create(
    #             brand=form_car.cleaned_data['brand'],
    #             model=form_car.cleaned_data['model'],
    #             registration=form_car.cleaned_data['registration'],
    #             year=form_car.cleaned_data['year'],
    #             insurance=form_car.cleaned_data['insurance'],
    #             review_date=form_car.cleaned_data['review_date'],
    #             owner=User.objects.get(pk=self.request.user.id)
    #         )
    #         return render(request, self.template_name)
        # if form_car_update.is_valid():
        #     pass
            # car = Car.objects.get(owner=self.request.user)
            # car.brand = form_car.cleaned_data['brand']
            # car.model = form_car.cleaned_data['model']
            # car.registration = form_car.cleaned_data['registration']
            # car.year = form_car.cleaned_data['year']
            # car.insurance = form_car.cleaned_data['insurance']
            # car.review_date = form_car.cleaned_data['review_date']
            # return render(request, self.success_url)

class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone', 'email']
    template_name_suffix = '_update_form'


class CarCreateView(FormView):
    form_class = CarCreateForm
    template_name = 'account/car_form.html'
    success_url = 'profile'


    def form_valid(self, form):
        car = Car.objects.create(
            brand=form.cleaned_data['brand'],
            model=form.cleaned_data['model'],
            registration=form.cleaned_data['registration'],
            year=form.cleaned_data['year'],
            insurance=form.cleaned_data['insurance'],
            review_date=form.cleaned_data['review_date'],
            owner=User.objects.get(pk=self.request.user.id)
        )
        return HttpResponseRedirect(
            reverse(
                self.success_url
            )
        )


class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'registration', 'year', 'review_date', 'insurance']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("profile")

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("profile")


class AccountServisesView(View):
    template_name = 'account/servises.html'

    def get(self, request):
        categories = Category.objects.all().order_by('name')
        context = {
            'categories': categories,
        }
        return render(request, self.template_name, context)


class ProcessesView(View):
    template_name = 'account/processes.html'
    success_url = 'servises'

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        processes = category.processes.all().order_by('name')
        context = {
            'processes': processes,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart = user.get_cart()
        process_id = int(request.POST['pid'])
        process = Process.objects.get(id=process_id)
        cart.process.add(process)
        return HttpResponseRedirect(reverse(self.success_url))


class AccountBasketView(View):
    template_name = 'account/basket.html'
    success_url = ('basket')

    def get(self, request):
        user = User.objects.get(pk=self.request.user.id)
        cart = user.get_cart()
        context = {
            'cart': cart,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        cart.process.remove(int(request.POST['pid']))
        processes = Process.objects.filter(carts=cart)

        return HttpResponseRedirect(reverse(self.success_url))


class OrderMailView(FormView):
    form_class = OrderMailForm
    template_name = 'account/mail_send.html'
    def form_valid(self, form):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        ordered_cart = OrderedCart.objects.create(user=user)
        price = cart.get_total_price()
        processes = Process.objects.filter(carts=cart)
        for proc in processes:
            ordered_cart.process.add(proc)
        title = 'Zamowienie na naprawe samochodu'
        info = form.cleaned_data['info']
        date = form.cleaned_data['order_date']
        message = f'Zamowienie od: {user.first_name} {user.last_name}\nNumer teefonu: {user.phone}'
        message += '\nPotrzebuje zamowic takie uslugi: '
        for i in processes:
            message += i.name +';\n '
        message += f'Cena za wszystko {price} zl'
        send_mail(title,
                  f'{message} \nDodatkowe uwagi: {info} \nData zamowienia:{date}',
                  'wdsasha22@gmail.com',
                  ['wdsasha22@gmail.com'])
        cart.delete()
        return HttpResponseRedirect(reverse_lazy('profile'))


class OrderedCartsView(View):
    template_name = 'account/ordered_carts.html'

    def get(self, request):
        user = User.objects.get(pk=self.request.user.id)

        ordered_carts = OrderedCart.objects.filter(user=user)
        context = {
                'ordered_carts': ordered_carts,
        }
        return render(request, self.template_name, context)
