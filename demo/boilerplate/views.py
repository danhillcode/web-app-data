from multiprocessing import context
from wsgiref.util import FileWrapper

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Demo
import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm , CreateUserForm
from django.shortcuts import render_to_response
import numpy as np

import random
import datetime
import time

'''
This outlines the routes and is basically the controller where data
is processed and can interact with the views
'''

# DJango User Authentication

from django.contrib.auth.forms import UserCreationForm 

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            form.save()
    
    context = {'form':form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    return render(request,'registration/login.html')

def logoutUser(request):
    return render(request,'registration/logged_out.html')
    


def index(request):
    latest_demo_list = Demo.objects.all()
    context = {'latest_demo_list': latest_demo_list}
    return render(request, 'boilerplate/index.html', context)


def index2(request):
    form = NameForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # print(form.cleaned_data.values())
        # name = list(form.cleaned_data.values())[0]
        # name1 = list(form.cleaned_data.values())[0]
        # print(name)
        # data = pd.read_csv("/")
        # data = data.Forename
        return render(request, 'boilerplate/index2.html', {"form": form})

# def test(request):
#     form = NameForm(request.POST)
#     # check whether it's valid:
#     if form.is_valid():
#         # print(form.cleaned_data.values())
#         # name = list(form.cleaned_data.values())[0]
#         # name1 = list(form.cleaned_data.values())[0]
#         # print(name)
#         # data = pd.read_csv("/")
#         # data = data.Forename
#         return render(request, 'boilerplate/index2.html', {"form": form})


# This is the method which control my form
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data.values())
            name = list(form.cleaned_data.values())[0]
            request.session['name'] = name
            print(name)
            # process the data in form.cleaned_data as required this is where the data is
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(request, 'boilerplate/name.html', {"name": name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print(form)
    return render(request, 'boilerplate/name.html', {'form': form})


# # https://django-nvd3.readthedocs.io/en/latest/classes-doc/multi-bar-chart.html
# # https://docs.google.com/document/d/1j-QHjCJy4AQWOUJG5JtmCXXHQ54XE1WsUzj4ChQBHtM/edit
# def demo_scatter(request):
#     """
#     multibarchart page
#     Emmas data below
#
#     data = pd.read_csv("/Users/danielhill/PycharmProjects/web-app-data/demo/static/EmmaData_FRGrades.csv")
#     """
#     data = pd.read_csv("/Users/danielhill/PycharmProjects/web-app-data/demo/static/Year_7_EOT.csv")
#
#     name1 = np.array(data.Name[0:1])
#     print(name1)
#
#     # print(data.columns)
#     # score = np.array(data.Gender[0:10]).tolist()
#
#     # inserting data for males and females
#     # nb_element = 20
#     # xdata = range(nb_element)
#     # ydata = [random.randint(1, 10) for i in range(nb_element)]
#     # ydata2 = map(lambda x: x * 2, ydata)
#     # ydata3 = map(lambda x: x * 3, ydata)
#     # ydata4 = map(lambda x: x * 4, ydata)
#     #
#     # extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
#     #
#     # chartdata = {
#     #     'x': xdata,
#     #     'name1': 'Male', 'y1': ydata, 'extra1': extra_serie,
#     #     'name2': 'Female', 'y2': ydata2, 'extra2': extra_serie,
#     # }
#     #
#     # charttype = "multiBarChart"
#     # data = {
#     #     'charttype': charttype,
#     #     'chartdata': chartdata
#     # }
#
#     return render_to_response('boilerplate/scatter.html', data)



# original graph for the student data
#Computing charts - show data for a class
def demo_scatter(request):
    data = pd.read_csv("/Users/danielhill/PycharmProjects/web-app-data/demo/static/Year_7_EOT.csv")
    names = np.array(data.Name[0:25])
    print(data.columns)
    score = np.array(data.Grade[0:25]).tolist()


    chartdata = {'x': names, 'y': score}
    charttype = "discreteBarChart"
    chartcontainer = 'multiBarChart'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('boilerplate/scatter.html', data)



# Finding individual data - work in progress
def scatter_student(request):

    # print("session value here:???")
    # print(Demo.objects.all)

    data = pd.read_csv("/Users/danielhill/PycharmProjects/web-app-data/demo/static/Year_7_EOT.csv")
    #name is data but didnt change name1 is actual name
    name = np.array(data[0:1])
    df = pd.DataFrame(data)

    columnTitles = df.columns[8:25]
    print(df.columns[8:18])
    # dataSet = np.array(data[0:1])





    name1 = name[0]
    data = name[0][8:28]

    # Need to find a way to go across and access all of the scores for one student
    score = np.array(name[0][8:25]).tolist()


    chartdata = {'x':columnTitles , 'y': score}
    charttype = "multiBarHorizontalChart"
    chartcontainer = 'piechart_container'
    # charttype = "discreteBarChart"
    # chartcontainer = 'multiBarChart'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        # 'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('boilerplate/scatterStudent.html',data )






def question(request):
    # latest_demo_list = Demo.objects.all()
    # context = {'latest_demo_list': latest_demo_list}
    return render(request, 'boilerplate/examQuestion.html')


