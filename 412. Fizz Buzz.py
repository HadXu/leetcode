def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """

    return ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0  else str(i) for i in
            range(1, n + 1)]


if __name__ == '__main__':
    res = fizzBuzz(15)
    print(res)