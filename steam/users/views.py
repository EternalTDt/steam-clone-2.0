from django.shortcuts import render, redirect
from .forms import RegistrForm
from django.contrib import messages
from django.core.mail import send_mail
from steam.settings import local as settings
from django.contrib.auth.decorators import login_required
from .forms import ProfileImage, UserUpdateForm
 
def register(request):
	if request.method == "POST":
		form = RegistrForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request, f'You are registered now, {username}!')
			send_mail(
				'You have successfully registered on Steam. <no-reply>',
				f'Hi, {username}.\nThank you for register on Steam. \n\nWe remind you, that you have chosen username {username}. You can edit any information in your own profile.\n\nSee ya.',
				settings.EMAIL_HOST_USER,
				[f'{email}'],
				fail_silently=False,
			)
			return redirect('/')
	else:
		form = RegistrForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(
            request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'img_profile': img_profile,
        'update_user': update_user,
    }

    return render(request, 'users/profile.html', data)