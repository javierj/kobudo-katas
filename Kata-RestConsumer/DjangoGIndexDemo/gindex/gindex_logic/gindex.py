__author__ = 'Javier'

import urllib.request
import json

class Repo(object):
    def __init__(self, fork, stars, watchers):
        self._fork = int(fork)
        self._stars = int(stars)
        self._watchers = int(watchers)

    @property
    def forks(self):
        return self._fork

    @property
    def stars(self):
        return self._stars

    @property
    def watchers(self):
        return self._watchers


class GIndexCalculator(object):
    def calc(self, repo_info):
        return (repo_info.forks *3) + repo_info.stars + repo_info.watchers


class RepositoryService(object):
    def get_repos_from(self, user):
        url = "https://api.github.com/users/"+user+"/repos"
        connection = urllib.request.urlopen(url)
        result_raw = connection.read().decode('utf-8')
        repos = json.loads(result_raw)
        return repos

    def find_repo(self, repos, repo_name):
        for repo in repos:
            if repo['name'] == repo_name:
                return repo
        return None

    def get_repo(self, user, repo_name):
        repos = self.get_repos_from(user)
        repo = self.find_repo(repos, repo_name)
        print(repo)
        return Repo(repo['forks_count'], repo['stargazers_count'], repo['watchers_count'])



class GIndexPresenter(object):
    def __init__(self, view, service):
        self.view = view
        self.service = service

    def show_gindex(self, user, repo_name):
        repo_info = self.service.get_repo(user, repo_name)
        calculator = GIndexCalculator()
        gindex = calculator.calc(repo_info)
        self.view.show(gindex)
