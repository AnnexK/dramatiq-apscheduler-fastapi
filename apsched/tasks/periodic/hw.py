from .periodic_task import PeriodicTask


class HW(PeriodicTask):
    def perform(self):
        print("Hello world!")
