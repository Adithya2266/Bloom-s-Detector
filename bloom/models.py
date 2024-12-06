from django.db import models

class BloomLevel(models.Model):
    BLOOM_LEVELS = [
        ('Remembering', 'Remembering'),
        ('Understanding', 'Understanding'),
        ('Applying', 'Applying'),
        ('Analyzing', 'Analyzing'),
        ('Evaluating', 'Evaluating'),
        ('Creating', 'Creating'),
    ]

    level_name = models.CharField(max_length=50, choices=BLOOM_LEVELS, unique=True)
    description = models.TextField(help_text="Add keywords separated by commas")

    def _str_(self):
        return self.level_name

    # Get keywords from the description field
    def get_keywords(self):
        return [keyword.strip() for keyword in self.description.split(',')]



class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.TextField()

    def _str_(self):
        return self.course_name


class CourseOutcome(models.Model):
    course = models.ForeignKey(Course, related_name='cos', on_delete=models.CASCADE)  # Ensures deletion of COs when Course is deleted
    co_number = models.CharField(max_length=10)
    description = models.TextField()

    def _str_(self):
        return f"{self.course.course_name} - CO{self.co_number}"


class ProgramOutcome(models.Model):
    course = models.ForeignKey(Course, related_name='pos', on_delete=models.CASCADE)  # Ensures deletion of POs when Course is deleted
    po_number = models.CharField(max_length=10)
    description = models.TextField()
    def _str_(self):
        return f"{self.course.course_name} - PO{self.po_number}"
    
    

#test




