import random as r

s_box1 = [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
          [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
          [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
          [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

def setInputBlock():
    input_block = ""
    for _ in range(6):
        input_block += str(r.randint(0,1))
    return input_block

'''
The function below accepts text and sbox. Then, it converts the text to 4 bits from 6 bits.
'''

# def SBox(inp, sbox):
#     from_ = 0
#     nextEncr = ""
#     for i in range(1, 9):
#         text = inp[from_:6*i]
    
#         row = (int(inp[0] + inp[-1], 2))
#         col = (int(inp[1:-1], 2))

#         temp = format(s_box1[row][col], '04b')
#         print(temp)

#         nextEncr += temp
#         from_ = 6*i
    
#     return nextEncr

def SBox(inp):
    row = (int(inp[0] + inp[-1], 2))
    col = (int(inp[1:-1], 2))
    encr = s_box1[row][col]
    
    return encr

input_bits = setInputBlock()
output = SBox(input_bits)

print("Input Bit:", input_bits)
print("Output:", format(output, '04b'))
