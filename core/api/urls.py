from rest_framework.routers import DefaultRouter
from user_data.api.urls import user_data_router
from django.urls import path, include

router = DefaultRouter()
# users
router.registry.extend(user_data_router.registry)

'userdata'
urlpatterns = [
    path('', include(router.urls))
]
