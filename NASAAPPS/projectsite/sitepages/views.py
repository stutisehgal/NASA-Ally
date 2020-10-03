from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from sitepages.forms import CorporateSignUp,IndividualSignUp,CardInfoForm
from sitepages.models import User,Individual
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        return redirect('sitepages/login')

def save(request):
    
    if request.method == 'POST':
        obj = CardInfoForm(request.POST,request.FILES)
        try:
            if obj.is_valid():
                
                form = obj.save(commit=False)
                form.user = User.objects.get(id=request.user.id)
                form.is_filled = True
                form.save()
                return render(request,'sitepages/valid.html')
        except:
            return redirect('')
    else:
        obj = CardInfoForm()
    return render(request,'sitepages/personalinfoform.html',{'form':obj})
                
def personalinfovalid(request):
    return render(request,'sitepages/valid.html')


def SignUpChoice(request):
     return render(request,'sitepages/first.html')


def AllyAssessPage(request):
    return render(request,'sitepages/allyassess.html')


def ViewCards(request):
    all_info = Individual.objects.all()
    return render(request,'sitepages/profilecard.html',{'all_cards':all_info})