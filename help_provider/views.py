from django.shortcuts import get_object_or_404, render, redirect
from .models import HelpPost
from help_provider.forms import ExtendedSignupForm
from django.contrib.auth import login
from .models import HelpPost, Category
from django.contrib.auth.decorators import login_required
def home(request):
    posts = HelpPost.objects.select_related('user', 'user__profile').exclude(status='closed').order_by('-created_at')
    
    return render(request, 'home.html', {'posts': posts})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(HelpPost, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
    return redirect('home')

@login_required
def create_post(request, help_type):
    if request.method == 'POST':
        # Get the ID from the dropdown select
        category_id = request.POST.get('category')
        
        # Find that specific category object
        category_obj = get_object_or_404(Category, id=category_id)
        
        HelpPost.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=category_obj,
            priority=1,
            city=request.POST.get('city', 'Kathmandu'),
            contact=request.POST.get('contact'),
            help_type=help_type,
            user=request.user
        )
        return redirect('home')
    
    # --- GET part ---
    # Fetch all categories from the DB to show in the dropdown
    categories = Category.objects.all() 
    return render(request, 'create_post.html', {
        'help_type': help_type,
        'categories': categories # Send them to the template
    })

def signup(request):
    if request.method == 'POST':
        form = ExtendedSignupForm(request.POST) # Use the new form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ExtendedSignupForm()
    return render(request, 'registration/signup.html', {'form': form})