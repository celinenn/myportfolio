from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput, ChoiceField, Select

from main.models import Education, Experience

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
            "category": ChoiceField(
                choices=Education.EDUCATION_LEVELS,
                widget=Select,
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
            "category": ChoiceField(
                choices=Experience.EXPERIENCE_CHOICES,
                widget=Select,
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