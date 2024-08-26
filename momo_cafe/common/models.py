import uuid

from django.db import models

from momo_cafe.authentication.models import User


class AbstractBase(models.Model):
    """Common model to be used throughout the project."""

    guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField()
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.UUIDField()

    class Meta:
        abstract = True


class Person(AbstractBase):
    """Person model."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class UserProfile(AbstractBase):
    """Links a user to a Person."""

    user = models.ForeignKey(
        User, related_name="user_profiles", on_delete=models.PROTECT
    )
    person = models.ForeignKey(
        Person, related_name="person_profiles", on_delete=models.PROTECT
    )
