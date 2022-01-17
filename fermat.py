import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y / 2, N)
    if y % 2 == 0:
        return z ^ 2 % N
    else:
        return x * z ^ 2 % N


def fprobability(k):
    return 1 - (1 / pow(2, k))


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if N == 2:
        return 'prime'

    if N % 2 == 0:
        return 'composite'

    for x in range(0, k):
        y = random.randint(1, N-1)
        if pow(y, (N - 1)) % N != 1:  # probably not the right place to mod, but it seems to work for now
            return 'composite'
        return 'prime'



def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    return 'composite'
