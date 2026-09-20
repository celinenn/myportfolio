import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
        ('bootcamp', 'Bootcamp'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_LEVELS = [
        ('highschool', 'Highschool'),
        ('bachelors', 'Bachelors'),
        ('masters', 'Masters'),
        ('doctoral', 'Doctoral')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    school = models.CharField(max_length=255, default='Unknown')
    category = models.CharField(max_length=20, choices=EDUCATION_LEVELS)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    class Skill(models.Model):
        SKILL_TYPE = [
            ('language', 'Language'),
            ('soft-skill', 'Soft-Skill'),
            ('hard-skill', 'Hard-Skill')
        ]

        LANGUAGE_LEVEL = [
            ('native', 'Native'),
            ('first-language', 'First Language'),
            ('fluent', 'Fluent'),
            ('intermediate', 'Intermediate'),
            ('beginner', 'Beginner'),
        ]
        
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        title = models.CharField(max_length=255)
        type = models.CharField(max_length=20, choices=SKILL_TYPE)
        language_level = models.CharField(max_length=30, choices=LANGUAGE_LEVEL, null=True)
        level = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(10)], 
                blank=True, 
                null=True
            )
        
        def __str__(self):
            return self.title
        
        @property
        def is_ongoing(self):
            return self.ended_at is None