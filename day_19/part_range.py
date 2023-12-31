import copy
from rule import Rule


class PartRange:
    def __init__(self, workflow):
        self.workflow = workflow
        self.x = range(1, 4000)
        self.m = range(1, 4000)
        self.a = range(1, 4000)
        self.s = range(1, 4000)

    def get_value(self):
        return  (self.x.stop - self.x.start + 1) * \
                (self.m.stop - self.m.start + 1) * \
                (self.a.stop - self.a.start + 1) * \
                (self.s.stop - self.s.start + 1)
    
    def return_new_workflow(self, workflow):
        nwr = copy.copy(self)
        nwr.workflow = workflow
        return nwr, None

    def split_by_rule(self, rule: Rule):

        cr = getattr(self, rule.input)

        if rule.operator == '<' and cr.start < rule.value:
            if cr.stop <= rule.value:
                return self.return_new_workflow(rule.output)

            nwr = copy.copy(self)
            swr = copy.copy(self)
            nwr.workflow = rule.output
            setattr(nwr, rule.input, range(cr.start, min(cr.stop, rule.value - 1)))
            setattr(swr, rule.input, range(rule.value, cr.stop))
            return nwr, swr
        
        if rule.operator == '>' and cr.stop > rule.value:
            if cr.start >= rule.value:
                return self.return_new_workflow(rule.output)
            
            nwr = copy.copy(self)
            swr = copy.copy(self)
            setattr(nwr, rule.input, range(max(cr.start, rule.value + 1), cr.stop))
            setattr(swr, rule.input, range(cr.start, rule.value))
            return nwr, swr
        
        if rule.operator == None:
            return self.return_new_workflow(rule.output)

        
        return None, self