fib_seq=[0]*10
a=0
b=1
for i in range(10):
    temp=b
    b=b+a
    a=temp
    fib_seq[i]=a

print(fib_seq)
