from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, ProfileForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountView(generic.TemplateView):
    # template_name = 'users/userAccount.html'
    pass

class UserView(generic.DetailView):
    # model = CustomUser
    # template_name = 'users/userAccount.html'
    pass

class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class UpdateProfileView(generic.CreateView):
    form_class = ProfileForm
    context_object_name = 'storyForm'
    template_name = 'users/updateProfile.html'
    success_url = reverse_lazy('users:userAccount')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def profile(request):
    return render(request, 'users/profile.html')