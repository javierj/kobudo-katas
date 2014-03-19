__author__ = 'Javier'

import unittest
from gindex import GIndex, Project, ProjectRepositoryService
from gindex_presenter import GIndexPresenter
from unittest.mock import MagicMock
import httpretty


class TestProject(unittest.TestCase):

    def test_init_convetrs_string_into_int(self):
        project = Project("1", "2", "3")
        self.assertEquals(project.forks, 1)
        self.assertEquals(project.stars, 2)
        self.assertEquals(project.watchs, 3)


class TestGIndex(unittest.TestCase):

    def setUp(self):
        self.gindex = GIndex()

    def create_project(self, forks=0, stars=0, watchs=0):
        return Project(forks, stars, watchs)

    def test_when_project_has_no_forks_stars_watchs_gindex_is_0(self):
        result = self.gindex.calculate(self.create_project())
        self.assertEqual(result, 0)

    def test_when_project_has_one_forks_gindex_is_3(self):
        result = self.gindex.calculate(self.create_project(forks=1))
        self.assertEqual(result, 3)

    def test_when_project_has_forks_stars_and_watsh_use_them(self):
        result = self.gindex.calculate(self.create_project(forks=1, stars=1, watchs=1 ))
        self.assertEqual(result, 5)


class TestGIndexPresenter(unittest.TestCase):

    def setUp(self):
        pass

    def test_requesting_scikit_aero_project(self):
        view_mock = MagicMock()
        repo_service_mock = MagicMock()
        repo_service_mock.find = MagicMock(return_value=Project(2, 3, 3))
        presenter = GIndexPresenter(view_mock, repo_service_mock)
        presenter.request_gindex_for("Pybonacci", "scikit-aero")
        view_mock.show_gindex.assert_called_with(12)


class TestProjectRepositoryService(unittest.TestCase):

    def setUp(self):
       self.repo = ProjectRepositoryService()

    def mock_read(self, unused01, unused02):
        return {'forks_count':'2', 'watchers_count':'3', 'stargazers_count':'3'}

    def test_when_requesting_sckiti_aero_return_project_(self):
        self.repo._read_repo = self.mock_read
        project = self.repo.find("Pybonacci", "scikit-aero")
        self.assertEquals(project.forks, 2)
        self.assertEquals(project.stars, 3)
        self.assertEquals(project.watchs, 3)

    @httpretty.activate
    def test__read_report(self):
        httpretty.register_uri(httpretty.GET, "https://api.github.com/users/Pybonacci/repos",
                           body='[{"name": "scikit-aero"}]',
                           content_type="application/json")
        json_project = self.repo._read_repo("Pybonacci", "scikit-aero")
        self.assertEqual(json_project['name'], "scikit-aero")

    def test__create_github_url(self):
        url = self.repo._create_github_url("Pybonacci")
        self.assertEqual(url, "https://api.github.com/users/Pybonacci/repos")

    def test__build_project(self):
        josn_project={'forks_count':'2', 'watchers_count':'3', 'stargazers_count':'3'}
        project = self.repo._build_project(josn_project)
        self.assertEquals(project.forks, 2)
        self.assertEquals(project.stars, 3)
        self.assertEquals(project.watchs, 3)


if __name__ == '__main__':
    unittest.main()
