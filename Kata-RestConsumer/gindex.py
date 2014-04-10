__author__ = 'Javier'


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

    def __init__(self, conector):
        self.conector = conector
        self.project_factory = ProjectFactory()

    def find(self, user, repo_name):
        raw_json = self._read_repo(user, repo_name)
        return self.project_factory.build_from(raw_json)

    def _read_repo(self, user, repo_name):
        repos = self.conector.read_all(user)
        for repo in repos:
            if repo['name'] == repo_name:
                return repo
        return None


class ProjectFactory(object):

    def build_from(self, json_project):
        return Project(json_project['forks_count'],
                       json_project['watchers_count'],
                        json_project['stargazers_count'])