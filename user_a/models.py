from django.db import models
from django.core.urlresolvers import reverse

from djangotoolbox.fields import ListField, EmbeddedModelField


class Language(models.Model):
	detected_at = models.DateTimeField(auto_now_add=True, db_index=True)
	language_name = models.CharField(max_length=255)






