from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from savant.api.savant.resources.comparison import ComparisonViewSet
from savant.api.savant.resources.diff import DiffViewSet
from savant.api.savant.resources.set import SetViewSet

router = routers.DefaultRouter()
router.register(r'comparisons', ComparisonViewSet)
router.register(r'diffs', DiffViewSet)
router.register(r'sets', SetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
