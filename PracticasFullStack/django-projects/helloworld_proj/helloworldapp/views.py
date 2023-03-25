from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User

# Create your views here.
def firstPage(request,year,example):
    print(year)
    print(example)
    now = datetime.datetime.now()
    html = '<html><body> Its now %s. </body></html>' %now
    return HttpResponse(html)

def home(request):
    context = {
        'name': 'Juan',
        'phone_number': 66778899
    }
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html',{})

blogpost = [

{
    'title':'First post',
    'content':'content of first post',
    'author':'juan',
    'post_number': 1
},
{
    'title':'second post',
    'content':'content of second post',
    'author':'miguel',
    'post_number': 2
    },
{
    'title':'third post',
    'content':'content of third post',
    'author':'beto',
    'post_number': 3
    },
{
    'title':'fourth post',
    'content':'content of fourth post',
    'author':'pepe',
    'post_number': 4
    }
]

def blog (request):
    context = {
        'posts':blogpost
    }
    return render(request, 'blog.html', context)

def createUser(request):
    user = User.objects.create_user('michael', 'michael@mail.com', 'michaelpassword')
    context = {
        'result' : 'username %s email %s' %(user.username, user.email)
    }
    return render(request, 'result.html',context)

def changePassword(request):
    user =  User.objects.get(username='michael')
    user.set_password('michaelpassword')
    user.save()

    context = {
        'result': 'Username %s password %s' %(user.get_full_name(), user.password)
    }
    return render(request, 'result.html', context)

