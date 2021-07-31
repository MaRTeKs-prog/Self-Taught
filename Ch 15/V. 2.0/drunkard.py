from card import Card
from deck import Deck
from player import Player

class Game:
	def __init__(self):
		name1 = input("Имя игрока 1: ")
		name2 = input("Имя игрока 2: ")
		self.deck = Deck()
		self.player1 = Player(name1)
		self.player2 = Player(name2)

	def play_game(self):
		cards = self.deck.cards
		print("Поехали!")
		response = None
		while len(cards) >= 2:
			response = input('Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры.')
			if response == 'Х':
				break
			player1_card = self.deck.remove_card()
			player2_card = self.deck.remove_card()
			print("{} кладет {}, а {} кладет {}.".format(self.player1.name, player1_card, self.player2.name, player2_card))
			if player1_card > player2_card:
				self.player1.wins += 1
				print("{} забирает карты".format(self.player1.name))
			else:
				self.player2.wins += 1
				print("{} забирает карты".format(self.player2.name))
		print("Игра окончена. {} выиграл!".format(self.winner(self.player1, self.player2)))

	def winner(self, player1, player2):
		if player1.wins > player2.wins:
			return player1.name
		if player1.wins < player2.wins:
			return player2.name
		return "Ничья!"

game = Game()
game.play_game()
