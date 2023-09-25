from django.shortcuts import render
from django.http import HttpResponse
 
def vista3(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 3</h2>

"""
    return HttpResponse(html)

def vista4(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 4</h2>

"""
    return HttpResponse(html)
