n = int(input(" "))
i = 2
while i <= n/2 :
    if n % i == 0 :
        print("no")
        break
    i += 1
if i > n/2 :
    print("yes")
