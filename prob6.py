'''
To run this program, make sure you've installed python3.
Open terminal/command prompt, go to directory of this program
and type python3 prob6.py. and then follow the instruction to get how
many char removed to make both string anagram
'''

from math import fabs as abs

def inc(d, st):
    for isi in st:
        n = d.get(isi,0)
        if (n==0):
            d[isi] = 1
        else:
            d[isi] += 1
            
def anagram(string1, string2):
    dic = {}
    dic2 = {}
    delta = 0
    inc(dic, string1)
    inc(dic2, string2)
    arr1 = [isi for isi in dic.keys()]
    arr2 = [isi for isi in dic2.keys()]

    bedakey = [isi for isi in arr1 if isi not in arr2]
    for isi in bedakey:
        delta += (dic[isi]-1)
    delta += (len(bedakey))

    bedakey = [isi for isi in arr2 if isi not in arr1]
    for isi in bedakey:
        delta += (dic2[isi]-1)
    delta += (len(bedakey))

    samakey = [isi for isi in arr2 if isi in arr1]
    for isi in samakey:
        delta+=abs(dic[isi]-dic2[isi])
    return delta

if __name__ == '__main__':
    
    st1 = input("Insert first string: ")
    st2 = input("Insert second string: ")
    anagram(st1, st2)
    
