from django.urls import path
from cui_sahiwal import views

urlpatterns = [
    path('',views.create),
    path('get/',views.get),
]
