import http.client
import json
import pandas as pd
from football_data.constants import SOCCER_CLI_API_TOKEN, SOCCER_API_HOST

import logging
logging.basicConfig(level='INFO')

API_CONN = http.client.HTTPConnection(SOCCER_API_HOST.replace('http://', ''))


def get_flat_result(route, request_type='GET', extra_headers=None):
    headers = {'X-Auth-Token': SOCCER_CLI_API_TOKEN, 'X-Response-Control': 'minified'}
    if extra_headers is not None:
        headers += extra_headers
    API_CONN.request(request_type, route, None, headers)
    response = json.loads(API_CONN.getresponse().read().decode())
    logging.info(response)
    return response


routes = ['/v1/competitions/?season=2015',
          '/v1/competitions/?season=2016',
          '/v1/competitions/445/teams',
          '/v1/teams/397',
          '/v1/competitions/445/leagueTable/?matchday=1',
          '/v1/competitions/445/fixtures',
          '/v1/teams/57/players'
          ]

for route in routes:
    get_flat_result(route)



