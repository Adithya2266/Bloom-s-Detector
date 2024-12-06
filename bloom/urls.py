from django.urls import path
from . import views
from.views import home

urlpatterns = [

    path('questions/', views.home, name='home'),
    path('submit_question/', views.question_view, name='submit_question'),
    path('',views.welcome_view,name='welcome_view'),
    # Bloom Level CRUD
    path('bloom_levels/', views.list_bloom_levels, name='list_bloom_levels'),
    path('bloom_levels/add/', views.add_bloom_level, name='add_bloom_level'),
    path('bloom_levels/update/<int:pk>/', views.update_bloom_level, name='update_bloom_level'),
    path('bloom_levels/delete/<int:pk>/', views.delete_bloom_level, name='delete_bloom_level'),

    # Course CRUD
    path('courses/', views.list_courses, name='list_courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/update/<int:pk>/', views.update_course, name='update_course'),
    path('courses/delete/<int:pk>/', views.delete_course, name='delete_course'),

    # Course Outcome CRUD
    path('course_outcomes/', views.list_course_outcomes, name='list_course_outcomes'),
    path('course_outcomes/add/', views.add_course_outcome, name='add_course_outcome'),
    path('course_outcomes/update/<int:pk>/', views.update_course_outcome, name='update_course_outcome'),
    path('course_outcomes/delete/<int:pk>/', views.delete_course_outcome, name='delete_course_outcome'),

    # Program Outcome CRUD
    path('program_outcomes/', views.list_program_outcomes, name='list_program_outcomes'),
    path('program_outcomes/add/', views.add_program_outcome, name='add_program_outcome'),
    path('program_outcomes/update/<int:pk>/', views.update_program_outcome, name='update_program_outcome'),
    path('program_outcomes/delete/<int:pk>/', views.delete_program_outcome, name='delete_program_outcome'),
    
    # Project overiew
    path('definitions/', views.definitions_page, name='definitions'),

]
