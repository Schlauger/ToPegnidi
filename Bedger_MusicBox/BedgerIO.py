import struct

def Append2bin_file(filename = "boltClock.schl", text = "note", number = 1000):
    # Open and append to binary file
    with open(filename, 'ab') as f:
        # From text to bytes
        txt_bytes = text.encode('utf-8')
        # Write the length of the text as a 4-byte integer followed by the text itself
        f.write(struct.pack('I', len(txt_bytes)))
        f.write(txt_bytes)
        # Write the number as a 8-byte
        f.write(struct.pack('d', number)) # 'd' for double

def Read_bin_file(filename = "boltClock.schl"):
    data = []
    # Open the binary file
    with open(filename, 'rb') as f:
        # Read until EOF
        while True:
            # Read the length of the text as a 4-byte integer
            txt_len_bytes = f.read(4)
            if not txt_len_bytes: # No ore bytes
                break
            txt_len = struct.unpack('I', txt_len_bytes)[0]
            # Read the text based on its length
            text = f.read(txt_len).decode('utf-8')
            # Read the number as a 8-byte float
            number = struct.unpack('d', f.read(8))[0]
            data.append((text, number))
    return data

if __name__ == "__main__":
    fl = "notes.schl"
    Append2bin_file(fl, "Bedger", 6595)
    data=Read_bin_file(fl)
    print(data)