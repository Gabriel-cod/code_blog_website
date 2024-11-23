from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login/'
    model = User
    context_object_name = 'form'


class SignInView(LoginView):
    template_name = 'accounts/login.html'
    form_class = SignInForm
    redirect_authenticated_user = True
