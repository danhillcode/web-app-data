from multiprocessing import context
from wsgiref.util import FileWrapper

from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm , CreateUserForm
# from django.shortcuts import render_to_response
import numpy as np

import random
import datetime
import time

'''
This outlines the routes and is basically the controller where data
is processed and can interact with the views
'''
# Import Models
from .models import Demo,Question,Answer



# DJango User Authentication

from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages #error messages for form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#from registration form

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f'congratulations {user}, successfully registered') # flash message for successful user registration
            return redirect('login') #redirecting to login page after form submission
    
    context = {'form':form}
    return render(request,'registration/register.html',context)


#data from login page form
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #authenticating the request data
        user = authenticate(request,username = username, password = password) 

        #if user exists
        if user is not None:
            login(request,user)
            return redirect('home')  

    return render(request,'registration/login.html')

def logoutUser(request):
    logout(request)
    return render(request,'registration/login.html')
    

# def home(request):


# @login_required(login_url="login") #it will redirect unauthenticated url to login
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
    return render('boilerplate/scatter.html', data)




# Finding individual data - work in progress
from django.http import HttpResponseNotFound
def scatter_student(request):

    
   
    
    # surnameFilter =  data['Surname']
    # surnameFilter = surnameFilter.str.replace(" ","")
    # surnameFilter.str.lower()

    
    # name = request.POST['your_name'].replace(" ","")
    # name.lower()
    # surname = request.POST['surname'].replace(" ","")    
    # surname.lower()
    
    
    
    
    data = pd.read_csv("/home/maaz/django-support1/web-app-data/demo/static/Year_7_EOT.csv")
    print(request.POST['your_name'])
    # If name exists in csv
    nameFilter = data['Name'] #copy Name column
    nameFilter = nameFilter.str.replace(" ","") #removing spaces in last
    nameFilter.str.lower() #to lowercase
    
    name = request.POST['your_name'].replace(" ","")
    name.lower()
    
    # #if the name is in request
    if name not in nameFilter.unique():
        return HttpResponseNotFound("Student not found")
        # return JsonResponse({'message':"Does not exist"})

    # #get index of the requested name
    n = nameFilter[nameFilter == name].index
    getIndex = np.array(n)
    getIndex = getIndex[0]
    
    
    
    labels = list(data.columns[8:]) #col titles
    score = data.iloc[getIndex][8:].values #qioz scores
    score = list(score.astype(float)) #converting str to float
    name = [data['Name'][getIndex]] #name of requeseted student

    
    dataset = {
        'labels': labels,
        'data': score,
        'studentName' : name #lablel title
    }

    return render(request, 'boilerplate/scatterStudent.html',dataset)


    
#this function handles question asked to a user
@login_required(login_url="login") #it redirects to login page if not logged in
def question(request):

    #this block return questions
    if request.method == 'GET':
        q = Question.objects.all()
        context = {
            'questions': q
        }
        return render(request, 'boilerplate/examQuestion.html',{'q':q})
    
    #this block saves answers to answer table
    if request.method == 'POST':
        data = {}
        #answer
        data['answer'] = request.POST.get('answer')
        #user data
        data['user'] = request.user 
        #question id
        data['question'] = request.POST.get('question')
        #we need to save instance to answer model not just pk
        question = Question.objects.get(pk=data['question'])
        print(data['answer'],data['user'],)

        answer = Answer(student = data['user'],answer = data['answer'],question = question)
        answer.save()
        return redirect('home')




