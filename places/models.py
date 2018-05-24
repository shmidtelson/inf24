from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        """Return "app_label.model_label.manager_name"."""
        return '%s (id:%s)' % (self.title, self.pk)