import flatbuffers 
from typing import List 

from mahjong import Suit, Wind, Player, Game
from common.tilemap import get_randomized_full_set

class PlayerState:
    def __init__(self, id, name, hidden_tiles, shown_tiles, account_balance, seat):
        self.id = id
        self.name = name
        self.hidden_tiles = hidden_tiles
        self.shown_tiles = shown_tiles
        self.account_balance = account_balance
        self.seat = seat

# Sample data for 4 players
temp_players = [
    PlayerState(1, "Alice", [1, 2, 3], [4, 5], 1000, 0),
    PlayerState(2, "Bob", [6, 7, 8], [9, 10], 2000, 1),
    PlayerState(3, "Charlie", [11, 12, 13], [14, 15], 3000, 2),
    PlayerState(4, "Dave", [16, 17, 18], [19, 20], 4000, 3),
]


def generate_player_vector(builder: flatbuffers.Builder, players: List[PlayerState]):
    players_fb = None
    if (len(players) > 0):
        player_offsets = []
        for player in players:

            Player.PlayerStartHiddenTilesVector(builder, len(player.hidden_tiles))
            for tile in reversed(player.hidden_tiles):
                builder.PrependByte(tile)
            hidden_tiles_fb = builder.EndVector()

            Player.PlayerStartShownTilesVector(builder, len(player.shown_tiles))
            for tile in reversed(player.shown_tiles):
                builder.PrependByte(tile)
            shown_tiles_fb = builder.EndVector()

            # Create the player object and get its offset
            player_name_offset = builder.CreateString(player.name)
            Player.PlayerStart(builder)
            Player.PlayerAddId(builder, player.id)
            Player.PlayerAddName(builder, player_name_offset)

            Player.PlayerAddHiddenTiles(builder, hidden_tiles_fb)
            Player.PlayerAddShownTiles(builder, shown_tiles_fb)

            Player.PlayerAddAccountBalance(builder, player.account_balance)
            Player.PlayerAddSeat(builder, player.seat)
            player_offset = Player.PlayerEnd(builder)
            
            # Add the offset to the list
            player_offsets.append(player_offset)

        # Create the vector of players
        Game.GameStartPlayersVector(builder, len(player_offsets))
        for player_offset in reversed(player_offsets):
            builder.PrependUOffsetTRelative(player_offset)
        players_fb = builder.EndVector()

    return players_fb


def new_game(builder: flatbuffers.Builder, players: List[Player]) -> Game:
    unused_tiles = get_randomized_full_set()

    unused_tiles_fb = None
    if (len(unused_tiles) > 0):
        Game.GameStartUnusedTilesVector(builder, len(unused_tiles))
        for tile in reversed(unused_tiles):
            builder.PrependByte(tile)
        unused_tiles_fb = builder.EndVector()

    players_fb = generate_player_vector(builder, temp_players)

    Game.Start(builder)
    Game.AddCurrentRound(builder, 1)
    Game.AddCurrentTurn(builder, 0)
    Game.AddCurrentWind(builder, 0)

    if unused_tiles_fb:
        Game.AddUnusedTiles(builder, unused_tiles_fb)

    if players_fb:
        Game.AddPlayers(builder, players_fb) 

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
        for j in range(player.HiddenTilesLength()):
            print(f"  Hidden tiles: {player.HiddenTiles(j)}")
        for j in range(player.ShownTilesLength()):
            print(f"  Shown tiles: {player.ShownTiles(j)}")
        print(f"  Account balance: {player.AccountBalance()}")
        print(f"  Seat: {player.Seat()}")

    print(f"Discarded tiles: {game.DiscardedTilesAsNumpy()}")
    print(f"Unused tiles: {game.UnusedTilesAsNumpy()}")


