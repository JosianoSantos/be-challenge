from datetime import datetime

from apps.football_data.models import TeamMember, Team, Competition


def create_team_member(member: dict, team: Team, role=TeamMember.PLAYER) -> None:
    TeamMember.objects.get_or_create(
        name=member.get('name'),
        position=member.get('position'),
        nationality=member.get('nationality'),
        role=role,
        date_of_birth=datetime.strptime(member.get('dateOfBirth'), '%Y-%m-%d') if member.get('dateOfBirth') else None,
        defaults={
            'member_id': member.get('id'),
            'team': team
        }
    )


def get_or_create_team(team: dict) -> Team:
    return Team.objects.get_or_create(
        name=team.get('name'),
        tla=team.get('tla'),
        area_name=team.get('area').get('name'),
        short_name=team.get('shortName'),
        address=team.get('address'),
        defaults={'team_id': team.get('id')}
    )[0]


def get_or_create_competition(data: dict) -> Competition:
    return Competition.objects.get_or_create(
        name=data.get('name'),
        code=data.get('code'),
        area_name=data.get('area').get('name'),
        defaults={'competition_id': data.get('id')}
    )[0]
