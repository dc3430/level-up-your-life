from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('journals/', views.JournalList.as_view(), name='journal_index'),
  path('journals/create/', views.JournalCreate.as_view(), name='journal_create'),
  path('journals/<int:pk>/', views.JournalDetail.as_view(), name='journal_detail'),
  path('journals/<int:pk>/update/', views.JournalUpdate.as_view(), name='journal_update'),
  path('journals/<int:pk>/delete/', views.JournalDelete.as_view(), name='journal_delete'),
  path('journals/<int:journal_id>/assoc_post/<int:post_id>/', views.assoc_post, name='assoc_post'),
  path('journals/<int:journal_id>/unassoc_post/<int:post_id>/', views.unassoc_post, name='unassoc_post'),
  path('journals/<int:journal_id>/attachement/', views.add_attachment, name='add_attachment'),

  path('posts/', views.PostList.as_view(), name='post_index'),
  path('posts/create/', views.PostCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
  path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
  path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),

  path('tasks/', views.TaskList.as_view(), name='task_index'),
  path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),
  path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
  path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
  path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),

  path('workouts/', views.WorkoutList.as_view(), name='workout_index'),
  path('workouts/create/', views.WorkoutCreate.as_view(), name='workout_create'),
  path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout_detail'),
  path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout_update'),
  path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout_delete'),
  
  path('mealplan/', views.MealPlanList.as_view(), name='mealplan_index'),
  path('mealplan/create/', views.MealPlanCreate.as_view(), name='mealplan_create'),
  path('mealplan/<int:pk>/', views.MealPlanDetail.as_view(), name='mealplan_detail'),
  path('mealplan/<int:pk>/update/', views.MealPlanUpdate.as_view(), name='mealplan_update'),
  path('mealplan/<int:pk>/delete/', views.MealPlanDelete.as_view(), name='mealplan_delete'),
  path('accounts/signup', views.signup, name='signup'),
]