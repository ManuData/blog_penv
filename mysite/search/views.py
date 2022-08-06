from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import json

# Create your views here.


def search_results(request):
    query = request.GET.get("q")
    return render(request,'search/search_results.html',{'data':query})

