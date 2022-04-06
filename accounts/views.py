from multiprocessing import context
from django.shortcuts import render
from .forms import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        print('POST')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('valid')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            print(phone_number)

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name,
                email=email, username=username,
                password=password)
            print(user)

            user.phone_number = phone_number
            user.save()

    else:
        print('get')
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')