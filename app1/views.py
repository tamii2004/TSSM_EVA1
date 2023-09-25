from django.shortcuts import render
from django.http import HttpResponse
 
def vista1(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 1</h2>
<a href="/vista2/" > ir a la vista 2</a>
<a href="/vista3/" > ir a la vista 3</a>
<a href="/vista4/" > ir a la vista 4</a>

"""
    return HttpResponse(html)

def vista2(request):
    html ="""
<h1>bienvenido</h1>
<h2>esta en la vista 2</h2>
<a href="/" > ir a la vista 1</a>
<a href="/vista3/" > ir a la vista 3</a>
<a href="/vista4/" > ir a la vista 4</a>

"""
    return HttpResponse(html)