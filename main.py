from typing import Optional, Any
import sys

class Serial:

    def __init__(self, data, baudrate) -> None:
        pass

    def write(self, data: bytes):
        print(data)



def main():
    if len(sys.argv) < 3:
        print("Please specify a file and a port. ")
        return
    _, com_port, path = sys.argv

    file = open_file(path) 
    if file == None:
        return
    
    write_to_port(file, com_port)


def write_to_port(data: bytes, com_port: str):
    s = None
    try:
        s = Serial(com_port, baudrate=115200)
    except:
        print(f"Failed to open COM port {com_port}")

    for pos, byte in enumerate(data):
        write_byte(pos, byte, s)


def write_byte(addr: int, byte: int, port: Serial):
    lower_addr = format(addr & 0xFF, '03d')
    upper_addr = format((addr >> 8) & 0b111, '03d')
    data = format(byte, '03d')

    port.write(f"L{lower_addr}".encode())
    port.write(f"U{upper_addr}".encode())
    port.write(f"D{data}".encode())


def open_file(path: str) -> Optional[bytes]:
    try:
        
        return open(path, "rb").read()
    except:
        print(f"Failed to find file: {path}")
        return None

if __name__ == "__main__":
    main()
