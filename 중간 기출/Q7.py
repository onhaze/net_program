import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed


def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked


def getSrcPort(unpacked):
    return unpacked[0]

def getDstPort(unpacked):
    return unpacked[1]

def getLength(unpacked):
    return unpacked[2]

def getChecksum(unpacked):
    return unpacked[3]


if __name__ == "__main__":
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    
    packed_udphdr = udp.pack_Udphdr()
    print(binascii.hexlify(packed_udphdr).decode())
    
    unpacked_udphdr = unpack_Udphdr(packed_udphdr)
    print(unpacked_udphdr)

    print(f"Source Port: {getSrcPort(unpacked_udphdr)}, "
      f"Destination Port: {getDstPort(unpacked_udphdr)}, "
      f"Length: {getLength(unpacked_udphdr)}, "
      f"Checksum: {hex(getChecksum(unpacked_udphdr))}")
