from django.urls import path
from . import  views
urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # Page d'accueil ou liste des blogs
    path('chatbot/', views.chatbot, name='chatbot'),  # Vue pour le chatbot
    path('bot/', views.bot, name='bot'),  # Vue pour la page du bot (si nécessaire)
]