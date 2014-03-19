__author__ = 'Javier'

import urllib.request
import json


class Project(object):

    def __init__(self, forks, stars, watchs):
        self._forks = int(forks)
        self._stars = int(stars)
        self._watchs = int(watchs)

    @property
    def forks(self):
        return self._forks

    @property
    def stars(self):
        return self._stars

    @property
    def watchs(self):
        return self._watchs


class GIndex(object):

    def calculate(self, project):
        return project.forks * 3 + project.stars + project.watchs


class ProjectRepositoryService(object):

    def find(self, user, repo_name):
        return self._build_project(self._read_repo(user, repo_name))

    def _read_repo(self, user, repo_name):
        url = self._create_github_url(user)
        page = urllib.request.urlopen(url)
        json_as_text = page.read().decode('utf-8')
        repos = json.loads(json_as_text)
        for repo in repos:
            if repo['name']  == repo_name:
                return repo
        return None

    def _create_github_url(self, user):
        return "https://api.github.com/users/"+user+"/repos"

    def _build_project(self, json_project):
        return Project(json_project['forks_count'],
                       json_project['watchers_count'],
                        json_project['stargazers_count'])