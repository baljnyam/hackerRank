if __name__ == '__main__':
    try:
        N = int(input())
        x = [[x for x in input().split(' ')] for _ in range(N)]
        b = []
        for i in x:
            for j in i:
                if j == "insert":
                    b.insert(int(i[1]), int(i[2]))
                elif j == "print":
                     print(b, "\n")
                elif j == "remove":
                     b.remove(int(i[1]))
                elif j == "append":
                     b.append(int(i[1]))
                elif j == "sort":
                     b.sort()
                elif j == "pop":
                     b.pop()
                elif j == "reverse":
                     b.reverse()
    except:
        print("Wrong input")              
