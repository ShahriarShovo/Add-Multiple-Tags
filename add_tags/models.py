from django.db import models

# Create your models here.

class Tags(models.Model):
    tag_name=models.CharField(max_length=1000, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.tag_name)