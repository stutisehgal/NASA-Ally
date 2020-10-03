from django.conf.urls import url
from django.contrib.auth import views as auth_views
#this file already takes care of login and logout views.
from . import views

app_name = 'sitepages'

urlpatterns = [
        url(r"login/$",auth_views.LoginView.as_view(template_name='sitepages/login.html'),name='login'),
        url(r"logout/$",auth_views.LogoutView.as_view(),name='logout'),
        url(r"signupindividual/$",views.IndividualSignUpForm.as_view(),name='signupindividual'),
        url(r"signupcorporate/$",views.CorporateSignUpForm.as_view(),name='signupcorporate'),
        url(r"signupchoice/$",views.SignUpChoice,name='signupchoice'),
        url(r"ally_assess/$",views.AllyAssessPage,name='allyassess'),
        url(r"personalinfocard/$",views.showCardInfoForm,name='cardinfoform'),
        
    ]
#After making this we need to connect our sitepages to the full project using views and url.
#We will add it the main urls.py
