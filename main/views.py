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
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Celine",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_education(request):
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Celine",
        "education_list": educations,
        "title_query": title_query,
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

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")