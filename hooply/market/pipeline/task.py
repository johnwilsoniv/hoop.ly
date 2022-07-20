from typing import Protocol

class Task(Protocol):
    def run(self):
        pass


class IngestTeamsTask(Task):
    def run(self):
        print("Hello")


class IngestTeamsTask(Task):
    def run(self):
        print("Hello")

class IngestTeamsTask(Task):
    def run(self):
        print("Hello")