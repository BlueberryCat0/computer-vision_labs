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

def check(i, j, type):
    print('----', i, j)
    print(type)
    try:
        if image[i+1][j] == 1 and type != 1:
            image[i+1][j] = num
            # return [i+1, j]
            # i = i+1
            print('llll')
            check(i+1, j, 1)
    except Exception as e:
        pass
    try:
        if image[i][j+1] == 1 and type != 2:
            image[i][j+1] = num
            print('rrr')
            # return [i, j+1]
            check(i, j+1, 2)
    except Exception as e:
        pass
    try:
        if image[i-1][j] == 1 and type != 3:
            image[i-1][j] = num
            print('ppp')
            # return [i-1, j]
            check(i-1, j, 3)
    except Exception as e:
        pass
    try:
        if image[i][j-1] == 1 and type != 4:
            image[i][j-1] = num
            print('yyy')
            # return [i, j-1]
            check(i, j-1, 4)
    except Exception as e:
        pass
    return [i, j]

num = 2

for i in range(m):
    for j in range(n):
        if image[i][j] == 1:
            try:
                image[i][j] = num
                # print('----------', i, j)
                if image[i+1][j] == 1:
                    image[i+1][j] = num
                    check(i, j, 0)
                    # print(a)
                    num+=1
                    break
            except Exception as e:
                pass
                num+=1
        # break







pprint(image)





















#
