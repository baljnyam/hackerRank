def split_and_join(line):
    # write your code here
    a = line.split(" ") # a is converted to a list of strings. 
    a = "-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
