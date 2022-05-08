print("hello world")

max = (2**20) - 1

# including the corners
maskA = 0xFC000
maskB = 0x07E00
maskC = 0x003F0
maskD = 0x8001F

# excluding the corners

print("{0:020b}\n".format(maskA))
print("{0:020b}\n".format(maskB))
print("{0:020b}\n".format(maskC))
print("{0:020b}\n".format(maskD))

valid = []

# for x in range(max):
#     if x & maskA == 0: continue
#     if x & maskA == maskA: continue

#     if x & maskB == 0: continue
#     if x & maskB == maskB: continue


#     if x & maskC == 0: continue
#     if x & maskC == maskC: continue

#     if x & maskD == 0: continue
#     if x & maskD == maskD: continue
#     # print("{0:020b}".format(x))
#     valid.append(x)

tile=0b11000100111101111111

BLOCK=chr(9608)
SPACE=" "

print("{0:020b} \n".format(tile))

print("{0:b}".format(tile>>14))
left=SPACE if tile&0x1 == 0 else BLOCK
right=SPACE if tile&0x2000 == 0 else BLOCK
print("{}xxxx{}".format(left,right))

left=SPACE if tile&0x2 == 0 else BLOCK
right=SPACE if tile&0x1000 == 0 else BLOCK
print("{}xxxx{}".format(left,right))

left=SPACE if tile&0x4 == 0 else BLOCK
right=SPACE if tile&0x800 == 0 else BLOCK
print("{}xxxx{}".format(left,right))

left=SPACE if tile&0x8 == 0 else BLOCK
right=SPACE if tile&0x400 == 0 else BLOCK
print("{}xxxx{}".format(left,right))

print("{0:b}".format((tile&maskC)>>4)[::-1])
