from django.shortcuts import render
from .domain import TableObject
from django.http import HttpResponse

def getTables(request):
    return HttpResponse(TableObject.dp.getTableNames())

def test(request):
    return HttpResponse("Hello There")
