# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mahjong

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Game(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Game()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGame(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Game
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Game
    def Players(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from mahjong.Player import Player
            obj = Player()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Game
    def PlayersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Game
    def PlayersIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Game
    def DiscardedTiles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Game
    def DiscardedTilesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Game
    def DiscardedTilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Game
    def DiscardedTilesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Game
    def CurrentWind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Game
    def CurrentTurn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Game
    def CurrentRound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def GameStart(builder):
    builder.StartObject(5)

def Start(builder):
    GameStart(builder)

def GameAddPlayers(builder, players):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(players), 0)

def AddPlayers(builder, players):
    GameAddPlayers(builder, players)

def GameStartPlayersVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPlayersVector(builder, numElems: int) -> int:
    return GameStartPlayersVector(builder, numElems)

def GameAddDiscardedTiles(builder, discardedTiles):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(discardedTiles), 0)

def AddDiscardedTiles(builder, discardedTiles):
    GameAddDiscardedTiles(builder, discardedTiles)

def GameStartDiscardedTilesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartDiscardedTilesVector(builder, numElems: int) -> int:
    return GameStartDiscardedTilesVector(builder, numElems)

def GameAddCurrentWind(builder, currentWind):
    builder.PrependUint8Slot(2, currentWind, 0)

def AddCurrentWind(builder, currentWind):
    GameAddCurrentWind(builder, currentWind)

def GameAddCurrentTurn(builder, currentTurn):
    builder.PrependUint8Slot(3, currentTurn, 0)

def AddCurrentTurn(builder, currentTurn):
    GameAddCurrentTurn(builder, currentTurn)

def GameAddCurrentRound(builder, currentRound):
    builder.PrependInt16Slot(4, currentRound, 0)

def AddCurrentRound(builder, currentRound):
    GameAddCurrentRound(builder, currentRound)

def GameEnd(builder):
    return builder.EndObject()

def End(builder):
    return GameEnd(builder)
