from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from help_provider.forms import ExtendedSignupForm
from django.contrib.auth.decorators import login_required 

# REMOVE @login_required from here!
def signup(request):
    if request.method == 'POST':
        # Use ExtendedSignupForm here
        form = ExtendedSignupForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        # And use ExtendedSignupForm here
        form = ExtendedSignupForm() 
        
    return render(request, 'registration/signup.html', {'form': form})

# USE THE DECORATOR HERE INSTEAD (Example):
@login_required
def profile_page(request):
    return render(request, 'profile.html')