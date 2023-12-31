import math
import sys

from collections import deque

from module import Module

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def main():
    broadcaster = []
    data = {}
    hi = lo = 0
    presses = 0

    # Load data
    with open(sys.argv[1]) as file:
        for line in file.read().splitlines():
            source, destination = line.split(" -> ")
            if source == "broadcaster":
                broadcaster = destination.split(', ')
                continue

            # (type, state, [destinations])
            data[source[1:]] = Module(source[0], False, tuple(destination.split(", ")))

    # Get memory items for '&' type
    for key_module in [m for m in data.items() if m[1].type == '&']:
        key_module[1].memory = {item[0]: False for item in data.items() if key_module[0] in item[1].destinations}

    # For part 2
    if sys.argv[2] == '2':

        # It only has one origin
        rx_origin = [key for key, module in data.items() if 'rx' in module.destinations][0]

        # It is a '&' type, so all its inputs must be 'high' for it to be low
        # Create a dictionary to check how many presses it takes for those inputs to be high
        rx_origin_inputs = {key: 0 for key, module in data.items() if rx_origin in module.destinations}

    while presses < 1000 if sys.argv[2] == '1' else True:
        presses += 1
        lo += 1
        queue = deque([("broadcaster", target, False) for target in broadcaster])
        
        while queue:
            source, target, pulse = queue.popleft()
            hi += 1 if pulse else 0
            lo += 0 if pulse else 1            
            
            if not target in data:
                continue
            
            module = data[target]            
            result = None

            # For part 2
            if sys.argv[2] == '2' and target == rx_origin and pulse == True:
                rx_origin_inputs[source] = presses if rx_origin_inputs[source] == 0 else rx_origin_inputs[source]

                # If all the cycles have been captured; calculate the lcm to know at which point all the
                # cycles will converge being high
                if all(value > 0 for value in rx_origin_inputs.values()):
                    return math.lcm(*tuple(rx_origin_inputs.values()))

            if module.type == '%' and pulse == False:
                module.state = not module.state
                result = [(target, dest, module.state) for dest in module.destinations]
            
            if module.type == '&':
                module.memory[source] = pulse
                result = [(target, dest, not all(module.memory.values())) for dest in module.destinations]

            if result != None:
                queue.extend(result)

    return lo * hi

if __name__ == "__main__":
    print(main())