import random
import pyperclip

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

if __name__ == "__main__":
    while(True):
        try:
            a = int(input("minimum symbols in string of array: "))
            break
        except Exception as e:
            print(f"error: {e}\nplease try again")

    while(True):
        try:
            b = int(input("maximum symbols in string of array: "))
            break
        except Exception as e:
            print(f"error: {e}\nplease try again")

    while(True):
        try:
            c = int(input("amount of strings in array: "))
            break
        except Exception as e:
            print(f"error: {e}\nplease try again")

    array = get_rand_array(c, a, b)
    print(f"success!\n{array}")

    while(True):
        yn = input("copy array to clipboard? (yes or no): ")
        if yn == "yes":
            pyperclip.copy(convert_array_to_string(array))
            print("copied!")
            break
        elif yn == "no":
            print("good bye!")
            break
        else:
            print("please try again!")
