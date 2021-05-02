from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('questionnaire', views.questionnaire, name='questionnaire' ),
    path('result', views.result, name='result')

]
