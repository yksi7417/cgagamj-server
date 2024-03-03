from common.mahjong import Suit, Wind, Player, Game
import flatbuffers 

def new_game(builder: flatbuffers.Builder) -> Game:
    discarded_tiles = [143, 0, 122]
    Game.GameStartDiscardedTilesVector(builder, len(discarded_tiles))

    for tile in reversed(discarded_tiles):
        builder.PrependByte(tile)

    discarded_tiles_fb = builder.EndVector()

    Game.Start(builder)
    Game.AddCurrentRound(builder, 1)
    Game.AddCurrentTurn(builder, 0)
    Game.AddCurrentWind(builder, 0)
    Game.AddDiscardedTiles(builder, discarded_tiles_fb)
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


