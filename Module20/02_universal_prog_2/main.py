
def is_prime(i_num):
    if i_num == 0 or i_num == 1:
        return False
    for i in range(2, i_num):
        if i_num % i == 0:
            return False
    return True


def crypto(text_in):
    return [j for i, j in enumerate(text_in) if is_prime(i)]


