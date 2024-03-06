from typing import List 
import flatbuffers 

from common.mahjong import Suit, Wind, Player, Tile, Game
from common.tilemap import get_randomized_full_set

# class GameBuilder:
#     def __init__(self, builder: flatbuffers.Builder):
#         self.builder = builder 
#         Game.Start(self.builder)
#         pass

#     def AddUnusedTiles(self, tiles: List[Tile]) -> 'GameBuilder': 
#         return self

#     def AddDiscardedTiles(self, tiles: List[Tile]) -> 'GameBuilder': 
#         if len(tiles) > 0:
#             Game.GameStartDiscardedTilesVector(self.builder, len(tiles))
#             for tile in reversed(tiles):
#                 self.builder.PrependByte(tile)
#             tiles_fb = self.builder.EndVector()
#             Game.AddUnusedTiles(self.builder, tiles_fb)
#         return self

#     def AddPlayers(self, players: List[Player]) -> 'GameBuilder': 
#         return self


def new_game(builder: flatbuffers.Builder, players: List[Player]) -> Game:
    tiles = get_randomized_full_set()
    if len(tiles) > 0:
        Game.GameStartUnusedTilesVector(builder, len(tiles))
        for tile in reversed(tiles):
            builder.PrependByte(tile)
        tiles_fb = builder.EndVector()
        Game.AddUnusedTiles(builder, tiles_fb)

    # gb.AddPlayers(players)
    Game.AddCurrentRound(builder, 1)
    Game.AddCurrentTurn(builder, 0)
    Game.AddCurrentWind(builder, 0)
    my_new_game = Game.End(builder)
    builder.Finish(my_new_game)


def decode_game(payload: bytes) -> Game:
    game = Game.Game.GetRootAsGame(payload, 0)
    return game

def encode_game(game: Game) -> bytes:

    return bytes(builder.Output())

def encode_game(builder: flatbuffers.Builder) -> bytes:
    return bytes(builder.Output())

def print_game(game: Game):

    print(f"Current wind: {game.CurrentWind()}")
    print(f"Current turn: {game.CurrentTurn()}")
    print(f"Current round: {game.CurrentRound()}")

    for i in range(game.PlayersLength()):
        player = game.Players(i)
        print(f"Player {i}:")
        print(f"  ID: {player.Id()}")
        print(f"  Name: {player.Name()}")
        print(f"  Hidden tiles: {player.HiddenTiles()}")
        print(f"  Shown tiles: {player.ShownTiles()}")
        print(f"  Account balance: {player.AccountBalance()}")
        print(f"  Seat: {player.Seat()}")

    print(f"Discarded tiles: {game.DiscardedTilesAsNumpy()}")
    print(f"Unused tiles: {game.UnusedTilesAsNumpy()}")


