from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from sitepages.forms import CorporateSignUp,IndividualSignUp
from sitepages.models import User,Individual

# Create your views here.
class CorporateSignUpForm(CreateView):
    model = User
    form_class = CorporateSignUp
    template_name = 'sitepages/signup.html'
    

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'corporate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('sitepages/login')


class IndividualSignUpForm(CreateView):
    model = User
    form_class = IndividualSignUp
    template_name = 'sitepages/signup.html'
    

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'individual'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('sitepages/login')

def SignUpChoice(request):
     return render(request,'sitepages/first.html')


def AllyAssessPage(request):
    return render(request,'sitepages/allyassess.html')
