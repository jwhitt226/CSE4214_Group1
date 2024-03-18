
from django.shortcuts import render
from .models import User
from .forms import UserForm 

def create_user(request):
    if request.method == 'POST':
        # Process form submission
        form = UserForm(request.POST)
        if form.is_valid():
            # Create a new user using form data
            User.objects.create_user(**form.cleaned_data)
            # Redirect to a success page or display a success message
    else:
        # Display the form for creating a new user
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
