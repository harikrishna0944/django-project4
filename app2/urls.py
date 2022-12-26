from django.urls import path
from app2.views import *
app_name="somiting2"


urlpatterns = [
    path("hari/",hari,name="hari"),
    path("krishna/",krishna,name="krishna")
]
    
