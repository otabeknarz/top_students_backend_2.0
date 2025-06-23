from rest_framework.routers import DefaultRouter

from users.api.views import UserViewSet, InvitationViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("invitations", InvitationViewSet)

urlpatterns = router.urls
