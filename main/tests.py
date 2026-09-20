from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import *


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

        self.education = Education.objects.create(
            title="Computer Science Bachelors",
            school="Universitas Indonesia",
            category="bachelors"
        )

        self.skill = Skill.objects.create(
            title="Python",
            type="hard-skill",
            proficiency="advanced"
        )

    def test_main_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertNotContains(response, self.education.title)
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_education_model(self):
        self.assertEqual(str(self.education), "Computer Science Bachelors")
        self.assertEqual(self.education.category, "bachelors")
        self.assertTrue(self.education.is_ongoing)

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(self.skill.type, "hard-skill")
        self.assertEqual(self.skill.proficiency, "advanced")

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.title)
        self.assertContains(response, self.education.school)
        self.assertContains(response, "Bachelors")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, "Hard-Skill")
        self.assertContains(response, "Advanced")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "No education has been added yet.")

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "No skills have been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Finished")
        self.assertNotContains(response, "Ongoing")

    def test_completed_education(self):
        self.education.ended_at = timezone.now()
        self.education.save()
        response = self.client.get(reverse("main:show_education"))

        self.assertFalse(self.education.is_ongoing)
        self.assertContains(response, "Finished")
        self.assertNotContains(response, "Ongoing")

    def test_json_endpoints(self):
        response_exp = self.client.get(reverse("main:get_experiences_json"))
        response_edu = self.client.get(reverse("main:get_educations_json"))
        response_skill = self.client.get(reverse("main:get_skills_json"))

        self.assertEqual(response_exp.status_code, 200)
        self.assertEqual(response_edu.status_code, 200)
        self.assertEqual(response_skill.status_code, 200)