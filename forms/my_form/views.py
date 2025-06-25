from django.shortcuts import render
from .form import RegistrationForm, LoginForm
# Create your views here.
def register_form(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'success.html',{'data' : data})
    return render(request, 'register_form.html', {'form': form})

def login_form(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'login_form.html', {'form' : form, 'data': data })
    return render(request, 'login_form.html', {'form':form})