import random
from matplotlib import pyplot as plt

iterations = 10000
debug = False

player_wins = 0
computer_wins = 0
amount_of_deals = []

# Define the cards and their values
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

for iteration in range(iterations):

    # Create a full deck of cards
    deck = list(cards.keys()) * 4

    # Shuffle the deck
    random.shuffle(deck)

    # Distribute the cards evenly between the players
    player_hand = deck[:26]
    computer_hand = deck[26:]

    # Initialize piles for cards captured during the game
    player_pile = []
    computer_pile = []
    deal_amount = 0

    if iteration % (iterations / 10) == 0:
        print(f"Playing {iteration}/{iterations}...")

    # Play the game
    while len(player_hand) > 0 and len(computer_hand) > 0:

        deal_amount += 1

        # Player plays a card
        player_card = player_hand.pop(0)
        if (debug): print("Player plays: " + player_card.ljust(2), end=" | ")
        computer_pile.append(player_card)

        # Computer plays a card
        computer_card = computer_hand.pop(0)
        if (debug): print("Computer plays: " + computer_card.ljust(2), end=" | ")
        player_pile.append(computer_card)

        # Compare the cards played
        if cards[player_card] > cards[computer_card]:
            # Player captures the pile
            if (debug): print("Player captures the pile".ljust(59), end=" | ")
            player_pile += computer_pile
            player_hand += player_pile
            computer_pile = []
            player_pile = []
        elif cards[player_card] < cards[computer_card]:
            # Computer captures the pile
            if (debug): print("Computer captures the pile".ljust(59), end=" | ")
            computer_pile += player_pile
            computer_hand += computer_pile
            computer_pile = []
            player_pile = []
        else:
            # If the cards are the same value, another card is dealt to the pile
            if (debug): print("Cards are the same value, another card is dealt to the pile".ljust(59), end=" | ")
        if (debug): print("Player has " + str(len(player_hand)) + " cards left", end=" | ")
        if (debug): print("Computer has " + str(len(computer_hand)) + " cards left")

    # if (debug): print final results
    if len(player_hand) == 0:
        computer_wins += 1
        if (debug): print("Player has no cards left. Computer wins.")
    else:
        player_wins += 1
        if (debug): print("Computer has no cards left. Player wins.")
    amount_of_deals.append(deal_amount)

print(f"Player wins: {player_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Max amount of deals: {max(amount_of_deals)}")
print(f"Min amount of deals: {min(amount_of_deals)}")
print(f"Mean amount of deals: {sum(amount_of_deals) / len(amount_of_deals)}")


plt.figure()
plt.hist(amount_of_deals, bins=50)
plt.xlabel("Amount of deals")
plt.ylabel("Frequency")
plt.title("Amount of deals in " + str(iterations) + " games")
plt.savefig("amount_of_deals.png")
# plt.show()
