import binascii

filename = 'Smallest+Map+Ever2.scm'
MQPHeaderinfo = []
MQPHeader = []

with open(filename, 'rb') as f:
    content = f.read()
binin = binascii.hexlify(content)

MQPHeaderinfo = binin[0:16]
HeaderSize = MQPHeaderinfo[8:16]

print("Header length : ", MQPHeaderinfo[8:16])

inputsize = input("input yout format size : ")

MQPheader = binin[16:int(inputsize)*4]
print("---------------------------------------")
print("\ MQP HEADER        : ",MQPHeaderinfo[0:8])
print("\ Header length     : ", MQPHeaderinfo[8:16])
print("\ File length       : ", MQPheader[0:8])
print("\ MPQ version       : ", MQPheader[8:12])
print("\ sector Size Shift : ", MQPheader[12:16])
print("\ HET offset        : ", MQPheader[16:24])
print("\ BET offset        : ", MQPheader[24:32])
print("\ HET number        : ", MQPheader[32:40])
print("\ BET number        : ", MQPheader[40:48])
print("---------------------------------------")
