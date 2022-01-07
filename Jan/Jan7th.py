
def reverse(x):
    s = str(abs(x))
    reversed = int(s[::-1])
    if reversed > 2147483647:
        return 0;
    if x >0 :
        return reversed
    else:
        return reversed * -1


if __name__ == '__main__':
    num = 123
    print(reverse(num))
    a = -456
    print(reverse(a))
    print(reverse(0))