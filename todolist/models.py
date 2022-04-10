from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50,)
    description = models.TextField(null=True,)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']