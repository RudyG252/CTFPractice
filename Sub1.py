from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

dict = {}
#picoctf
knownString = "qtlvLKO"
knownCypher = "Ove kwtb qevmsjr, kwj osgx tb: qtlvLKOhuzdfia".lower()
knownBase   = "for this problem, the flag is: picoCTFundwvkq".lower()
cipher = "ABlDEoGHtJKCMNvqpRSkUOWXYZ".lower()
base   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
cipherText = """LKOb (bwvek ove lgqkhej kwj osgx) gej g kyqj vo lvrqhkje bjlhetky lvrqjktktvu. Lvukjbkgukb gej qejbjukjz dtkw g bjk vo lwgssjuxjb dwtlw kjbk kwjte lejgktftky, kjlwutlgs (guz xvvxstux) bitssb, guz qevmsjr-bvsftux gmtstky. Lwgssjuxjb hbhgssy lvfje g uhrmje vo lgkjxvetjb, guz dwju bvsfjz, jglw ytjszb g bketux (lgssjz g osgx) dwtlw tb bhmrtkkjz kv gu vustuj blvetux bjeftlj. LKOb gej g xejgk dgy kv sjgeu g dtzj geegy vo lvrqhkje bjlhetky bitssb tu g bgoj, sjxgs juftevurjuk, guz gej wvbkjz guz qsgyjz my rguy bjlhetky xevhqb gevhuz kwj dvesz ove ohu guz qeglktlj. Ove kwtb qevmsjr, kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}""".lower()





def solveCipher(dict : Dict[str, str], cipherText : str) -> str:
    sol : str = ""
    for c in cipherText:
        if c not in dict:
            sol += c
            continue
        sol += dict[c]
    return sol

def createCipher(knownCipher : str, knownBase : str) -> Dict[str, str]:
    dict : Dict[str, str] = {}
    for i in range(len(knownCipher)):
        dict[knownCipher[i]] = knownBase[i]
    return dict

def checkLetters(currentBase : str):
    sol : str = ""
    for c in base:
        if c not in currentBase:
            sol += c
    return sol



dict : Dict[str, str] = createCipher(knownCypher, knownBase)
print(dict)
print(solveCipher(dict, cipherText))


