import random

Suits=('Diamond','Club','Spades','Heart')
Ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing=True

class Card():
	"""docstring for ClassName"""		
	def __init__(self,suits,ranks):
		self.suits=suits
		self.ranks=ranks
	def __str__(self):
		return f"{self.ranks} of {self.suits}"

class Deck():
	"""docstring for Classname"""
	def __init__(self):
		self.deck=[]
		for suits in Suits:
			for ranks in Ranks:
				self.deck.append(Card(suits,ranks))
	def __str__(self):
		deck_comp = ''  # start with an empty string
		for card in self.deck:
		 deck_comp += '\n '+card.__str__() # add each Card object's print string
		return 'The deck has:' + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)
	def deal(self):
		return self.deck.pop()

class Hand():
	"""docstring for Classname"""
	def __init__(self):
		self.cards=[]
		self.value=0
		self.aces=0
	def add_card(self,card):
		self.cards.append(card)      #from deck.deal()
		self.value+=values[card.ranks]
		#to keep track of no. of aces
		if card.ranks=='Ace':
			self.aces+=1
	def ace_adjust(self):
		# loop will keep running if the value is >21 and no. osf aces is >0
		while self.value>21 and self.aces:
			self.value-=10
			self.aces-=1

class Chips():
	"""docstring for Classname"""
	def __init__(self,total):
		self.total=total
		self.bet=0
	def win_bet(self):
		self.total+=self.bet
	def lose_bet(self):
		self.total=self.total-self.bet

def take_bet(Chips):

	while True:
		try:
			Chips.bet=int(input('Enter number of chips you want to bet: '))
		except:
			print('Sorry!!Enter an integer value ')
		else:
			if Chips.bet>Chips.total:
				print(f'You dont have enough chips!! You have {Chips.total} chips')
			else:
				break


def hit(Hand,Deck):
	single_card=deck.deal()
	Hand.add_card(single_card)
	Hand.ace_adjust()

def hit_stand(deck,player_hand):
	global playing	
	while True:
		x=input('>>>>>>Hit or Stand? Enter h or s:  ')
		if x[0]=='h':
			hit(player_hand,deck)
		elif x[0]=='s':
			print(">>>>>Player stands dealer's turn")	
			playing=False
		else:
			print("Sorry enter the correct input ")
			continue
		break

def show_some(player_hand,dealer_hand):
	print("Dealer's Hand")
	print('<card hidden>')
	print('',dealer_hand.cards[1])
	print("\nPlayers's Hand: ",*player_hand.cards,sep='\n')

def show_all(player_hand,dealer_hand):
	print('\n')
	print("Dealer's Hand: ",*dealer_hand.cards,sep='\n')
	print('\n')
	print("Dealer's Value:= ",dealer_hand.value)
	print('\n')
	print("Player's Hand: ",*player_hand.cards,sep='\n')
	print('\n')
	print("Player's Value:=",player_hand.value)
	print('\n')

def player_busts(player_hand,dealer_hand,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player_hand,dealer_hand,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player_hand,dealer_hand,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player_hand,dealer_hand,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player_hand,dealer_hand):
    print("Dealer and Player tie! It's a push.")

while True:
	print('Welcome to Blackjack!! Get as close to 21 as you can without going over!!'+'\nDealer hits unit he reaches 17.Aces count as 1 or 11')

	deck=Deck()   #A deck of 52 cards is created
	deck.shuffle() # deck is shuffled

    # Player cards are recorded, 2 cards are given in the start
	player_hand=Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

    # Dealer's cards are recorded
	dealer_hand=Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	total=int(input('enter number of chips you have: '))
	player_chips=Chips(total)

	take_bet(player_chips)

	show_some(player_hand,dealer_hand)

	while playing:

		hit_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		if player_hand.value>21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	if player_hand.value<=21:
		while dealer_hand.value<17:
			hit(dealer_hand,deck)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value>21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value>player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value<player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	print("Player's winnings stand at: ",player_chips.total)    


	new_game=input("Would you like to play again? y or n: ")

	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thank you for playing")
		break





		







