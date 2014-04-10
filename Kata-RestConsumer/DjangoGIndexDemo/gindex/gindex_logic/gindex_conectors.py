__author__ = 'Javier'

import urllib.request
import json


class GithubConnector(object):

    def read_all(self, user):
        url = self._create_github_url(user)
        page = urllib.request.urlopen(url)
        json_as_text = page.read().decode('utf-8')
        return json.loads(json_as_text)

    def _create_github_url(self, user):
        return "https://api.github.com/users/"+user+"/repos"