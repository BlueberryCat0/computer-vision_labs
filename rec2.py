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

image = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
# image = [
#     [1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0],
# ]

pprint(image)
m = len(image)
n = len(image[0])
km = 0
kn = 0
cur = 1

def check(i, j, q=-1, p=-1):
    print('Enter', i, j, q, p)
    try:
        if image[i-1][j] == 1 and not (i-1 == q and j == p):
            image[i-1][j] = num
            check(i-1, j, i, j)
    except Exception as e:
        pass
    try:
        print('FFF', i, j)
        if image[i][j+1] == 1 and not (i == q and j+1 == p):
            image[i][j+1] = num
            check(i, j+1, i, j)
    except Exception as e:
        pass
    try:
        if image[i+1][j] == 1 and not (i+1 == q and j == p):
            image[i+1][j] = num
            check(i+1, j, i, j)
    except Exception as e:
        pass
    try:
        if image[i][j-1] == 1 and not (i == q and j-1 == p):
            image[i][j-1] = num
            check(i, j-1, i, j)
    except Exception as e:
        pass
    # check(i, j)
    # num = num
    # return [i, j]
    return num

num = 2

for i in range(m):
    for j in range(n):
        if image[i][j] == 1:
            print(i, j)
            try:
                num+=1
                image[i][j] = num
                # if image[i+1][j] == 1:
                check(i, j)
                print('----')
                break
            except Exception as e:
                pass
        if image[i][j] == 'p':
            print('---', i, j)
    # num+=1






pprint(image)





















#
