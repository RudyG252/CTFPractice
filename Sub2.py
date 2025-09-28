from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

dict = {}
#picoctf
knownString = "qtlvLKO"
#ae
#ws
knownCypher = "pxzqZNVfagselwyhkubtprciom".lower()
knownBase   = "picoCTFehmpsnurybvdalgkqxw".lower()
cipher = "ABlDEoGHtJKCMNvqpRSkUOWXYZ".lower()
base   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
cipherText = """nafyffoxenefufytpqnafymfppfentkpxeafbaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlexlzpwbxlrzhkfystnyxqntlbwezhkfyzatppflrfnafefzqgsfnxnxqlevqzwesyxgtyxphqlehenfgetbgxlxenytnxqlvwlbtgflntpemaxzatyfufyhwefvwptlbgtycfntkpfecxppeaqmfufymfkfpxfufnafsyqsfyswysqefqvtaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlxelqnqlphnqnftzautpwtkpfecxppekwntpeqnqrfnenwbflnexlnfyfenfbxltlbfozxnfbtkqwnzqgswnfyezxflzfbfvflexufzqgsfnxnxqletyfqvnflptkqyxqwetvvtxyetlbzqgfbqmlnqywllxlrzafzcpxenetlbfofzwnxlrzqlvxrezyxsneqvvflefqlnafqnafyatlbxeaftuxphvqzwefbqlfospqytnxqltlbxgsyquxetnxqltlbqvnflatefpfgflneqvspthmfkfpxfuftzqgsfnxnxqlnqwzaxlrqlnafqvvflexuffpfgflneqvzqgswnfyefzwyxnhxenafyfvqyftkfnnfyufaxzpfvqynfzafutlrfpxegnqenwbflnexltgfyxztlaxraezaqqpevwynafymfkfpxfufnatntlwlbfyentlbxlrqvqvvflexufnfzalxiwfexefeeflnxtpvqygqwlnxlrtlfvvfznxufbfvfleftlbnatnnafnqqpetlbzqlvxrwytnxqlvqzweflzqwlnfyfbxlbfvflexufzqgsfnxnxqlebqfelqnpftbenwbflnenqclqmnafxyflfghtefvvfznxufphtenftzaxlrnafgnqtznxufphnaxlcpxcftltnntzcfysxzqznvxetlqvvflexufphqyxflnfbaxraezaqqpzqgswnfyefzwyxnhzqgsfnxnxqlnatneffcenqrflfytnfxlnfyfenxlzqgswnfyezxflzftgqlraxraezaqqpfyenftzaxlrnafgflqwratkqwnzqgswnfyefzwyxnhnqsxiwfnafxyzwyxqexnhgqnxutnxlrnafgnqfospqyfqlnafxyqmltlbfltkpxlrnafgnqkfnnfybfvflbnafxygtzaxlfenafvptrxesxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}""".lower()


letterFrequency = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.360,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074
}





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

def analyzeFrequency(text : str) -> Dict[str, float]:
    total : int = len(text) - 2
    totals : Dict[str, float] = {}
    for c in text:
        if (c in totals):
            totals[c] = totals[c] + 1
        elif c in letterFrequency:
            totals[c] = 1
    for key, value in totals.items():
        totals[key] = (value / total) * 100
    return totals

def analyzeFrequencyGroups(text : str, number : int) -> Dict[str, float]:
    totals: Dict[str, float] = {}
    total = len(text) - number + 1
    for c in range(len(text) - number + 1):
        combo : str = text[c : c + number]
        if combo not in totals:
            totals[combo] = 1
        else:
            totals[combo] = totals[combo] + 1
    # for key, value in totals.items():
    #     totals[key] = (value / total)
    return totals

def printDict(dict: Dict[Any, Any], minimum : float):
    for key, value in dict.items():
        if value >= minimum:
            print(f"key: {key} value: {value}")

def frequencyAttack(frequencies : Dict[str, float], baseFrequencies : Dict[str, float]) -> Dict[str, str]:
    dict : Dict[str, str] = {}
    for key, value in frequencies.items():
        min : float = 100000
        similarChar : str = ""
        for baseKey, baseValue in baseFrequencies.items():
            similarity : float = abs(baseValue - value)
            if similarity < min:
                min = similarity
                similarChar = baseKey
        if min <= 1.2:
            dict[key] = similarChar
    print(dict)
    return dict

def findThings(cipher : str):
    for i in range(len(cipher) - 2):
        if cipher[i] == 't' and cipher[i + 2] == 'e':
            print(cipher[i : i + 3])







dict : Dict[str, str] = createCipher(knownCypher, knownBase)
# print(dict)
print(solveCipher(dict, cipherText))
# num : int = 4
# num2 : float = 13
# groupDict = analyzeFrequencyGroups(cipherText, num)
# printDict(groupDict, num2)
# print('\n')
# groupDict = analyzeFrequencyGroups(solveCipher(dict, cipherText), num)
# printDict(groupDict, num2)
# printDict(analyzeFrequency(cipherText), 0)
# findThings(solveCipher(dict, cipherText))


