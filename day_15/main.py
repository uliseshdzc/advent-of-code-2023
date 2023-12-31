import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def get_hash(str):
    value = 0
    for c in str:
        value += ord(c)
        value *= 17
        value %= 256

    return value

def main():

    # Load file and get data
    file = open(sys.argv[1])
    data = file.read().split(',')
    file.close()

    if sys.argv[2] == '1':
        return sum([get_hash(str) for str in data])
    
    if sys.argv[2] == '2':
        boxes = {}

        for str in data:
            if '-' in str:
                h = get_hash(str[:-1])

                # Check if hash exists in boxes, and if it exists, pop it
                if h in boxes.keys() and str[:-1] in boxes[h]:
                    boxes[h].pop(str[:-1])
                continue

            label, fl = str.split('=')
            h = get_hash(label)

            # If hash has not been added to boxes, create a new dictionary in that box
            if not h in boxes.keys():
                boxes[h] = {}

            # Add entry with label and focal length
            boxes[h][label] = int(fl)

        result = 0

        # Iterate over the boxes and slots and calculate the result
        for box, slots in boxes.items():
            for i, (slot, fl) in enumerate(slots.items(), start=1):
                result += (box + 1) * i * fl

        return result
    
if __name__ == "__main__":
    print(main()) 