from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


########################################################################################################################
# ** register function ** for signing up new users
########################################################################################################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account successfully created with username {username}')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)


########################################################################################################################
# ** profile function ** for updating user details and profile details
########################################################################################################################


@login_required(login_url='accounts:login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)

########################################################################################################################
# ** home function ** to display homepage
########################################################################################################################


# @login_required(login_url='/login/')
def home(request):
    context = {}
    return render(request, 'index.html', context)

