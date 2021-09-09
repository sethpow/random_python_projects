def run_fizz_buzz():
    for num in range(1, 101):
        my_str = ''

        if num % 3 == 0:
            my_str += 'Fizz'
        if num % 5 == 0:
            my_str += 'Buzz'
        if my_str == '':
            my_str = num

        print(my_str)