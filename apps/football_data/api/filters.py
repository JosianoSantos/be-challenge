from django_filters import rest_framework as filters

from apps.football_data.models import Team, TeamMember


class TeamMemberFilter(filters.FilterSet):
    league_code = filters.CharFilter(field_name='team__competitions__code')
    team_name = filters.CharFilter(field_name='team__name', lookup_expr='icontains')

    class Meta:
        model = TeamMember
        fields = ['league_code', 'team_name', ]


class MemberOfTeamFilter(filters.FilterSet):
    team_name = filters.CharFilter(field_name='team__name', lookup_expr='icontains')

    class Meta:
        model = TeamMember
        fields = ['team_name', ]


class TeamFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['name']
