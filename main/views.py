from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from main.models import Experience, Education
from main.forms import ExperienceForm, EducationForm


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

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        education_item = form.save(commit=False)

        if not education_item.started_at:
            education_item.started_at = timezone.now()
        
        education_item.save()
        messages.success(request, "New education added!")
        return redirect("main:show_education")

    context = {
        "name": "Celine",
        "form": form,
    }
    return render(request, "educations_form.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        experience_item = form.save(commit=False)

        if not experience_item.started_at:
            experience_item.started_at = timezone.now()
        
        experience_item.save()
        messages.success(request, "New experience added!")
        return redirect("main:show_experience")

    context = {
        "name": "Celine",
        "form": form,
    }
    return render(request, "experiences_form.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")
