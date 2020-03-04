if __name__ == "__main__":
    n = int(input())
    phonebook = {}

    for _ in range(n):
        name, number = map(str, input().split())
        phonebook[name] = number

    while True:
        try:
            query = input()

            if query in phonebook:
                number = phonebook[query]
                print(query + "=" + number)
            else:
                print("Not found")
        except:
            break

    
    




