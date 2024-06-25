from django.urls import path
from .views import chatbot, blog_list, bot

urlpatterns = [
    path('', blog_list, name='blog_list'),  # Page d'accueil ou liste des blogs
    path('chatbot/', chatbot, name='chatbot'),  # Vue pour le chatbot
    path('bot/', bot, name='bot'),  # Vue pour la page du bot (si nécessaire)
]