for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=' ')


print()
for i in range(1, 10):
    print(i, end = ' ')


print()
for i in range(0, 10, 2):
    print(i, end = ' ' )


print()
print("{}{}".format(range(0, 10), list(range(0, 10))))

print()
print(list(range(0, 20, 5)))
print(list(range(-10, 0 , 2)))
print(list(range(3, -10, -3)))
print(list(range(0, -5, 1)))

# # 구구단

# gugu(2) # 2단


# gugudan() # 전체의 구구단
print()
for i in range(2, 10, 1):
    print("*** {} 단 ***".format(i))
    for j in range(1, 10, 1):
        print("{} * {} = {}".format(i, j, i*j), end = '\n')

# gugudan_land() # 2*1=2 3*1=3 .... 9*1=9