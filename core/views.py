from django.shortcuts import render
from django.views import View 
from .apps import APP_NAME


TEMPLATE_ROOT="core/"
LAYOUT_PARENT="phoenix/layout.html"

def CoreContext(request,app_name,*args, **kwargs):
    context={}
    context['farsi_font_name']=""
    return context


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
