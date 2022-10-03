from django.db import models


class Competition(models.Model):
    competition_id = models.PositiveIntegerField()
    name = models.CharField('Name', max_length=255)
    code = models.CharField('Code', max_length=255)
    area_name = models.CharField('Code', max_length=255)


class Team(models.Model):
    team_id = models.PositiveIntegerField()
    name = models.CharField('Name', max_length=255)
    tla = models.CharField('Tla', max_length=255, null=True)
    short_name = models.CharField('Short name', max_length=255, null=True)
    area_name = models.CharField('Area', max_length=255)
    address = models.CharField('Adress', max_length=255)
    competitions = models.ManyToManyField(Competition)


class TeamMember(models.Model):
    PLAYER = 'PLAYER'
    COACH = 'COACH'

    ROLES = (
        (PLAYER, 'Player'),
        (COACH, 'Coach'),
    )

    member_id = models.PositiveIntegerField()
    name = models.CharField('Name', max_length=255)
    date_of_birth = models.DateField('Date of Birth', max_length=255, null=True)
    nationality = models.CharField('Nationality', max_length=255, null=True)
    position = models.CharField('Position', max_length=255, null=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    role = models.CharField('Role', max_length=6, choices=ROLES, default=PLAYER)
