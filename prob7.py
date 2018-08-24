'''
Run the program using python3 prob7.py
First insert number of n when asked input
and for n times, you insert the command;
i.e. add hendra
    find h
'''

def inc(d, st):
    n = d.get(st,0)
    if (n==0):
        d[st] = 1
    else:
        d[st] += 1
        
n = int(input("input: "))
dic = {}
for index in range(n):
    inp = input()
    
    for idx in range(len(inp)-3):
        if (inp[idx:idx+3]=="add"):
            i = idx+3
            while ((i<len(inp))and(inp[i]!=" ")):
                i+=1
            i+=1
            nama = ""
            while(i<len(inp)):
                nama += inp[i]
                i+=1
            inc(dic, nama)
            break
        elif (inp[idx:idx+3]=="fin"):
            if (idx+3<len(inp)) and (inp[idx+3]=='d'):
                i = idx+4
                while ((i<len(inp))and(inp[i]!=" ")):
                    i+=1
                i+=1
                nama = ""
                while i<len(inp):
                    nama += inp[i]
                    i+=1
                total = 0
                for isi in dic.keys():
                    if (isi[0:len(nama)]==nama):
                       total += dic[isi]
                print(total)
     
