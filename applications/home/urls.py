from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.indexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resume-foundation/', views.ResumenFoundationView.as_view(), name = 'resume_foundation')
]
