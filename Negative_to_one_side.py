num= [-12, 11, -13, -5, 6, -7, 5, -3, -6]

p1 = 0
p2 = len(num) - 1

while p1 <= p2:
    if num[p1] < 0:
        p1 += 1
    elif num[p2] >= 0:
        p2 -= 1
    else:
        num[p1], num[p2] = num[p2], num[p1]
        p1 += 1
        p2 -= 1

print(num)