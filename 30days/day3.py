if __name__ == '__main__':
    N = int(input())

    if N%2 != 0:
        print("Weird")
    elif N%2 == 0 and N>=2 or N<=5:
        print("Not Weird")
    elif N%2 == 0 and N>= 6 or N<=20:
        print("Weird")
    else:
        print("Not Weird")