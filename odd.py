first,last=map(int,input().split())
for i in range (first,last+1):
    if i % 2 != 0:
        print(i,end = "  ")
