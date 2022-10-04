from django.test import TestCase
from django.urls import reverse

from apps.football_data.models import Competition, Team, TeamMember


class IndexTests(TestCase):

    @classmethod
    def setUpTestData(self):
        self.competition = Competition.objects.create(
            name='Competition test',
            area_name='Brazil',
            code='BSA',
            competition_id=1,
        )
        self.competition2 = Competition.objects.create(
            name='Competition test2',
            area_name='Brazil',
            code='LDA',
            competition_id=2,
        )

        self.team = Team.objects.create(
            name='Team test',
            area_name='Brazil',
            short_name='Team',
            address='Street',
            tla='TT',
            team_id=1,
        )

        self.team2 = Team.objects.create(
            name='Another team',
            area_name='Brazil',
            short_name='Team2',
            address='Street',
            tla='TT',
            team_id=2,
        )

        self.team.competitions.add(self.competition)
        self.team2.competitions.add(self.competition2)

        TeamMember.objects.create(
            name='John doe',
            team=self.team,
            member_id=1,
            position='Goalkeeper',
            nationality='Brazilian',
            role=TeamMember.PLAYER,
            date_of_birth='1998-06-23',
        )
        TeamMember.objects.create(
            name='Jane doe',
            team=self.team2,
            member_id=1,
            position='Goalkeeper',
            nationality='Brazilian',
            role=TeamMember.PLAYER,
            date_of_birth='1998-06-23',
        )

    def test_get_players(self):
        all_members = self.client.get(reverse('players-list'))
        self.assertEqual(all_members.status_code, 200)

        filter_by_league_code = self.client.get(reverse('players-list') + '?league_code=BSA')
        self.assertEqual(filter_by_league_code.status_code, 200)

        filter_by_team_name = self.client.get(reverse('players-list') + '?team_name=Another team')
        self.assertEqual(filter_by_team_name.status_code, 200)

    def test_get_teams(self):
        all_teams = self.client.get(reverse('teams-list'))
        self.assertEqual(all_teams.status_code, 200)

        filter_by_team_name_no_members = self.client.get(reverse('teams-list') + '?name=Team test&show_members=false')
        self.assertEqual(filter_by_team_name_no_members.status_code, 200)
        self.assertEqual(filter_by_team_name_no_members.json()[0].get('members') , None)

        filter_by_team_name_with_members = self.client.get(reverse('teams-list') + '?name=Team test&show_members=true')
        self.assertEqual(filter_by_team_name_with_members.status_code, 200)
        self.assertNotEqual(filter_by_team_name_with_members.json()[0].get('members') , None)

    def test_players_of_team(self):
        response = self.client.get(reverse('players-of-team-list') + '?team_name=Team test')
        self.assertEqual(response.status_code, 200)
