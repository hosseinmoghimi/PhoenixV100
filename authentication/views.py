 
# Create your views here.
from django.shortcuts import render
from django.views import View 
from core.views import CoreContext
from .apps import APP_NAME


TEMPLATE_ROOT="authentication/"
LAYOUT_PARENT="phoenix/layout.html"
 


def getContext(request,*args, **kwargs):
    context=CoreContext(request=request,app_name=APP_NAME,*args, **kwargs)
    context["TEMPLATE_ROOT"]=TEMPLATE_ROOT
    context["LAYOUT_PARENT"]=LAYOUT_PARENT 
    return context


class HomeViews(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context)
# Create your views here.
