# jetil_main/views
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.core.mail import send_mail
from .models import FreeLesson, Courses


def submit_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')

        # Отправляем письмо
        send_mail(
            'Новая заявка',
            f'Имя: {name}, Телефон: {phone_number}',
            'mereimag1@mail.ru',  # Отправитель
            ['mereimag1@mail.ru'],  # Получатель
            fail_silently=False,
        )
        return render(request,'index.html')

    return render(request, 'index.html')


def index(request):
    lessons = FreeLesson.objects.all()
    courses = Courses.objects.all()
    return render(request, 'jetil_main/index.html',
                  {'lessons': lessons,
                          'courses': courses})

def about(request):
    lessons = FreeLesson.objects.all()
    courses = Courses.objects.all()
    return render(request, 'jetil_main/about.html', {'lessons': lessons,
                                                                         'courses': courses,})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
