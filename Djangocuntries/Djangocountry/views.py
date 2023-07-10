from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from Djangocountry import country

def home(request):
    text = """<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Правка номер один Жилкин А.А </i>
            <a href="http://127.0.0.1:8000/countries-list/ ">Список Стран</a>"""
    return HttpResponse(text)
# Create your views here.

def countries_list(request):
    e = []
    for i in country.a:
        a = i["country"].replace(" ","_")
        e.append(f"<a href = http://127.0.0.1:8000/countries-list/{a}>")
        e.append("<h1>")
        e.append(i["country"])
        e.append('</h1>')
        e.append("</a>")
    return HttpResponse(e)

def get_country(request,value):
    text = []
    for i in country.a:
        if i["country"].replace(" ","_") == value:
            text.append('<h1>')
            text.append("В Стране - ")
            text.append(i["country"])
            text.append(" Говорят на Вот этих языках - ")
            text.append(i["languages"])
            text.append("</h1>")
            text.append("</br>")
            text.append("<h1>")
            text.append("<a href = http://127.0.0.1:8000/countries-list/>Вернутся к списку стран</a>")
    return HttpResponse(text)