from openai import OpenAI
from django.shortcuts import render, redirect   
from .models import BlogPost
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import activate
from django.urls import reverse
from .forms import LanguageForm
from django.conf import settings
from .models import Chat


client = OpenAI(api_key="")
def bot(request):
    return render(request, 'chatbot.html')

def chatbot(request):

    if request.method == 'POST':
        message = request.POST.get('message', '')
        completion  = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        answer = completion.choices[0].message.content
        new_chat = Chat(message=message, response=answer)
        new_chat.save()
        return JsonResponse ({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)


def blog_list(request):
    posts = BlogPost.objects.all()  # Récupère tous les articles de blog
    return render(request, 'blog_list.html', {'posts': posts})

def my_view(request):
    language = request.GET.get('lang', 'en')  # 'en' est la langue par défaut
    activate(language)

    posts = BlogPost.objects.all()

    # Votre logique de vue
    context = {
        'posts' : posts,
        'current_language': language,

    }
    return render(request, 'blog_list.html', context)

def change_language(request):
    if request.method == 'POST':
        language_code = request.POST.get('language', 'en')
        translation.activate(language_code)
        response = redirect(request.META.get('HTTP_REFERER', reverse('home')))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
        return response











