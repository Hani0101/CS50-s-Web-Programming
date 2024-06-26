from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("hani", views.hani, name = "hani"),
    path("sunbul", views.sunbul, name = "sunbul"),
    path("<str:name>", views.greet, name="greet"),
    

]