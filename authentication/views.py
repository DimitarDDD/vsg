from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.contrib.auth.models import User  
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):  
    if request.method == 'POST':
        username = request.POST['username']  
        firstname = request.POST['firstname']   
        lastname = request.POST['lastname']  
        email = request.POST['email']    
        password = request.POST['password']      
        
        thisuser = User.objects.create_user(username, email, password)  
        thisuser.first_name = firstname 
        thisuser.last_name = lastname
        
        thisuser.save() 
        
        messages.success(request, "Your account has been succesfuly created") 
        
        return redirect("authentication:signin")
        
        
    return render(request, "authentication/register.html") 
    

def signin(request): 
    
    if request.method == "POST":
        username = request.POST['username']  
        password = request.POST['password']    
        
        user = authenticate(username=username, password=password) 
        
        if user is not None:
            login(request, user)  
            firstname = user.first_name 
            print(firstname)
            return render(request, "jikan/home.html", {'firstname': firstname}) 
        else:
            messages.error(request, "Typo mistake had been made or user doesnt exist" ) 
            return redirect("authentication:signin")
    return render(request, "authentication/signin.html") 

def signout(request):
    logout(request)
    messages.success(request, "You log out succesfully") 
    return render(request, "authentication/signin.html") 