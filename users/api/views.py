from rest_framework import viewsets
from rest_framework.response import Response

from users.models import User, Invitation
from .serializers import UserSerializer, InvitationSerializer, UserDetailSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def create(self, request, *args, **kwargs):
        invitation_token = request.data.get('invitation_token')
        invited_user_id = request.data.get('invited_user_id')

        invited_by = User.objects.filter(invitation_token=invitation_token).first()
        invited_user = User.objects.filter(id=invited_user_id).first()

        if not invited_by or not invited_user:
            return Response({'detail': 'Invalid token or user ID'}, status=404)

        # Optional: Check if already invited
        if Invitation.objects.filter(invited_user=invited_user).exists():
            return Response({'detail': 'User has already been invited'}, status=400)

        if invited_by.id == invited_user.id:
            return Response({'detail': 'You can\'t invite yourself'}, status=400)

        data = {
            'invited_by': invited_by.id,
            'invited_user': invited_user.id
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=201)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return UserSerializer
        return UserDetailSerializer
