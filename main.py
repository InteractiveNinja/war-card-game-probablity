import random
from statistics import mean


def game():
    c = list(range(2, 16))
    deck = c + c + c + c

    def get_cards():
        cards = []
        for _ in range(0, 27):
            choice = random.choice(deck)
            deck.pop(deck.index(choice))
            cards.append(choice)
        return cards

    first_player_deck = get_cards()
    second_player_deck = get_cards()

    def turn():
        first_player_fighter = first_player_deck[0]
        second_player_fighter = second_player_deck[0]
        if first_player_fighter > second_player_fighter:
            #             # print("##")
            #             # print(str(first_player_fighter) + " wins against " + str(second_player_fighter))
            first_player_deck.append(second_player_fighter)
            first_player_deck.append(first_player_deck.pop(0))
            second_player_deck.pop(0)
        elif first_player_fighter < second_player_fighter:
            #             # print("##")
            #             # print(str(second_player_fighter) + " wins against " + str(first_player_fighter))
            second_player_deck.append(first_player_fighter)
            second_player_deck.append(second_player_deck.pop(0))
            first_player_deck.pop(0)
        else:
            # print("war")
            war()

    def war():
        first_player_fighter_sum = sum(first_player_deck[0:4])
        second_player_fighter_sum = sum(second_player_deck[0:4])
        if first_player_fighter_sum > second_player_fighter_sum:
            #             print(str(first_player_deck[:4]) + " wins against " + str(second_player_deck[:4]))
            first_player_deck.extend(second_player_deck[0:4])
            first_player_deck.extend(first_player_deck[0:4])
            del first_player_deck[:4]
            del second_player_deck[:4]
        else:
            #             print(str(second_player_deck[:4]) + " wins against " + str(first_player_deck[:4]))
            second_player_deck.extend(first_player_deck[0:4])
            second_player_deck.extend(second_player_deck[0:4])
            del first_player_deck[:4]
            del second_player_deck[:4]

    count = 0
    while len(first_player_deck) != 0 and len(second_player_deck) != 0:
        #         print("____")
        #         print(first_player_deck)
        #         print(second_player_deck)
        #         print("____")
        turn()
        count += 1

    # if len(first_player_deck) == 0:
    # # print("Second Player won")
    # if len(second_player_deck) == 0:
    # print("First Player won")
    #     print("Turns took " + str(count))
    return count


turns = []
for _ in range(100000):
    turns.append(game())

print(f'Min Turns: {min(turns)}')
print(f'Max Turns: {max(turns)}')
print(f'Average Turns: {mean(turns)}')
