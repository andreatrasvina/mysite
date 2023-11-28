from django.shortcuts import render

# Create your views here.
def login_form(request):
    return render(request, 'ecommerce/login.html')
