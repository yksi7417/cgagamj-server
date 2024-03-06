import flatbuffers 
from typing import List 

from common.mahjong import Suit, Wind, Player, Game
from common.tilemap import get_randomized_full_set


def new_game(builder: flatbuffers.Builder, players: List[Player]) -> Game:
    unused_tiles = get_randomized_full_set()
    Game.GameStartUnusedTilesVector(builder, len(unused_tiles))

    for tile in reversed(unused_tiles):
        builder.PrependByte(tile)

    unused_tiles_fb = builder.EndVector()

    Game.Start(builder)
    Game.AddCurrentRound(builder, 1)
    Game.AddCurrentTurn(builder, 0)
    Game.AddCurrentWind(builder, 0)
    Game.AddUnusedTiles(builder, unused_tiles_fb)
    game = Game.End(builder)
    builder.Finish(game)
    return game


def decode_game(payload: bytes) -> Game:
    game = Game.Game.GetRootAsGame(payload, 0)
    return game

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


