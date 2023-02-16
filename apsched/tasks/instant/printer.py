from .instant_task import InstantTask


class Printer(InstantTask):
    def perform(self, to_print: str):
        print(to_print)
