from django.shortcuts import render,HttpResponseRedirect
from .models import CustomUser
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def signup(request):
    if request.method=='POST':
        forms=SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            return HttpResponseRedirect('/login/')
        
    forms = SignupForm()
    return render(request, 'app/signup.html', {'forms': forms})
        
def login(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            print(username,password)
            user = authenticate( request=request,username=username, password=password)
            print(user)
            if user is not None:
                
                return HttpResponseRedirect('/dashboard/')
    
    forms = LoginForm()
    return render(request, 'app/login.html', {'forms': forms})

def dashboard(request):
    if request.user.is_authenticated:
        u=CustomUser.objects.get(username=request.user.username)
       
        return render(request, 'app/dashboard.html', {'user': u})
    else:
        return HttpResponseRedirect('/login/')
