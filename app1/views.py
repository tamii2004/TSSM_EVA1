from django.shortcuts import render
from django.http import HttpResponse
 
def vista1(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 1</h2>

"""
    return HttpResponse(html)

def vista2(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 2</h2>

"""
    return HttpResponse(html)