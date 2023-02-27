from typing import List
from OOP.project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):

        for element in self.tasks:
            if task_name == element.name:
                element.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        completed_tasks = 0
        for element in self.tasks:
            if element.completed:
                self.tasks.remove(element)
                completed_tasks += 1

        return f'Cleared {completed_tasks} tasks.'

    def view_section(self):
        tasks = "\n".join(info.details() for info in self.tasks)
        return f'Section {self.name}:\n{tasks}'
