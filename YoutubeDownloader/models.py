from django.db import models

class Task(models.Model):
    """The url or keyword the user is going to download."""
    content = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model.""" 
        return self.content
