def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total = 1
    if k>0 :
        while k >0:

            total = total * n
            n = n-1
            k = k -1
        return total
    else:
        return 1


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while y > 0:
        y, total = y // 10, total + y % 10,   # 这里的前后位置不会影响y的值，输入一个y，统一是先做右边的所有事情，再来赋值给左边。右边所有的y都是相等的。
    return total

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while(n > 0 ):
        if (n % 10 == 8):
            k = n // 10
            if(k % 10 ==8):
               return True
        n = n // 10                  # while 循环里的计数器是放在缩进里的，条件用if 来判断
       
    return False



    


