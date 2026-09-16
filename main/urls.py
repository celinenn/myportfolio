from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("educations/add/", create_education, name="create_education"),
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("educations/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("experiences/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
]