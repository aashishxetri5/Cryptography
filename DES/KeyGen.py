import random as r

PARITY_DROP = (57, 49, 41, 33, 25, 17,  9,  1,
               58, 50, 42, 34, 26, 18, 10,  2,
               59, 51, 43, 35, 27, 19, 11,  3,
               60, 52, 44, 36, 63, 55, 47, 39,
               31, 23, 15,  7, 62, 54, 46, 38,
               30, 22, 14,  6, 61, 53, 45, 37,
               29, 21, 13,  5, 28, 20, 12,  4)

COMPRESSION_PBOX = (14, 17, 11, 24,  1,  5,
                    3,  28, 15,  6, 21, 10,
                    23, 19, 12,  4, 26,  8,
                    16,  7, 27, 20, 13,  2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32)

def setInputBlock():
    input_block = ""
    for _ in range(64):
        input_block += str(r.randint(0,1))
    return input_block

def boxOperation(bits, box):
    text = ""
    for i in box:
        text += bits[i-1]
    return text

def shiftBits(lkey, rkey, shift):
    lkey = lkey[shift:] + lkey[:shift]
    rkey = rkey[shift:] + rkey[:shift]
    return lkey, rkey

def keyGenerator(input, PARITY_DROP, COMPRESSION_PBOX):
    # Reducing 64bit input bits to 56 bits by removing ciphers
    cipher_key = boxOperation(input, PARITY_DROP)
    
    # Breaking key into two halves
    left_28bits = cipher_key[:28]
    right_28bits = cipher_key[28:]
    round = 1 #Counts rounds

    oneBitShiftRounds = (1, 2, 9, 16) #These rounds have one bit shift
    while(round <= 16):
        if(round in oneBitShiftRounds):
            left_28bits, right_28bits = shiftBits(left_28bits, right_28bits, 1)
        else:
            left_28bits, right_28bits = shiftBits(left_28bits, right_28bits, 2)

        roundKey = left_28bits + right_28bits
        print("Round", round, "Key: ", boxOperation(roundKey, COMPRESSION_PBOX))
        round += 1

input = setInputBlock()
# input = "1100110100000000110011001111111111110001101010101111000010101010"
keyGenerator(input, PARITY_DROP, COMPRESSION_PBOX)