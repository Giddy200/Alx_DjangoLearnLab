from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')]
    CATEGORY_CHOICES = [('Meeting', 'Meeting'), ('Gym', 'Gym'), ('Fruit', 'Fruit'), ('Project', 'Project')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Meeting')

    #Lifestyle Fields
    fruit_goals = models.IntegerField(default=0)
    fruit_progress = models.IntegerField(default=0)
    exercise_goals = models.IntegerField(default=0)
    exercise_progress = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
       #Logic: if status is completed, set progress to timestamp
         if self.status == 'Completed' and not self.completed_at:
          self.completed_at = timezone.now()
         elif self.status == 'Pending':
          self.completed_at = None
         super().save(*args, **kwargs)

         def __str__(self):
            return f"{self.title} - {self.user.username}"