from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """The url or keyword the user is going to download."""
    content = models.TextField()
    email = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return a string representation of the model.""" 
        return self.content
