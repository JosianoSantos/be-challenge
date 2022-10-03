from django.db import transaction
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from apps.football_data.api.filters import TeamMemberFilter, TeamFilter, MemberOfTeamFilter
from apps.football_data.api.serializers import TeamSerializer, TeamMemberSerializer, ImportCompetiitonSerializer, \
    CompetitionSerializer
from apps.football_data.football_api import FootballAPI
from apps.football_data.models import TeamMember, Team

from apps.football_data.api import services


class CompetitionViewset(viewsets.ViewSet):
    serializer_class = ImportCompetiitonSerializer
    http_method_names = ['post']

    @extend_schema(
        request=ImportCompetiitonSerializer,
        responses={201: CompetitionSerializer},
    )
    @action(methods=["post"], detail=False)
    def import_league(self, request):
        league = request.data['league_code']
        try:
            with transaction.atomic():
                football_api = FootballAPI()

                res = football_api.getCompetitions(league)
                competition = services.get_or_create_competition(res)
                teams = football_api.getTeamsCompetition(competition.code)

                for team in teams.get('teams'):
                    team_obj = services.get_or_create_team(team)
                    team_obj.competitions.add(competition)

                    if team['squad']:
                        for player in team['squad']:
                            services.create_team_member(player, team_obj)
                    else:
                        services.create_team_member(team['coach'], team_obj, TeamMember.COACH)

            return Response(CompetitionSerializer(competition).data, status=HTTP_201_CREATED)

        except Exception as e:
            transaction.rollback()
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)


@method_decorator(decorator=extend_schema(
    parameters=[OpenApiParameter(
        name='show_members',
        type={'type': 'boolean', },
        location=OpenApiParameter.QUERY,
        required=True,
        style='form',
        explode=False,
    )],
), name='list')
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get']
    filterset_class = TeamFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['show_members'] = self.request.query_params.get('show_members') == 'true'
        return context


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    http_method_names = ['get']
    filterset_class = TeamMemberFilter


class MemberOfTeamViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    http_method_names = ['get']
    filterset_class = MemberOfTeamFilter
