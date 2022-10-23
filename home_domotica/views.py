from django.shortcuts import render
import serial,time,json
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,"index.html")


def prender_foco(request):
    dato = request.GET['data']
    sa = serial.Serial("COM3",9600)
    time.sleep(3)
    sa.write(str.encode(dato))
    sa.close()
    return render(request,"index.html")