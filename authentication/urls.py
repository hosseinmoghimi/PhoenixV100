from django.urls     import path
from .apps import APP_NAME
from . import views
app_name=APP_NAME
urlpatterns = [
    path("",views.HomeViews.as_view(),name="home"),
    path("register/",views.HomeViews.as_view(),name="register"),
    path("login/",views.HomeViews.as_view(),name="login"),
]
