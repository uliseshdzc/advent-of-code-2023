import sys

from part import Part
from part_range import PartRange
from workflow import Workflow

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():

    # Load data
    file = open(sys.argv[1])
    rules_text, parts_text = file.read().split("\n\n")
    file.close()

    # Get lists of parts and workflows
    parts = [Part(part) for part in parts_text.splitlines()]
    workflows = {}
    for line in rules_text.splitlines():
        workflow = Workflow(line)
        workflows[workflow.name] = workflow

    if sys.argv[2] == '1':

        # For every part, iterate until 'A' or 'R' is reached
        for part in parts:
            while not part.set_workflow(workflows[part.workflow].get_output(part)):
                pass

        # Get the values of every part that is approved
        return sum([part.get_value() for part in parts if part.workflow == 'A'])

    if sys.argv[2] == '2':
        part_ranges = [PartRange("in")]
        total = 0

        while part_ranges:
            part_range = part_ranges.pop()

            # Skip if rejected
            if part_range.workflow == 'R':
                continue

            # Add to the total if approved
            if part_range.workflow == 'A':
                total += part_range.get_value()
                continue

            # Pass the ranges in every workflow
            for rule in workflows[part_range.workflow].rules:
                nwr, part_range = part_range.split_by_rule(rule)
                if nwr != None:
                    part_ranges.append(nwr)
                if part_range == None:
                    break

        return total


if __name__ == "__main__":
    print(main())