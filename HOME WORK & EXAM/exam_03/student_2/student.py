class Student:

    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress

    def __repr__(self):
        return self.name
