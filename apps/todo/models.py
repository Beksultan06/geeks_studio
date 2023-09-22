from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовка"
    )
    description = models.TextField(
        verbose_name="описание"
    )
    completed = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Датасоздание"
        )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Таски"