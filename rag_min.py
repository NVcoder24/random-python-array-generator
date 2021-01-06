import random

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_rand_char():
    return random.choice(list(chars))


def get_rand_str(minimum, maximum):
    i = random.choice(list(range(minimum, maximum)))
    string = ""
    while(True):
        string = string + get_rand_char()
        i = i - 1
        if i == 0:
            break
    return string


def get_rand_array(amount, minimum, maximum):
    array_ = []
    while(True):
        array_.append(get_rand_str(minimum, maximum))
        amount = amount - 1
        if amount == 0:
            break
    return array_


def convert_array_to_string(array):
    base = "[{content}]"
    element = "\"{content}\","
    inner = ""
    for ele in array:
        ele = str(ele)
        inner = inner + element.format(content=ele)
    return base.format(content=inner)
