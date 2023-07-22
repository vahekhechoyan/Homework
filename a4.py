for a in range(1,10000):
    sum=0
    for b in range(1,a):
        if a%b==0:
            sum= sum + b
    if a==sum:
        print(a," is a perfect square")
