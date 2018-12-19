from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm, RegisterForm2 , RegisterForm3, RegisterForm4

def index(request):
    context={
        "title" : "Contact us for more..",
        
        }
    if request.user.is_authenticated:
        username = request.user.username
        context["user"] = username
    return render(request, 'personal/home.html', context)

def about(request):
    context={
        "title" : "Contact us for more..",
        "content" : "we are sole distributor"
        }
    return render(request, 'personal/about.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "Contact",
        "content" : "Welcome to contact page.",
        "form" : contact_form
        }
    if request.user.is_authenticated:
        context["pcontent"] = "you are prime member"
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST.get('fullname'))
        #print(request.POST.get('email'))
        #print(request.POST.get('content'))
    return render(request, 'personal/contact.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
        }
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        
        user = authenticate(request, username=username, password=password)
        #print(request.user.is_authenticated)
        if user is not None:
            print(user)
            login(request, user)
            #context['form']=LoginForm()
            return redirect("/")  
        else:
            print("error")
            
    return render(request, "personal/auth/login.html", context)

def logout_page(request):
    logout(request)
    return redirect("/")
    
 
            
            
    

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    form2 = RegisterForm2(request.POST or None)
    form3 = RegisterForm2(request.POST or None)
    form4 = RegisterForm2(request.POST or None)
    context = {
        "form" : form,
        "form2" : form2,
        "form3" : form3,
        "form4" : form4
        }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        email=form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect("/login/")
    return render(request, "personal/auth/register.html", context)

