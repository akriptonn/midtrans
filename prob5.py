'''
To use this program, first input number of line input,
then for each line you insert the Bus schedule for arrival and departure
i.e
input: 2
input: Bus 1 A 10:00 10:05
input: Bus 2 A 10:01 10:100
output: 1

The big O of this code is O(n^2)
'''
def compa(st, st2): #if st>st2 return 0, else 1
    i1 = st.split(":")
    in1 = (int(i1[0]))*60+(int(i1[1]))
    i1 = st2.split(":")
    in2 = (int(i1[0]))*60+(int(i1[1]))
    if (in1>in2):
        return 0
    elif (in1<in2):
        return 1
    else:
        return 2
    
inp = int(input())
dic_a = {}
dic_d = {}
for index in range(inp):

    line = input()
    temp = line.split(" A ")
    temp2 = temp[1].split(" D ")
    dic_a[temp[0]]=temp2[0]
    dic_d[temp[0]]=temp2[1]
    
maxi = 0
lis = [isi for isi in dic_a.values()]
lis2 = [isi for isi in dic_d.values()]
for idx in range(len(lis)-1):
    num = 0
    for i in range(len(lis)-idx-1):
        k = i+idx+1
        if (compa(lis[idx],lis[k])==1):
            if (compa(lis2[idx],lis[k])==0):
                num += 1
        elif (compa(lis[idx],lis[k])==2):
            num+=1
    if (num>maxi):
        maxi = num
print(maxi)
                

    
    
