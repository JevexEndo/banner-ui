import random
import struct
from uuid import UUID


class MCUUID(UUID):
    rng = random.Random(x="Mapwreck 4")

    def __init__(self) -> None:
        super().__init__(int=self.rng.getrandbits(128), version=4)

    @property
    def nbt(self) -> str:
        return "[I;{},{},{},{}]".format(
            struct.unpack(">i", bytes.fromhex(self.hex[0:8]))[0],
            struct.unpack(">i", bytes.fromhex(self.hex[8:16]))[0],
            struct.unpack(">i", bytes.fromhex(self.hex[16:24]))[0],
            struct.unpack(">i", bytes.fromhex(self.hex[24:32]))[0],
        )
