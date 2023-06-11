from rest_framework.routers import DefaultRouter

from .views import RoomsViewSet

app_name = 'rooms'

router = DefaultRouter()
router.register('rooms', RoomsViewSet, basename='room')
urlpatterns = router.urls
