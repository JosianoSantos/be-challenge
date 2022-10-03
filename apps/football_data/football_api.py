import requests

from django.conf import settings


class FootballAPI:
    endpoint = 'http://api.football-data.org/v4/'
    competition_endpoint = 'competitions/'
    team_endpoint = 'teams'

    def __init__(self):
        self.headers = {'X-Auth-Token': settings.FOOTBALL_DATA_API_TOKEN}

    def getResponse(self, url: str):
        request = requests.get(url, headers=self.headers)

        status_code = request.status_code
        if status_code == requests.codes.ok:
            return request
        elif status_code == requests.codes.bad:
            raise Exception('Invalid request.')
        elif status_code == requests.codes.forbidden:
            raise Exception('This resource is restricted for paid subscriptions.')
        elif status_code == requests.codes.not_found:
            raise Exception('Resource not found.')
        elif status_code == requests.codes.too_many_requests:
            raise Exception('The maximum number of requests allowed has been exceeded.')

    def getCompetitions(self, code: str) -> dict:
        return self.getResponse(f'{self.endpoint}{self.competition_endpoint}{code}').json()

    def getTeamsCompetition(self, competition_id):
        return self.getResponse(
            f'{self.endpoint}'
            f'{self.competition_endpoint}{competition_id}/'
            f'{self.team_endpoint}').json()
