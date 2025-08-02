def convert_string(num):
    new_list = list(range(num))
    new_list = [x+1 for x in new_list]
    return "".join(str(n) for n in new_list)
if __name__ == '__main__':
    n = int(input())
    print(convert_string(n))