from itertools import permutations
from string import ascii_lowercase
from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def rh(n):
    x, z = "a", permutations(ascii_lowercase[:n])
    for y in list(z):
        if x != y[0]: print("\n")
        x = y[0]
        print("".join(y) + " ")
rh(int(input()))
