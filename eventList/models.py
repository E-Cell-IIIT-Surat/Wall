from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=100)
    Desc=models.CharField(max_length=600, default="-----Default Desc------")
    image=models.ImageField(upload_to=f"static/images/")
    link=models.CharField(max_length=300)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    shown = models.BooleanField()

    def __str__(self) -> str:
        return self.title