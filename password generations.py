import random
import string


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def random_string(length) -> str:
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(length))


def main() -> None:
    pass_len = int(input("How namy sumbols do you want? "))


    print(bcolors.OKBLUE+random_string(pass_len))
    input()

if __name__ == '__main__':
    main()
