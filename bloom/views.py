from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import BloomLevelForm,CourseForm,QuestionForm
import json
from sentence_transformers import SentenceTransformer, util
import numpy as np
from .models import CourseOutcome, BloomLevel, ProgramOutcome
import random

model = SentenceTransformer('all-MiniLM-L6-v2')
from django.shortcuts import render, redirect


# Create a BloomLevel
def add_bloom_level(request):
    if request.method == 'POST':
        form = BloomLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bloom_levels')
    else:
        form = BloomLevelForm()
    return render(request, 'add_bloom_level.html', {'form': form})

# Read (list) BloomLevels
def list_bloom_levels(request):
    bloom_levels = BloomLevel.objects.all()
    return render(request, 'bloom_level_list.html', {'bloom_levels': bloom_levels})

# Update a BloomLevel
def update_bloom_level(request, pk):
    bloom_level = get_object_or_404(BloomLevel, pk=pk)
    if request.method == 'POST':
        form = BloomLevelForm(request.POST, instance=bloom_level)
        if form.is_valid():
            form.save()
            return redirect('list_bloom_levels')
    else:
        form = BloomLevelForm(instance=bloom_level)
    return render(request, 'update_bloom_level.html', {'form': form})

# Delete a BloomLevel
def delete_bloom_level(request, pk):
    bloom_level = get_object_or_404(BloomLevel, pk=pk)
    if request.method == 'POST':
        bloom_level.delete()
        return redirect('list_bloom_levels')
    return render(request, 'delete_bloom_level.html', {'bloom_level': bloom_level})


# Create a Course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

# Read (list) Courses
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Update a Course
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'update_course.html', {'form': form})

# Delete a Course (Cascade delete COs and POs)
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()  # Automatically deletes related COs and POs
        return redirect('list_courses')
    return render(request, 'delete_course.html', {'course': course})

from .models import CourseOutcome
from .forms import CourseOutcomeForm

# Create a CourseOutcome
def add_course_outcome(request):
    if request.method == 'POST':
        form = CourseOutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_course_outcomes')
    else:
        form = CourseOutcomeForm()
    return render(request, 'add_course_outcome.html', {'form': form})

# Read (list) CourseOutcomes
def list_course_outcomes(request):
    course_outcomes = CourseOutcome.objects.all()
    return render(request, 'course_outcome_list.html', {'course_outcomes': course_outcomes})

# Update a CourseOutcome
def update_course_outcome(request, pk):
    course_outcome = get_object_or_404(CourseOutcome, pk=pk)
    if request.method == 'POST':
        form = CourseOutcomeForm(request.POST, instance=course_outcome)
        if form.is_valid():
            form.save()
            return redirect('list_course_outcomes')
    else:
        form = CourseOutcomeForm(instance=course_outcome)
    return render(request, 'update_course_outcome.html', {'form': form})

# Delete a CourseOutcome
def delete_course_outcome(request, pk):
    course_outcome = get_object_or_404(CourseOutcome, pk=pk)
    if request.method == 'POST':
        course_outcome.delete()
        return redirect('list_course_outcomes')
    return render(request, 'delete_course_outcome.html', {'course_outcome': course_outcome})


from .models import ProgramOutcome
from .forms import ProgramOutcomeForm

# Create a ProgramOutcome
def add_program_outcome(request):
    if request.method == 'POST':
        form = ProgramOutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_program_outcomes')
    else:
        form = ProgramOutcomeForm()
    return render(request, 'add_program_outcome.html', {'form': form})

# Read (list) ProgramOutcomes
def list_program_outcomes(request):
    program_outcomes = ProgramOutcome.objects.all()
    return render(request, 'program_outcome_list.html', {'program_outcomes': program_outcomes})

# Update a ProgramOutcome
def update_program_outcome(request, pk):
    program_outcome = get_object_or_404(ProgramOutcome, pk=pk)
    if request.method == 'POST':
        form = ProgramOutcomeForm(request.POST, instance=program_outcome)
        if form.is_valid():
            form.save()
            return redirect('list_program_outcomes')
    else:
        form = ProgramOutcomeForm(instance=program_outcome)
    return render(request, 'update_program_outcome.html', {'form': form})

# Delete a ProgramOutcome
def delete_program_outcome(request, pk):
    program_outcome = get_object_or_404(ProgramOutcome, pk=pk)
    if request.method == 'POST':
        program_outcome.delete()
        return redirect('list_program_outcomes')
    return render(request, 'delete_program_outcome.html', {'program_outcome': program_outcome})

def welcome_view(request):
    return render(request, 'home1.html')
    
def home(request):
    courses = Course.objects.all()  
    return render(request, 'home.html', {'courses': courses})

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def map_blooms_level(question):
#     bloom_levels = BloomLevel.objects.all()
#     for bloom_level in bloom_levels:
#         keywords = bloom_level.get_keywords()
#         for keyword in keywords:
#             if keyword in question.lower():
#                 return bloom_level.level_name
#     return "unknown"

# def map_outcomes(question, course):
#     question_embedding = model.encode(question, convert_to_tensor=True)
    
#     # Retrieve course-specific COs and POs from the database
#     course_outcomes = CourseOutcome.objects.filter(course=course)
#     program_outcomes = ProgramOutcome.objects.filter(course=course)
    
#     # Convert descriptions to lists for encoding
#     co_descriptions = [co.description for co in course_outcomes]
#     po_descriptions = [po.description for po in program_outcomes]
    
#     # Encode descriptions for similarity matching
#     co_embeddings = model.encode(co_descriptions, convert_to_tensor=True)
#     po_embeddings = model.encode(po_descriptions, convert_to_tensor=True)
    
#     # Calculate similarity scores
#     co_similarity = util.pytorch_cos_sim(question_embedding, co_embeddings).numpy()[0]
#     po_similarity = util.pytorch_cos_sim(question_embedding, po_embeddings).numpy()[0]
    
#     # Find the best matching indices and convert them to Python int
#     best_co_index = int(np.argmax(co_similarity))  # Convert int64 to int
#     best_po_index = int(np.argmax(po_similarity))  # Convert int64 to int
    
#     # Retrieve the best-matching CO and PO based on indices
#     best_co = course_outcomes[best_co_index]
#     best_po = program_outcomes[best_po_index]
    
#     return best_co, best_po


# def question_view(request):
#     if request.method == 'POST':
#         course_id = request.POST.get('course')
#         course = Course.objects.get(id=course_id)
#         questions = request.POST.getlist('question')  # Retrieve multiple questions

#         # Prepare a results list to store each question's Bloom's level, CO, and PO mappings
#         results = []
#         for question in questions:
#             blooms_level = map_blooms_level(question)
#             best_co, best_po = map_outcomes(question, course)

#             results.append({
#                 'question': question,
#                 'course': course.course_name,
#                 'blooms_level': blooms_level,
#                 'co': best_co.description,
#                 'po': best_po.description,
#             })

#         # Pass results to the output template
#         return render(request, 'question_output.html', {'results': results})

#     # Retrieve available courses for selection
#     courses = Course.objects.all()
#     return render(request, 'home.html', {'courses': courses})


model = SentenceTransformer('all-MiniLM-L6-v2')

def map_blooms_level(question):
    bloom_levels = BloomLevel.objects.all()
    for bloom_level in bloom_levels:
        keywords = bloom_level.get_keywords()
        for keyword in keywords:
            if keyword in question.lower():
                return bloom_level.level_name
    return "Unknown"  # Updated to match your list of Bloom levels

def map_outcomes(question, course):
    question_embedding = model.encode(question, convert_to_tensor=True)
    
    # Retrieve course-specific COs and POs from the database
    course_outcomes = CourseOutcome.objects.filter(course=course)
    program_outcomes = ProgramOutcome.objects.filter(course=course)
    
    # Convert descriptions to lists for encoding
    co_descriptions = [co.description for co in course_outcomes]
    po_descriptions = [po.description for po in program_outcomes]
    
    # Encode descriptions for similarity matching
    co_embeddings = model.encode(co_descriptions, convert_to_tensor=True)
    po_embeddings = model.encode(po_descriptions, convert_to_tensor=True)
    
    # Calculate similarity scores
    co_similarity = util.pytorch_cos_sim(question_embedding, co_embeddings).numpy()[0]
    po_similarity = util.pytorch_cos_sim(question_embedding, po_embeddings).numpy()[0]
    
    # Find the best matching indices and convert them to Python int
    best_co_index = int(np.argmax(co_similarity))  # Convert int64 to int
    best_po_index = int(np.argmax(po_similarity))  # Convert int64 to int
    
    # Retrieve the best-matching CO and PO based on indices
    best_co = course_outcomes[best_co_index]
    best_po = program_outcomes[best_po_index]
    
    return best_co, best_po

def calculate_blooms_level_distribution(questions):
    total_questions = len(questions)
    # Initialize all Bloom levels with a count of 0
    bloom_count = {
        "Remembering": 0,
        "Understanding": 0,
        "Applying": 0,
        "Analyzing": 0,
        "Evaluating": 0,
        "Creating": 0
    }
    
    for question in questions:
        blooms_level = map_blooms_level(question)
        if blooms_level in bloom_count:
            bloom_count[blooms_level] += 1
        else:
            bloom_count["Unknown"] += 1  # Count as "Unknown" if not matched with predefined levels
    
    # Calculate percentages
    bloom_percentage = {
        level: (count / total_questions) * 100 for level, count in bloom_count.items()
    }
    return bloom_percentage

# def question_view(request):
#     if request.method == 'POST':
#         course_id = request.POST.get('course')
#         course = Course.objects.get(id=course_id)
#         questions = request.POST.getlist('question')  # Retrieve multiple questions

#         # Calculate the Bloom's level distribution for all questions
#         bloom_distribution = calculate_blooms_level_distribution(questions)

#         # Prepare a results list to store each question's Bloom's level, CO, and PO mappings
#         results = []
#         for question in questions:
#             blooms_level = map_blooms_level(question)
#             best_co, best_po = map_outcomes(question, course)

#             results.append({
#                 'question': question,
#                 'course': course.course_name,
#                 'blooms_level': blooms_level,
#                 'co': best_co.description,
#                 'po': best_po.description,
#             })

#         # Pass results and overall Bloom's level summary to the template
#         return render(request, 'question_output.html', {'results': results, 'bloom_summary': bloom_distribution})

#     # Retrieve available courses for selection
#     courses = Course.objects.all()
#     return render(request, 'home.html', {'courses': courses})

def question_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        total_marks = int(request.POST.get('total_marks', 0))

        # Retrieve section details
        section_marks = request.POST.getlist('section_marks[]')  # List of section marks
        questions_by_section = request.POST.getlist('question')  # Questions across all sections

        # Variables to store section-wise results
        section_results = []
        bloom_summary_by_section = {}

        # Iterate over sections
        for i, section_mark in enumerate(section_marks):
            section_questions = questions_by_section[i::len(section_marks)]  # Distribute questions into sections
            section_blooms_summary = calculate_blooms_level_distribution(section_questions)

            # Store section details and question mappings
            section_data = {
                'section_index': i + 1,
                'section_marks': section_mark,
                'questions': [],
                'bloom_summary': section_blooms_summary,
            }

            for question in section_questions:
                blooms_level = map_blooms_level(question)
                best_co, best_po = map_outcomes(question, course)

                section_data['questions'].append({
                    'question': question,
                    'blooms_level': blooms_level,
                    'co': best_co.description,
                    'po': best_po.description,
                })

            # Append section data to the section_results list
            section_results.append(section_data)
            bloom_summary_by_section[f"Section {i + 1}"] = section_blooms_summary

        # Render output with section-wise results and summary
        return render(request, 'question_output.html', {
            'course': course,
            'section_results': section_results,
            'bloom_summary_by_section': bloom_summary_by_section,
            'total_marks': total_marks,
        })

    # Retrieve available courses for selection
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})




###test
def definitions_page(request):
    return render(request, 'definitions.html')