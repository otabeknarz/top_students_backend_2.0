import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


def get_random_id():
    return uuid.uuid4().hex[:12]


class Invitation(models.Model):
    invited_by = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="invitations"
    )
    invited_user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="invited_by"
    )
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"@{self.invited_by} invited @{self.invited_user}"


class User(AbstractUser):
    id = models.CharField(max_length=32, primary_key=True, default=get_random_id)
    has_taken_gift = models.BooleanField(default=False)
    invitation_token = models.CharField(
        max_length=12, default=get_random_id, db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
