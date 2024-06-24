from django.urls import path
from .views import chatbot , blog_list, change_language,bot


urlpatterns = [
    path('',bot, name='bot'),
    path('chatbot/', chatbot, name='chatbot'),
    path('blog/',blog_list, name='blog_list'),
    path('change-language/',change_language, name='change_language'),
    
    ]