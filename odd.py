first,last=map(int,input().split())
for i in range (first+1,last):
    if i % 2 != 0:
        print(i,end = "  ")
