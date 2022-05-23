
def lambda_curry2(func):          
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    def h(x):
        def g(y):
            return func (x, y)
        return g
    return h 



def count_cond(condition):      #函数的参数传入可以是一个函数。
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2      # 当函数的参数是一个函数的时候,我们可以用lamda 函数来定义这个函数,并且赋值给一个变量。
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***" 
    def h (x):             #当有多个参数和条件的时候，我们可以在 def 语句里面使用 def 语句。最内层的就是最后的答案。
        i, count = 1, 0
        while i <= x:
            if condition(x, i):
                count += 1
            i += 1 
        return count
    return h
    

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        if compose1(f, g)(x) == compose1(g, f)(x):               #这里的等式数值相等不可以写成 compose1(f, g)== compose1(g, f） 和 compose1(f, g) = compose1(g, f）
        
            return True                                          # compose1(f, g) = compose1(g, f）这是两个函数的比较，必须带着具体的数值才能比较。
        else:
            return False
    
    return h




def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def h(n):
        def g(x):
            i = 0    #初始化的值放在循环之前。不要放在 while 里面。否则会出现错误  local variable 'i' referenced before assignment 
            while i < n:        
                if i % 3 == 0:        # 当 n 是1 的时候，我们是f1（x）,这时候相当于 i 等于0 的操作。因此这里的条件不是 i % 3 == 1
                    x = f1(x)
                if i % 3 == 1:
                    x = f2(x)
                if i % 3 == 2:
                    x = f3(x)
                i = i + 1
            return x
        return g
    return h

