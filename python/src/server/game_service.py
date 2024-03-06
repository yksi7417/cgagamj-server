from typing import List
import flatbuffers

from common.mahjong import Suit, Wind, Player, Game
from common.game_utils import new_game, encode_game

class GameStateNotificationService:
    def __init__(self):
        pass

    def new_game_notify_players(self, players: List[Player]):
        builder = flatbuffers.Builder(1024)
        self.current_game = new_game(builder, players)
        self.notify_players(players)
        
    def notify_players(self):
        payload = encode_game(builder)



## abstract the flatbuffer away from GameService.  
class GameService:
    def __init__(self, gsns: GameStateNotificationService):
        self.gsns = gsns
        pass

    def start_game(self, players: List[Player]):
        self.gsns.new_game_notify_players(players)
        pass

    def end_game(self, game: Game):
        # Ends the current game
        pass

    def draw_tile(self, game: Game):
        # Draws a tile for the current player
        # Takes the ID of the player as input
        pass

    def discard_tile(self, game: Game, tile: Tile):
        # Discards a tile from the current player
        pass

    def claim_win(self, game: Game, tiles: List[Tile]):
        # Claims a win for the current player
        pass

    def verify_win(self, game: Game, tiles: List[Tile]):
        # Verifies a win claim and calculates the number of "Faan"
        pass
