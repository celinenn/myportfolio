from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput, NumberInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import *

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "school",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Education Title",
            "school": "School Name",
            "category": "Education Level",
            "thumbnail": "Image Documented During Time Education was Taken",
            "started_at": "Start Date",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Computer Science Bachelors",
                    "maxlength": 255,
                }
            ),
            "school": TextInput(
                attrs={
                    "placeholder": "School Name",
                    "maxlength": 255,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/file/d/1br4lWOeHx40XD4zJv7dQsIh9kOK8wQqD/view?usp=sharing",
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%d'
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%d'
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Education name cannot just be filled with HTML tags.")
        return title

    def clean_school(self):
        return strip_tags(self.cleaned_data["school"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()
    
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience Title",
            "description": "Experience Description",
            "category": "Experience Type",
            "thumbnail": "Image Documented During Time Experience was Taken",
            "started_at": "Start Date",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Visual Design Staff at Open House Fasilkom UI 2025",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe Your Experience",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=1br4lWOeHx40XD4zJv7dQsIh9kOK8wQqD&sz=w1000",
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%d'
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%d'
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience name cannot just be filled with HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "title",
            "type",
            "proficiency",
        ]

        labels = {
            "title": "Skill Title",
            "type": "Skill Type",
            "proficiency": "Proficiency Level",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g. Python or Indonesian",
                    "maxlength": 255,
                }
            ),
        }
        
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Skill name cannot just be filled with HTML tags.")
        return title

    def clean_type(self):
        return strip_tags(self.cleaned_data["type"]).strip()

    def clean_proficiency(self):
        return strip_tags(self.cleaned_data["proficiency"]).strip()