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

# image = [
#     [1, 0, 0, 1],
#     [1, 1, 1, 1],
#     [1, 0, 0, 1],
# ]

pprint(image)
m = len(image)
n = len(image[0])
# print(m, n)
km = 0
kn = 0
cur = 1

i = 1
j = 1

no = [0, 1]
beside = 2
def get_beside(i, j, beside):
    try:
        if image[i+1][j] not in no:
            beside = image[i][j]
            return beside
    except Exception as e:
        pass
    try:
        if image[i][j+1] not in no:
            beside = image[i][j+1]
            return beside
    except Exception as e:
        pass
    try:
        if image[i-1][j] not in no:
            beside = image[i-1][j]
            return beside
    except Exception as e:
        pass
    try:
        if image[i][j-1] not in no:
            beside = image[i][j-1]
            return beside
    except Exception as e:
        pass

    # beside+=1
    # print('ll')
    return beside




# for i in range(m):
#     for j in range(n):
#         if image[i][j] == 1:
#             image[i][j] == 2
#         try:
#             if image[i+1][j] == 1:
#                 image[i+1][j] = 2
#         except Exception as e:
#             pass
#         try:
#             if image[i][j+1] == 1:
#                 image[i][j+1] == 2
#         except Exception as e:
#             pass
#         try:
#             if image[i-1][j] == 1:
#                 image[i-1][j] == 2
#         except Exception as e:
#             raise
#         try:
#             if image[i][j-1] == 1:
#                 image[i][j-1] == 2
#         except Exception as e:
#             raise

# for i in range(m):
#     for j in range(n):
#         print(image[i][j])
#         a = False
#         b = get_beside(i, j, beside)
#         beside = b
#         if image[i][j] == 1:
#             image[i][j] == b
#         try:
#             if image[i+1][j] == 1:
#                 image[i+1][j] = b
#                 a = True
#         except Exception as e:
#             pass
#         try:
#             if image[i][j+1] == 1:
#                 image[i][j+1] == b
#                 a = True
#         except Exception as e:
#             pass
#         try:
#             if image[i-1][j] == 1:
#                 image[i-1][j] == b
#                 a = True
#         except Exception as e:
#             pass
#         try:
#             if image[i][j-1] == 1:
#                 image[i][j-1] == b
#                 a = True
#         except Exception as e:
#             pass
#
#         if not a:
#             beside+=1

for i in range(m):
    for j in range(n):
        a = False
        b = get_beside(i, j, beside)
        # beside = b
        print(b)
        if image[i][j] == 1:
            # print('dd')
            image[i][j] = b
            # a = True
            # print(image[i][j])
            try:
                if image[i+1][j] not in no:
                    image[i][j] = image[i+1][j]
                    print('lel')
                    a = True
            except Exception as e:
                pass
            try:
                if image[i][j+1] not in no:
                    image[i][j] = image[i][j+1]
                    print('kek')
                    a = True
            except Exception as e:
                pass
            try:
                if image[i-1][j] not in no:
                    image[i][j] = image[i-1][j]
                    print('cheb')
                    a = True
            except Exception as e:
                pass
            try:
                if image[i][j-1] not in no:
                    image[i][j] = image[i][j-1]
                    print('urec')
                    a = True
            except Exception as e:
                pass

            if not a:
                print('index', i, j)
                beside+=1

pprint(image)























        #
