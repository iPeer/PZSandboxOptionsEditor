__all__ = ("ByteBuffer", )

from typing import Union


class ByteBuffer():
    def __init__(self, _bytes: Union[bytearray, bytes]):
        self._bytes = _bytes
        self._offset = 0
        self._mark = 0

    @property
    def getbytes(self) -> bytes:
        if isinstance(self._bytes, bytes):
            return bytes
        else:
            return bytes(self._bytes)

    @property
    def writable(self) -> bool:
        return isinstance(self._bytes, bytearray)

    @property
    def offset(self) -> int:
        return self._offset

    def skip(self, skipBytes: int = 1) -> None:
        if skipBytes > len(self._bytes):
            raise IndexError(f"Offset {skipBytes} is greater than size {len(self._bytes)}")
        self._offset += skipBytes

    def mark(self):
        self._mark = self._offset

    def reset(self):
        self._offset = self._mark

    def seek(self, offset: int) -> None:
        if offset > len(self._bytes):
            raise IndexError(f"Offset {offset} is greater than size {len(self._bytes)}")
        self._offset = offset

    # -- WRITING

    def put(self, data: getbytes) -> int:
        if not self.writable:
            raise PermissionError("ByteBuffer object is not writable")
        prev = len(self._bytes)
        #self._bytes.append(data)
        self._bytes.extend(data)
        return len(self._bytes) - prev

    def writePZString(self, string: str):
        _strLen = len(string.encode("utf-8"))
        _lenbytes = _strLen.to_bytes(2, byteorder="big")
        self.put(_lenbytes)
        self.put(string.encode("utf-8"))

    def putInt(self, value: int, byteorder="big"):
        self.put(value.to_bytes(4, byteorder=byteorder))

    # -- READING

    def get(self, count: int = 1, seek=True):
        r: bytes
        if self._offset + count > len(self._bytes):
            r = self._bytes[self._offset:]
        else:
            dist = self._offset + count
            r = self._bytes[self._offset:dist]
        if seek:
            self._offset += count
        return r

    def readPZString(self) -> str:
        _hex = self.get(2)
        _strLen = int(_hex.hex(), 16)
        _str: str = self.get(_strLen).decode("utf-8")

        return str(_str)

    def getInt(self, byteorder="big") -> int:
        return int.from_bytes(self.get(4), byteorder=byteorder)
        