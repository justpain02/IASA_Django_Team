from django.forms.formsets import INITIAL_FORM_COUNT
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views import View
from .forms import UserForm, ProfileForm
from django.shortcuts import redirect

# Create your views here.

class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = "profiles/profile_user.html"

class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        user_form = UserForm(initial={
            'first_name': user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
        })

        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'profile_photo': profile.profile_photo,
            })

        else:
            profile_form = ProfileForm()
    
        return render(request, 'profiles/profile_update.html', {"user_form": user_form, 'profile_form':profile_form})

    def post(self, request):
        u = User.objects.get(id=request.user.pk)
        user_form = UserForm(request.POST, instance=u)

        if user_form.is_valid():
            user_form.save()
        
        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = ProfileForm(request.POST, request.FILES)
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = u
            profile.save()
        
        return redirect('profile', pk=request.user.pk)