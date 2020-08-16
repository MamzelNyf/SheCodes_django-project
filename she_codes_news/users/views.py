from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# class UpdateProfileView(generic.UpdateView):
#     model=Profile
#     form_class = ProfileUpdateForm
#     context_object_name = 'profile'
#     template_name = 'users/updateProfile.html'
#     success_url = reverse_lazy('profile')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
        

@login_required
def profile(request):
    print(request.method)
    if request.method == 'POST':
        u_form=CustomUserChangeForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect ('profile')

    else:
        u_form=CustomUserChangeForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form=CustomUserChangeForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect ('profile')

    else:
        u_form=CustomUserChangeForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/updateProfile.html', context)

# Try request.method == 'DELETE': to delete a profile