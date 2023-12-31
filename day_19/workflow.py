import re
from rule import Rule
from part import Part


class Workflow:
    def __init__(self, line):
        values = re.match(r'(\w+)\{(.*)\}', line)
        self.rules = [Rule(rule) for rule in values[2].split(',')]
        self.name = values[1]
    
    def get_output(self, part: Part):
        for condition in self.rules:
            result = condition.check(part)
            if result != None:
                return result
