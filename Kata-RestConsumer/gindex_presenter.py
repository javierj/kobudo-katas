__author__ = 'Javier'

from gindex import GIndex, ProjectRepositoryService

class GIndexPresenter(object):

    def __init__(self, view, repo_service = ProjectRepositoryService()):
        self.view = view
        self.gindex_calc = GIndex()
        self.repo_service = repo_service

    def request_gindex_for(self, user, repo):
        project = self.repo_service.find(user, repo)
        gindex = self.gindex_calc.calculate(project)
        self.view.show_gindex(gindex)

