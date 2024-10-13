x=int(input())
y=int(input())
if (x//12)>y:
    print(f'Profit:{x-(12*y)}')
else:
    print(f'loss:{(12*y)-x}')
