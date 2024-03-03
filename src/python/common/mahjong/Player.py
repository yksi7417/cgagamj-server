# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mahjong

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Player(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Player()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPlayer(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Player
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Player
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Player
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Player
    def HiddenTiles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from mahjong.Tile import Tile
            obj = Tile()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Player
    def HiddenTilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Player
    def HiddenTilesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Player
    def ShownTiles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from mahjong.Tile import Tile
            obj = Tile()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Player
    def ShownTilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Player
    def ShownTilesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Player
    def IsBanker(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Player
    def AccountBalance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Player
    def Seat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def PlayerStart(builder):
    builder.StartObject(7)

def Start(builder):
    PlayerStart(builder)

def PlayerAddId(builder, id):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder, id):
    PlayerAddId(builder, id)

def PlayerAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    PlayerAddName(builder, name)

def PlayerAddHiddenTiles(builder, hiddenTiles):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(hiddenTiles), 0)

def AddHiddenTiles(builder, hiddenTiles):
    PlayerAddHiddenTiles(builder, hiddenTiles)

def PlayerStartHiddenTilesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartHiddenTilesVector(builder, numElems: int) -> int:
    return PlayerStartHiddenTilesVector(builder, numElems)

def PlayerAddShownTiles(builder, shownTiles):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(shownTiles), 0)

def AddShownTiles(builder, shownTiles):
    PlayerAddShownTiles(builder, shownTiles)

def PlayerStartShownTilesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartShownTilesVector(builder, numElems: int) -> int:
    return PlayerStartShownTilesVector(builder, numElems)

def PlayerAddIsBanker(builder, isBanker):
    builder.PrependBoolSlot(4, isBanker, 0)

def AddIsBanker(builder, isBanker):
    PlayerAddIsBanker(builder, isBanker)

def PlayerAddAccountBalance(builder, accountBalance):
    builder.PrependInt16Slot(5, accountBalance, 0)

def AddAccountBalance(builder, accountBalance):
    PlayerAddAccountBalance(builder, accountBalance)

def PlayerAddSeat(builder, seat):
    builder.PrependInt8Slot(6, seat, 0)

def AddSeat(builder, seat):
    PlayerAddSeat(builder, seat)

def PlayerEnd(builder):
    return builder.EndObject()

def End(builder):
    return PlayerEnd(builder)