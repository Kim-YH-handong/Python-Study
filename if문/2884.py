H, M = map(int, input().split())

M = (H*60) + M
M = M - 45

if M == 0:
    print("0 0")
elif M < 0:
    print("23 %d" %(M%60))
else:
    print("%d %d" %(M/60, M%60))