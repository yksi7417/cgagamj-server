# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mahjong

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Tile(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Tile()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTile(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Tile
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Tile
    def Suit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Tile
    def CardNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def TileStart(builder):
    builder.StartObject(2)

def Start(builder):
    TileStart(builder)

def TileAddSuit(builder, suit):
    builder.PrependUint8Slot(0, suit, 0)

def AddSuit(builder, suit):
    TileAddSuit(builder, suit)

def TileAddCardNumber(builder, cardNumber):
    builder.PrependUint8Slot(1, cardNumber, 0)

def AddCardNumber(builder, cardNumber):
    TileAddCardNumber(builder, cardNumber)

def TileEnd(builder):
    return builder.EndObject()

def End(builder):
    return TileEnd(builder)
