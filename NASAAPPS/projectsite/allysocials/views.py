from django.shortcuts import render

# Create your views here.
def showallysocials(request):
    return render(request,'allysocials/index.html')


def showabtallysocials(request):
    return render(request,'allysocials/blog-single.html')
