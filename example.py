from pprint import pprint

image = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

pprint(image)
m = len(image)
n = len(image[0])
print(m, n)
km = 0
kn = 0
cur = 1

i = 1
j = 1
# for i in image:
#     for j in i:
#         kn = j - 1
#         if kn < 0:
#             kn = 1
#             b = 0
#         else:
#             b = image[image.index(i)][kn]
#         print(b)

for i in range(m):
    for j in range(n):

        # ------------
        kn = j - 1
        if kn < 0:
            kn = 1
            b = 0
        else:
            kn = 1
            b = image[i][kn]

        # ------------
        km = i - 1
        if km < 0:
            km = 1
            c = 0
        else:
            c = image[km][j]

        a = image[i][j]
        if a == 0:
            pass
        elif b == 0 and c == 0:
            cur+=1
            image[i][j] = cur
        elif b != 0 and c == 0:
            image[i][j] = b
        elif b == 0 and c != 0:
            image[i][j] = c
        elif b != 0 and c != 0:
            if b == c:
                image[i][j] = b
            else:
                print('kek')

pprint(image)




















#
