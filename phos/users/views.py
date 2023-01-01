from django.shortcuts import render, redirect 
from users.forms import CustomUserCreationForm
# Create your views here.
from django.contrib.auth import login
def register(request):
    if request.POST:
        userform = CustomUserCreationForm(request.POST)
        if userform.is_valid():
            new_user = userform.save(commit=False)
            cd = userform.cleaned_data
            new_user.set_password(
                cd['password']
            )
            try:
                new_user.save()
            except Exception as e:
                print(e)
        return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'user_form':user_form})

