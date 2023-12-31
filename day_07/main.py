import sys

# sys.argv[1]: input file to use
# sys.argv[2]: part of the daily challenge to run

def card_value(card):
    # Assign individual value for each card
    try:
        return int(card)
    except:
        card_values         = {'A': 14, 'K': 13, 'Q': 12, 'T': 10 }
        card_values['J']    = 1 if sys.argv[2] == '2' else 11 # 'J' value changes for part 2

        return card_values[card]


def get_hand_value(cards):
    # Get hand value considering the count of the most repeated card
    # 7: 5 equal cards, 6: 4 equal cards, 5: full house, 4: 3 equal cards, 
    # 3: two pairs: 2: one pair, 1: no repeated card

    cards_count     = { i:cards.count(i) for i in cards }
    cards_values    = [card_value(card) for card in cards]

    # Part 2
    if sys.argv[2] == '2':

        if cards == "JJJJJ":
            return (7, *cards_values)

        if 'J' in cards_count.keys():

            # Get count of 'J' and remove it from dict
            buffer = cards_count['J']
            cards_count.pop('J')

            # Get max count and look for key with that value (without considering 'J')
            key = list(cards_count.keys())[list(cards_count.values()).index(max(cards_count.values()))]

            # Add count to that key and insert 'J' with count = 0
            cards_count[key]    += buffer
            cards_count['J']    = 0

    # Assign hand values
    hand_value = 0
    if 3 in cards_count.values() and 2 in cards_count.values(): # Full house
        hand_value = 5
    elif list(cards_count.values()).count(2) == 2:              # Two pairs
        hand_value = 3
    else:
        hand_value = { 5: 7, 4: 6, 3: 4, 2: 2, 1: 1 }[max(cards_count.values())]

    # Return the hand value along with the value of each individual card in order
    return (hand_value, *cards_values)

    
def main():
    # Load file
    file = open(sys.argv[1])
    hands, bids = zip(*[line.split() for line in file.read().splitlines()])
    file.close()

    # Sort hands by using the hand value tuple 
    # 1st vector: hands
    # 2nd vector: bids (converted to int)
    # Criteria: tuple: (hand value, 1st card value, ..., 5th card value)
    sorted_hands = sorted(zip(hands, map(int, bids)), key=lambda t: get_hand_value(t[0]))

    # Return sum of products of rank (i) and bid
    return sum([i * bid for i, (_, bid) in enumerate(sorted_hands, 1)])

if __name__ == "__main__":
    print(main())

