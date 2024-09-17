import random
import uuid

class Game:
    def __init__(self, players):
        self.players = players 

    def play_match(self, player1, player2):
        # player1, player2의 win_lose_history를 update하고 
        # elo rating 알고리즘에 따라 각자의 current_rating을 update할 것 
        # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 참고 
        k = 30
        
        rand_value = random.random()
        factor = (player2.actual_rating - player1.actual_rating) / 400
        we1 = 1 / (1 + 10 ** factor)
        we2 = 1 / (1 + 10 ** -factor)
        
        if rand_value < we1 : # player 1 wins
            w1 = 1
            w2 = 0
            player1.win_lose_history.append((player2, 'win'))
            player2.win_lose_history.append((player1, 'lose'))

        elif rand_value < 1 : # player 2 wins
            w1 = 0
            w2 = 1
            player1.win_lose_history.append((player2, 'lose'))
            player2.win_lose_history.append((player1, 'win'))

        factor = (player2.current_rating - player1.current_rating) / 400
        we1 = 1 / (1 + 10 ** factor)
        we2 = 1 / (1 + 10 ** -factor)

        player1.current_rating = player1.current_rating + k * (w1 - we1)
        player2.current_rating = player2.current_rating + k * (w2 - we2)
        # print(player1, player2)
    
    def match_players(self):
        self.players.sort(key = lambda player: player.current_rating, reverse=True)

        matches = []
        
        for i in range(0, len(self.players), 2):
            if i + 1 < len(self.players) :
                matches.append((self.players[i], self.players[i+1]))
        return matches
        
    def simulate(self):
        player_id_to_watch = self.players[0].player_id
        
        for i in range(1000):
            matches = self.match_players()
            for player1, player2 in matches:
                self.play_match(player1, player2)
                if player1.player_id == player_id_to_watch:
                    print(player1)
                elif player2.player_id == player_id_to_watch:
                    print(player2)
        
        

class Player:
    def __init__(self, player_id, initial_rating=1000, actual_rating=1000):
        self.player_id = player_id
        self.win_lose_history = []
        self.current_rating = initial_rating
        self.actual_rating = actual_rating
        
        
    def __str__(self):
        return f'{str(self.player_id)[:5]}: current rating - {self.current_rating}, actual rating - {self.actual_rating}'

def generate_player_data():
    player_id = str(uuid.uuid4())
    # actual_rating = random.randint(500, 2000)
    actual_rating = max(random.gauss(1000, 500), 500)
    return player_id, actual_rating

if __name__ == '__main__':
    player_list = []

    for i in range(100):
        player_id, actual_rating = generate_player_data()
        player = Player(player_id, actual_rating=actual_rating)
        # Player.__init__(player, player_id, actual_rating=actual_rating)
        player_list.append(player)
    

    g = Game(players = player_list)

    g.simulate()
    
