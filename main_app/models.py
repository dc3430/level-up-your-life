from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import date


IMPORTANCE = (
    ('1', 'Low Importance'),
    ('3', 'Medium Importance'),
    ('5', 'High Importance')
)

DAYS = (
    ('1', 'Sunday'),
    ('2', 'Monday'),
    ('3', 'Tuesday'),
    ('4', 'Wednesday'),
    ('5', 'Thursday'),
    ('6', 'Friday'),
    ('7', 'Saturday'),
)

class Workout(models.Model):
  workout = models.CharField(max_length=250)
  importance = models.CharField(
    max_length=1,
    choices=IMPORTANCE,
    default=IMPORTANCE[0][1],
  )

  def get_absolute_url(self):
    return reverse('workout_detail', kwargs={'pk': self.id})

class MealPlan(models.Model):
  name = models.CharField(max_length=50)
  breakfast = models.CharField(max_length=50)
  lunch = models.CharField(max_length=50)
  dinner = models.CharField(max_length=50)

  def get_absolute_url(self):
    return reverse('mealplan_detail', kwargs={'pk': self.id})


class User(AbstractUser):
  pass
  score = models.IntegerField(default=0)
  level = models.CharField(max_length=100, default='Newbie')

class Journal(models.Model):
  title = models.CharField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  about = models.TextField(max_length=2500)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('journal_detail', kwargs={'pk': self.id}) 

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=2500)
  importance = models.CharField(
    max_length=1,
    choices=IMPORTANCE,
    default=IMPORTANCE[0][1],
  )

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('task_detail', kwargs={'pk': self.id}) 
  
  def __str__(self):
    return f"{self.get_progress_display()} on {self.title}"
  
  def __str__(self):
    return f"{self.get_importance_display()} on {self.title}"

class Post(models.Model):
  date = models.DateField(default=date.today)
  mealplan = models.ManyToManyField(MealPlan)
  day = models.CharField(
    max_length=1,
    choices=DAYS,
    default=DAYS[0][0],
  )
  journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
  assignedtasks = models.ManyToManyField(Task, related_name="assignedTasks")
  completedtasks = models.ManyToManyField(Task, related_name="completedTasks")
  assignedworkout = models.ManyToManyField(Workout, related_name="assignedWorkout")
  completedworkout = models.ManyToManyField(Workout, related_name="completedWorkout")
  

  def get_absolute_url(self):
    return reverse('post_detail', kwargs={'pk': self.id}) 

class Attachment(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Attachment for post_id: {self.post_id} @{self.url}"