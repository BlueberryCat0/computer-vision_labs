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

#   C
# B A
for i in range(1, m):
    for j in range(1, n):

        print(image[i][j])
        # ------------
        kn = j - 1
        if kn < 0:
            kn = 1
            B = 0
        else:
            kn = 1
            B = image[i][kn]

        # ------------
        km = i - 1
        if km < 0:
            km = 1
            C = 0
        else:
            C = image[km][j]

        A = image[i][j]
        print(B, A, C)
        if A == 0:
            pass
        elif B == 0 and C == 0:
            cur = cur + 1
            print('dddddd', cur)
            image[i][j] = cur
        elif B != 0 and C == 0:
            image[i][j] = B
        elif C != 0 and B == 0:
            image[i][j] = C
        elif C != 0 and B != 0:
            if B == C:
                image[i][j] = B
            else:
                print('ll')
                # image[i][j] = B
                # for l in image:
                #     for k in l:
                #         if k == C:
                #             c = B


pprint(image)




















#
