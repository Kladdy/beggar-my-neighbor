from multiprocessing import freeze_support
import random
import concurrent.futures

limit = 27

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

# Define a function to play the game
def play_game():
    iterations = 0
    print("Starting iteration 0...")
    while True:

        iterations += 1
        if (iterations % 1000 == 0):
            print(f"Playing iteration {iterations}...")

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

        # Play the game
        while len(player_hand) > 0 and len(computer_hand) > 0:

            deal_amount += 1
            if (deal_amount > limit + 1): 
                break

            # Player plays a card
            player_card = player_hand.pop(0)
            computer_pile.append(player_card)

            # Computer plays a card
            computer_card = computer_hand.pop(0)
            player_pile.append(computer_card)

            # Compare the cards played
            if cards[player_card] > cards[computer_card]:
                # Player captures the pile
                player_pile += computer_pile
                player_hand += player_pile
                computer_pile = []
                player_pile = []
            elif cards[player_card] < cards[computer_card]:
                # Computer captures the pile
                computer_pile += player_pile
                computer_hand += computer_pile
                computer_pile = []
                player_pile = []

        if (deal_amount < limit):
            print(f"We found one under {limit} deals in {iterations} iterations")
            return iterations
        # else:
        #     return None



if __name__ == '__main__':
    # freeze_support()

    # Use a concurrent.futures.ProcessPoolExecutor to run the function on multiple cores
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(30):
            result = executor.submit(play_game).result()
            if result:
                print(f"We found one under {limit} deals in {result} iterations")
                break