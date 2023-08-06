from typing import Optional, Generator
from io import BufferedWriter
import sys

from serial import Serial


def main():
    if len(sys.argv) < 3:
        print("Please specify a filename and a port. ")
        return
    _, com_port, path = sys.argv

    file = open(path, "wb")
    if file == None:
        return
    
    port = None
    try:
        port = Serial(com_port, baudrate=115200)
    except:
        print(f"Failed to open COM port {com_port}")

    data = [item for item in read_eeprom_data(port)]
    file.write(bytearray(data))


def read_eeprom_data(port: Serial) -> Generator[int, None, None]:
    for addr in range(0x7FFF):
        print(addr)
        lower_addr = format(addr & 0xFF, '03d')
        upper_addr = format((addr >> 8) & 0x7F, '03d')

        serial_write_await(port, f"L{lower_addr}")
        serial_write_await(port, f"U{upper_addr}")

        data = serial_write_await(port, "R")[1:]
        yield parse_device_response(data)


def parse_device_response(data: str) -> int:
    try:
        data_i = int(data)
        if data_i > 255: raise
        return data_i
    except:
        raise Exception().add_note("Couldn't parse value from device. ")


def serial_write_await(s: Serial, data: str) -> str:
    s.write(data.encode())
    return s.readline().decode("utf-8")


main()
