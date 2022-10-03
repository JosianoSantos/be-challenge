from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.football_data.api import viewsets

router = DefaultRouter()
router.register(r'leagues', viewsets.CompetitionViewset, basename="leagues")
router.register(r'players', viewsets.TeamMemberViewSet, basename="players")
router.register(r'players-of-team', viewsets.MemberOfTeamViewSet, basename="players-of-team")
router.register(r'teams', viewsets.TeamViewSet, basename="teams")

urlpatterns = [
    path('', include(router.urls)),
]
