from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from catalog.models import AccountInfo

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_accounts = AccountInfo.objects.all().count()

    context = {
        'num_accounts': num_accounts,
        'user': request.user,
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)

def login(request):
    """Login form."""

    # redirect to index page if user is already logged in
    if request.user.is_authenticated:
        return redirect('catalog:index')
    else:
        # msg = messages.get_messages(request)
        return render(request, 'login.html')

def login_request(request):
    """Attempt login with provided username and password."""
    
    # redirect to index page if user is already logged in
    if request.user.is_authenticated:
        return redirect('catalog:index')

    try:
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            raise Exception
    except:
        return render(request, 'login.html', {
            'messages': ['Enter username and password.']
        })
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('catalog:index')
        else:
            return render(request, 'login.html', {
                'messages': ['The username or password is incorrect.']
            })

def register(request):
    """Register form."""

    context = {
        'user': request.user,
    }

    return render(request, 'register.html')

def register_request(request):
    """Attempt new user registration."""

    # redirect to index page if user is already logged in
    if request.user.is_authenticated:
        return redirect('catalog:index')
    
    try:
        usertype = request.POST['usertype']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        name = request.POST['name']
        location = request.POST['location']
        if not usertype or not username or not email or not password or not password_confirm or not name or not location:
            raise Exception
    except:
        return render(request, 'register.html', {
            'messages': ['Complete all fields to register.']
        })
    else:
        msgs = []

        if usertype != 'DO' and usertype != 'PA':
            msgs.append('Invalid user type.')
        if len(username) > 150:
            msgs.append('Username is too long.')
        elif User.objects.filter(username=username).exists():
            msgs.append('Username is already taken.')
        if password != password_confirm:
            msgs.append('Password does not match.')
        if len(name) > 20:
            msgs.append('Name is too long.')
        if len(location) > 30:
            msgs.append('Location is too long.')
        
        if msgs:
            return render(request, 'register.html', {
                'messages': msgs
            })
        
        django_user = User.objects.create_user(username, password=password, email=email)
        user = AccountInfo(django_user=django_user, name=name, type=type, location=location)
        user.save()

        auth.login(request, django_user)
        return redirect('catalog:index')

@login_required
def user_page(request):
    context = {
        'user': request.user
    }
    return render(request, 'user_page.html', context)

@login_required
def user_edit(request):
    context = {
        'user': request.user
    }
    return render(request, 'user_edit.html', context)

@login_required
def user_edit_request(request):
    """Attempt user data modification."""
    
    try:
        password_old = request.POST['password_old']
        email = request.POST['email']
        password_new = request.POST['password_new']
        password_confirm = request.POST['password_confirm']
        name = request.POST['name']
        location = request.POST['location']
    except:
        return render(request, 'user_edit.html', {
            'message': 'Something went wrong. Try again.'
        })
    else:
        current = request.user
        password_test = authenticate(
            request,
            username=current.username,
            password=password_old
        )
        # correct password?
        if current != password_test:
            return render(request, 'user_edit.html', {
                'messages': ['Your current password does not match.']
            })
        
        # validity test
        msgs = []
        if password_new != password_confirm:
            msgs.append('Your new password does not match.')
        if len(name) > 20:
            msgs.append('Name is too long.')
        if len(location) > 30:
            msgs.append('Location is too long.')
        
        if msgs:
            return render(request, 'user_edit.html', {
                'messages': msgs
            })
        
        # actual update
        if email:
            current.email = email
        if password_new:
            current.set_password(password_new)
        if name:
            current.accountinfo.name = name
        if location:
            current.accountinfo.location = location
        current.save()
        current.accountinfo.save()
        
        # user logs out if password is changed. login again
        auth.login(request, current)
        return redirect('catalog:user_page')

def logout(request):
    """User logout."""

    auth.logout(request)
    # return to index page
    return redirect('catalog:index')




# from django.views import generic

# class SignUp(generic.ListView):
#     model = AccountInfo;