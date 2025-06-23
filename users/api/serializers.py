from rest_framework import serializers

from users.models import User, Invitation


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ("id", "invited_by", "invited_user", "status")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "has_taken_gift",
            "invitation_token",
        )


class InvitationDetailSerializer(serializers.ModelSerializer):
    invited_user = UserSerializer(read_only=True)

    class Meta:
        model = Invitation
        fields = (
            "id",
            "invited_by",
            "invited_user",
            "status",
            "created_at",
            "updated_at",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    invitations = InvitationDetailSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "invitations",
            "invitation_token",
        )
