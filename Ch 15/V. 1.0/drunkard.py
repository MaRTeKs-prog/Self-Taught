from card import Card
from deck import Deck
from player import Player

class Game:
	def __init__(self):
		name1 = input('Имя игрока 1: ')
		name2 = input('Имя игрока 2: ')
		self.deck = Deck()
		self.p1 = Player(name1)
		self.p2 = Player(name2)

	def wins(self, winner):
		w = '{} забирает карты'
		w = w.format(winner)
		print(w)

	def draw(self, p1n, p1c, p2n, p2c):
		d = '{} кладёт {}, а {} кладёт {}'
		d = d.format(p1n, p1c, p2n, p2c)
		print(d)

	def play_game(self):
		cards = self.deck.cards
		print('Поехали!')
		while len(cards) >= 2:
			m = 'Нажмите X для выхода. Нажмите любую другую клавишу для начала игры.'
			response = input(m)
			if response == 'X' or 'Х':
				break
			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name
			self.draw(p1n, p1c, p2n, p2c)
			if p1c > p2c:
				self.p1.wins += 1
				self.wins(self.p1.name)
			else:
				self.p2.wins += 1
				self.wins(self.p2.name)
		win = self.winner(self.p1, self.p2)
		print('Игра окончена. {} выиграл!'.format(win))

	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name
		if p1.wins < p2.wins:
			return p2.name
		return 'Ничья!'

game = Game()
game.play_game()

"""
Код из книги хуйня полная!
Он даже не работает как надо!
Пиздец... Там сверху в def play_game не указаны ебаные действия,
которые игра делает после каждого раунда!
Т. е. я так думаю, что игра просто сама в себя играет и
ничего не выписывает. Но в конце появляется то,
что игра и выиграна, и сыграна в ничью.
Мда...
"""