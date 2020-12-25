#code snippet 1
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("Hi")
#time complexity of this code snippet in equivalent python code is O(n^2) as the loop would run (n^2+n)/2 times

#code snippet 2
m=int(input())
for x in range(1,m+1):
    x*=3
    for y in range(1,m+1):
        print("Hello")
#time complexity for this equivalent python code snippet is O(n*log(n))
