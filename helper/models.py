import uuid
from django.db import models


class CreationModificationBase(models.Model):
    """Mixin for adding creation and modification datetime."""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,unique=True)
    created = models.DateTimeField(auto_now_add=True, help_text="When this instance was created.")
    modified = models.DateTimeField(auto_now=True, help_text="When this instance was modified.")
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True,null=True)

    class Meta:
        abstract = True