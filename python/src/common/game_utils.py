import flatbuffers 
from typing import List 

from mahjong import Suit, Wind, Player, Game
from common.tilemap import get_randomized_full_set
from common.PlayerState import PlayerState

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


def new_game(builder: flatbuffers.Builder, players: List[PlayerState]) -> Game:
    unused_tiles = get_randomized_full_set()

    unused_tiles_fb = None
    if (len(unused_tiles) > 0):
        Game.GameStartUnusedTilesVector(builder, len(unused_tiles))
        for tile in reversed(unused_tiles):
            builder.PrependByte(tile)
        unused_tiles_fb = builder.EndVector()

    players_fb = generate_player_vector(builder, players)

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
    print(f"Current Wind: {game.CurrentWind()} Turn: {game.CurrentTurn()} Round: {game.CurrentRound()}")
    for i in range(game.PlayersLength()):
        player = game.Players(i)
        print(f"Player ID: {player.Id()} Name: {player.Name()} Account Balance: {player.AccountBalance()} Seat: {player.Seat()}")
        print(f"  Hidden tiles: {[player.HiddenTiles(j) for j in range(player.HiddenTilesLength())]}")
        print(f"  Shown tiles: {[player.ShownTiles(j) for j in range(player.ShownTilesLength())]}")
    print(f"Discarded tiles: {game.DiscardedTilesAsNumpy()}")
    print(f"Unused tiles: {game.UnusedTilesAsNumpy()}")


