from rest_framework import serializers

from apps.football_data.models import Team, TeamMember, Competition


class ImportCompetitionSerializer(serializers.Serializer):
    league_code = serializers.CharField()


class MemberOfTeamSerializer(serializers.Serializer):
    team_name = serializers.CharField()


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        exclude = ['id', 'team']

    def get_role(self, obj):
        return obj.get_role_display()


class TeamSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(source="teammember_set", many=True, read_only=True)
    competitions = CompetitionSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['name', 'tla', 'short_name', 'area_name', 'address', 'members', 'competitions']

    def get_fields(self):
        fields = super().get_fields()

        if not self.context.get('show_members', None):
            fields.pop('members', default=None)

        return fields
