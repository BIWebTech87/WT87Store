from django.urls import path
from .views import IndexUser, UsersViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'users'

urlpatterns = [
    # path('', IndexUser.as_view(), name='index'),
    path('', UsersViewSet.as_view({'post': 'create', }), name="users"),
    path('<int:pk>/', UsersViewSet.as_view({
        'delete': 'destroy',
        'patch': 'partial_update',
        'put': 'update',
        'get': 'retrieve'
    }), name="users"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
