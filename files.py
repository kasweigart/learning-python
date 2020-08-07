# Files

f = open('data.txt', 'w') # Make a new file in output mode ('w' is write)
f.write('Hello\n') # Write strings of characters to it
f.write('World\n')
f.close() # Close to flush out buffers to disk

f = open('data.txt') # 'r' (read) is the default processing mode
text = f.read() # Read entire file into a string
print(text) # print interprets control characters
print(text.split()) # File content is always a string

for line in open('data.txt'): print(line)

print(dir(f))

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8) # Create packed binary data
print(packed) # 10 bytes, not objects or text

file = open('data.bin', 'wb') # Open binary output file
file.write(packed) # Write packed binary data
file.close()

data = open('data.bin', 'rb').read() # Open/read binary data file
print(data) # 10 bytes, unaltered

print(data[4:8]) # Slice bytes in the middle
print(list(data)) # Sequence of 8-bit bytes

print(struct.unpack('>i4sh', data)) # Unpack into objects again

S = 'sp\xc4m' # Non-ASII Unicode text
print(S)
print(S[2]) # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf=8') # Write/encode UTF-8 text
file.write(S) # 4 characters written
file.close()

text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text)) # 4 chars (code points)

raw = open('unidata.txt', 'rb').read() # Read raw encoded bytes
print(raw)
print(len(raw)) # Really 5 bytes in UTF-8

print(text.encode('utf-8')) # Manual encode to bytes
print(raw.decode('utf-8')) # Manual decode to bytes

print(text.encode('latin-1')) # Bytes differ in others
print(text.encode('utf-16'))

print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16')) # But same string decoded

