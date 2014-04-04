__author__ = 'Javier'


from gindex_presenter import GIndexPresenter


class ConsoleView(object):

    def show_gindex(self, gindex):
        print("Gindex: ", gindex)


# Runner
presenter = GIndexPresenter(ConsoleView())
presenter.request_gindex_for("Pybonacci", "scikit-aero")
