from django.urls import path
from . import views 


app_name = 'contact'

urlpatterns = [
    path('' ,views.contact , name='contacto'),
    path('logout/', views.logout_view , name='logout'),
    path('login/' , views.login_view , name='login'),
    path('about/', views.about, name='about'),
]
