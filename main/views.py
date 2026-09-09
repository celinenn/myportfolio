from django.shortcuts import render

from main.models import Experience, Education


def show_main(request):
    context = {
        "name": "Celine",
        "npm": "2506590201",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I am a self-motivated and creative individual with a great passion "
            "for the IT industry. I am currently in my first year of studying "
            "Computer Science at the University of Indonesia. I am organized "
            "in completing my tasks, allowing me to finish them in time, and "
            "able to work in a team."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Celine",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_education(request):
    context = {
        "name": "Celine",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)