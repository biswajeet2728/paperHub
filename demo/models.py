from django.db import models



# Create your models here.
class Paper(models.Model):

    subject = models.CharField(max_length=100)
    examination = models.CharField(max_length=100)
    semester = models.IntegerField()
    course = models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    file = models.FileField(upload_to="papers/", default="paper.pdf")


    def __str__(self):
        return self.subject

