from django.shortcuts import render, redirect
from validapp.models import CreateAccount
# Create your views here.


def createuser(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        en = CreateAccount(username=name, email=email,
                           password=password, repassword=repassword,)
        en.save()
        redirect('/')

    return render(request, 'validapp/index.html')
