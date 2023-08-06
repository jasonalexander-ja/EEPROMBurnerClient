with open("/Users/jasonalex/dev/EEPROMBurnerClient/datadump.bin", "rb") as f:
    index = 0
    while (byte := f.read(1)):
        if byte != (0x12).to_bytes():
            print(f"Error at {index}: {byte}")
        index += 1
