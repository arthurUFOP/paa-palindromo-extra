import random
alphabet = "abcdefghijklmnopqrstuvwxyz"

def gen_random_str(size):
    return ''.join(random.choices(alphabet, k=size))

strings = []
for i in range(9):
    strings.append([gen_random_str(10 * (2**i)) for _ in range(20)])

with open("strings.txt", "w+") as f:
    f.write(str(strings))


