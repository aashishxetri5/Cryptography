import random as r

init_perm = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

final_perm = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25]


def setInputBlock():
    input_block = ""
    for _ in range(64):
        input_block += str(r.randint(0,1))
    return input_block

def permute(input_block, permutation_tbl):
    converted = ""
    for i in permutation_tbl:
        converted += input_block[i-1]
    return converted

def converter(text):
    from_ = 0
    for i in range(1, 17):
        print(str(hex(int(text[from_:i*4], 2))).replace('0x',''), end="")
        from_ = i*4
        if (i)%4 == 0: print(end=" ")
    print()



input_block = setInputBlock()  # generating input block
# input_block = "0000000000000010000000000000000000000000000000000000000000000001"
print("Input: " + input_block)
print("\nInput Block:", end=" ")
converter(input_block)

converted = permute(input_block, init_perm)
print("\ninit perm:", end=" ")
converter(converted)
print("From init permutation box: " + converted)

converted_f = permute(converted, final_perm)
print("\nFinal perm:", end=" ")
converter(converted_f)
print("From final permutation box: " + converted_f)