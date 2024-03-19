from django.shortcuts import render

def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'users/login.html', context)

def register(request):
    context = {
        'title': 'Register'
    }
    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)\
        
def logout(request):
    context = {
        'title': 'Logout'
    }
    return render(request, 'users/logout.html', context)