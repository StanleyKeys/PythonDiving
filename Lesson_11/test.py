


def s():
    a = 4
    b = 5

    list1 = [0] * a

    for i in range(a):
        list1[i] = [0] * b


    list1[2][3] = 5
    print(list1)

if __name__ == '__main__':
    s()