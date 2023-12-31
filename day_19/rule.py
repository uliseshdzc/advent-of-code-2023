import re

from part import Part


class Rule:
    def __init__(self, line):
        if not ':' in line:
            self.input = "x"
            self.output = line
            self.value = ""
            self.compare = lambda part, input: True
            self.operator = None
        else:
            values = re.match(r'(\w+)(.*?)(\d+):(\w+)', line)
            self.input = values[1]
            self.value = int(values[3])
            self.output = values[4]
            self.operator = values[2]
            if self.operator == '>':
                self.compare = lambda part, input: part > input
            if self.operator == '<':
                self.compare = lambda part, input: part < input

    def check(self, part: Part):
        if self.compare(part.__getattribute__(self.input), self.value):
            return self.output
        