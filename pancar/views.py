from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from pancar.models import Klient, Car, Process
# Create your views here.

@csrf_exempt
def client_creator(request):
    if request.method == "GET":
        html = """
            <form action="#" method="POST">
                <input required type="text" name="name" placeholder="Name"/>
                <input required type="text" name="surname" placeholder="Surname"/><br/>
                <input required type="email" name="email" placeholder="Email"/>
                <input required type="text" name="phone" placeholder="Phone number"/><br/>
                <button type="submit">Create</button>
            </form>
            """
        return HttpResponse(html)

    else:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        if name and surname and email and phone:
            client = Klient.objects.create(name=name, surname=surname, email=email, phone=phone)
            return HttpResponse(f'Client {name} {surname} has been successfully added.')

@csrf_exempt
def car_creator(request):
    if request.method == 'GET':
        html = """
            <form action="#" method="POST">
                <input required type="text" name="brand" placeholder="Car brand"/>
                <input required type="text" name="model" placeholder="Car model"/><br/>
                <input required type="text" name="registration" placeholder="Registr. number"/>
                <input required type="text" name="year" placeholder="Year"/><br/>
                <button type="submit">Create</button>
            </form>
            """
        return HttpResponse(html)
    else:
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        registr = request.POST.get("registration")
        year = request.POST.get("year")
        if brand and model and registr and year:
            car = Car.objects.create(brand=brand, model=model, registration=registr, year=year)
            return HttpResponse(f'Car {brand} {model} has been successfully created.')

@csrf_exempt
def process_creator(request):
    if request.method == "GET":
        html = """
            <form action="#" method="POST">
                <input required type="text" name="name" placeholder="Process"/>
                <input required input type="number" min="0.00" step="0.01" name="price" placeholder="Price"/><br/>
                <button type="submit">Create</button>
            </form>
            """
        return HttpResponse(html)
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        if name and price:
            process = Process.objects.create(name=name, price=price)
            return HttpResponse(f'Process {name}  has been successfully created.')