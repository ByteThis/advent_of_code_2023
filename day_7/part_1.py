from functools import cmp_to_key

card_values = '23456789TJQKA'


def get_hand_rank(cards):
    card_counts = {card: cards.count(card) for card in set(cards)}

    if 5 in card_counts.values():
        return 6
    if 4 in card_counts.values():
        return 5
    if set(card_counts.values()) == {3, 2}:
        return 4
    if 3 in card_counts.values():
        return 3
    if len(card_counts) == 3:
        return 2
    if len(card_counts) == 4:
        return 1
    return 0


def compare_hands(h1, h2):
    if len(h1) == 0:
        return 0

    if h1[0] == h2[0]:
        return compare_hands(h1[1:], h2[1:])

    if card_values.index(h1[0]) < card_values.index(h2[0]):
        return -1
    else:
        return 1


def custom_compare(h1, h2):
    result = get_hand_rank(h1[0]) - get_hand_rank(h2[0])
    if result == 0:
        return compare_hands(h1[0], h2[0])
    return result


hands = []
with open("input", "r") as file:
    for line in file:
        cards, bet = line.strip().split(" ")
        hands.append((cards, bet))

    sorted_hands = sorted(hands, key=cmp_to_key(custom_compare))

    bets = [int(bet) for (_, bet) in sorted_hands]

    products = [(index + 1) * bet for index, bet in enumerate(bets)]
    result = sum(products)

    print(result)