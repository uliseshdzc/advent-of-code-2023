import re


class Part:
    def __init__(self, line):
        values = re.match(r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}', line)
        self.x = int(values[1])
        self.m = int(values[2])
        self.a = int(values[3])
        self.s = int(values[4])
        self.workflow = "in"

    def set_workflow(self, workflow: str):
        self.workflow = workflow
        return self.workflow in "AR"
    
    def get_value(self):
        return self.x + self.m + self.a + self.s