from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    colab = models.CharField(max_length=255, blank=True, default='')
    youtube = models.CharField(max_length=255, blank=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = RichTextField(config_name='default',
                          extra_plugins=['codesnippet'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
