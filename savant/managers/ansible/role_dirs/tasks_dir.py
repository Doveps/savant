# Copyright (c) 2015 Kurt Yoder
# See the file LICENSE for copying permission.
from . import common

class Tasks(common.Directory):
    required_file = 'main.yml'

    def add(self, entry):
        # TODO: allow appending to other .yml files
        '''Append a task to main.yml'''
        target = self.file_data[Tasks.required_file]
        target.append(entry.as_directive())
        self.added += 1

    def get_report(self):
        return 'tasks: added %d'%self.added

