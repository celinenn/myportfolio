from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from main import api_views

app_name = "api"
urlpatterns = [
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("educations/", api_views.education_list, name="education-list"),
    path("skills/", api_views.skill_list, name="skill-list"),
    path("experiences/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("educations/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    path("skills/<uuid:skill_id>/", api_views.skill_detail, name="skill-detail"),
    path("experiences/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("educations/<uuid:education_id>/star/", api_views.education_star, name="education-star"),
    path("skills/<uuid:skill_id>/star/", api_views.skill_star, name="skill-star"),
]