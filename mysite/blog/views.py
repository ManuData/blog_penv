from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd

import json

# Datos a modo de test
test_datos = [0,1,2,30,34,21]
serie = pd.Series(test_datos,name="test")
obj = {'test1':1,'test2':2}

# Create your views here.


def index(request):
    return render(request,'blog/index.html',{'numbers':serie,"obj_as_json":json.dumps(obj)})


def base(request):
    return render(request,'blog/base.html')

def search_results(request):
    query = request.GET.get("q")
    return render(request,'blog/search_results.html',{'data':query})

    





