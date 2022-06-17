from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from church import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def signup(request):
    
    if request.method == 'POST':
        username   = request.POST['username']
        fname   = request.POST['fname']
        lname   = request.POST['lname']
        email   = request.POST['email']
        pass1   = request.POST['pass1']
        pass2   = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
        if len(username)>10:
            messages.error(request, "Username must be less than ten characters!")
        if pass1 != pass2:
            messages.error(request, 'Password did not match')

        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        
        
        messages.success(request, "Your account has been successfully created")
        
        subject = "Welcome to Redeemed Church Website!!"
        message ='Hello' + myuser.first_name + '!! \n'+ 'Welcome to Redeemed' + 'Thank you for visiting our website \n We have also sent you  a confirmation email, Please confirm your email adress in order to activate your account.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)
        
        return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname':fname})
            
        else:
            messages.error(request ,'Bad Credentials!')
            return redirect('home')
    
    return render(request, 'signin.html')
def signout(request):
    logout(request)
    messages.success(request, "You successfully logged out")