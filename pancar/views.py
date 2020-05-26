from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from pancar.models import Klient, Car, Process


class ProcessView(View):

    def get(self, request):
        processes = Process.objects.all()
        context = {
            'processes': processes,
        }
        return render(request, 'base.html', context)