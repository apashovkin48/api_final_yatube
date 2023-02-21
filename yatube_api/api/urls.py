from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views
from django.urls import path, include

router = SimpleRouter()
router.register(
    'v1/posts',
    PostViewSet,
    basename='posts'
)
router.register(
    'v1/groups',
    GroupViewSet,
    basename='groups'
)
router.register(
    r'v1/posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
