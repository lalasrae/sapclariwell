from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# Create your views here.
def index (request):
    return render(request, "app1/index.html")

def about (request):
    return render(request, "app1/about.html")

def courses (request):
    return render(request, "app1/courses.html")

def blog (request):
    return render(request, "app1/blog.html")

def contact (request):
    return render(request, "app1/contact.html")



def sendmail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        location = request.POST.get('location')
        message = request.POST.get('message')

        data ={
            "name": name,
            "email": email,
            "mobile_number": mobile_number,
            "location": location,
            "message":message
        }
        message = '''
        New message: {}

        mobile_number: {}

        email: {}

        location: {}
        '''.format(data['message'], data["mobile_number"], data["email"], data["location"])
        send_mail(data["name"], message, '', ['clariwelltech@gmail.com'])
      
    return render(request, "app1/contact.html")
   

  