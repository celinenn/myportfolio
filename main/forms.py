from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput, NumberInput

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
                }, format='%Y-%m-%dT%H:%M'
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%dT%H:%M'
            ),
        }
    
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
                }, format='%Y-%m-%dT%H:%M'
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }, format='%Y-%m-%dT%H:%M'
            ),
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "title",
            "type",
            "language_level",
            "level",
        ]

        labels = {
            "title": "Skill Title",
            "type": "Skill Type",
            "language_level": "Language Level (If Applicable)",
            "level": "Skill Level (1-10)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g. Python or Indonesian",
                    "maxlength": 255,
                }
            ),
            "level": NumberInput(
                attrs={
                    "min": 1,
                    "max": 10,
                    "placeholder": "1-10",
                }
            ),
        }