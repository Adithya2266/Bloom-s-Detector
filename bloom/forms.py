from django import forms
from .models import BloomLevel, Course, CourseOutcome, ProgramOutcome
from django.forms import formset_factory

# Form for BloomLevel model
class BloomLevelForm(forms.ModelForm):
    class Meta:
        model = BloomLevel
        fields = ['level_name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# Form for Course model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code']
        widgets = {
            'course_name': forms.TextInput(attrs={'placeholder': 'Enter course name'}),
            'course_code': forms.TextInput(attrs={'placeholder': 'Enter course code'}),
        }

# Form for CourseOutcome model
class CourseOutcomeForm(forms.ModelForm):
    class Meta:
        model = CourseOutcome
        fields = ['course', 'co_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# Form for ProgramOutcome model
class ProgramOutcomeForm(forms.ModelForm):
    class Meta:
        model = ProgramOutcome
        fields = ['course', 'po_number', 'description']  # Ensure that related_cos is a field
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# class QuestionForm(forms.Form):
#     question = forms.CharField(widget=forms.Textarea, label="Enter your question")
#     course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Select Course")

# QuestionFormSet = formset_factory(QuestionForm, extra=1)
    

class QuestionForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        to_field_name="id",  # This ensures that the ID of the course is used
        empty_label="Select Course",
    )
    question = forms.CharField(widget=forms.Textarea, required=True)