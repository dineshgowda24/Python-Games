#This is a basic Black Jack Game
import random

ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Jack','Queen')
suits =('Hearts','Diamonds','Spades','Clubs' )
values = { 'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
           'King':10,'Queen':10, 'Jack':11,'Ace':11 }

playing = True

"""
Card Class holds 2 values suit and rank
"""
class Card():
	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit
	def __str__(self):
		return self.rank + " of " + self.suit

"""
Deck of 52 cards
Deck has functionality to shuffle cards
"""
class Deck():
	def __init__(self):
		self.deck = [] #Empty list of deck having card objects
		for rank in ranks:
			for suit in suits:
				self.deck.append(Card(rank,suit))

	def __str__(self):
		deck_str = ''
		for card in self.deck:
			deck_str+= '\n' + card.__str__()
		return 'The deck has: ' + deck_str

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

"""
Breif Implementation of Hand class
Hand class reprents either player or a dealer.
Hand has the ability to adjust of ace(1 or 11) just like a normal player.
"""
class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.num_aces = 0

	def __str__(self):
		hand = 'Hand has '
		for card in self.cards:
			hand += '\n' + card.__str__()
		hand += '\n' + 'Value : ' + str(self.value)
		return hand

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.num_aces += 1

	def adjust_for_ace(self):
		
		#If our total value goes above 21, we will adjust the ace to be 1. else we leave it to 11.
		while self.value > 21 and self.num_aces:
			self.value -= 10
			self.num_aces -= 1

class Chip():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):

	while True:
		try:
			chips.bet = int(input("Enter your bet amount : "))
		except TypeError:
			print("Invaild bet amount, please enter an integer")
		else:
			if chips.bet > chips.total:
				print("No balance. Current outstanding balance {}".format(chips.total))
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()


def hit_or_stand(deck,hand):
	global playing
	while True:
		i = input("Hit or Stand? Enter h or s. ")

		if i[0].lower() == 'h':
			hit(deck,hand)
			continue
		elif i[0].lower() == 's':
			print('Player Stands. Dealers Turn')
			playing = False
		else:
			print("Invaild input, enter h or s")
			continue
		break

def player_wins(player,dealer,chips):
	print("Player Wins!")
	chips.win_bet()

def player_busts(player,dealer,chips):
	print("Player Busted!")
	chips.lose_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer Wins!")
	chips.lose_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer Busted!")
	chips.win_bet()

def push(player,dealer):
	print("Player and Dealer tie. Push!")

#Initial Player all cards are shown and Dealer's one face up and one face down.
def show_some(player,dealer):

	print("Dealer Hand :")
	print("One Card Hidden")
	print(dealer.cards[1])
	print("\n")
	print("Player Hand : ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):

	print("Dealer Hand :")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("Player Hand : ")
	for card in player.cards:
		print(card)

while True:

	print("Welcome to BlackJack!")

	# Init Deck & Shuffle Deck
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#Init a chip object and take the bet from the player
	player_chips = Chip()
	take_bet(player_chips)

	show_some(player_hand,dealer_hand)
	
	#Take hit from player until he stands
	while playing:

		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)

		if player_hand.value > 21 :
			player_busts(player_hand,dealer_hand,player_chips)
			break

	#If player didn't bust then hit the dealer until he soft17 and then validate results
	if player_hand.value <= 21 :

		#Soft17 rule in BlackJack, where dealer hits only till 17
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	print("\n")
	print("Total Player chips are at : {}".format(player_chips.total))

	if input("Do you want to play again? y/n ")[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank you for playing.")
		break
