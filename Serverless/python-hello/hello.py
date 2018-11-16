import sys


def get_stdin():
    buf = str(sys.stdin.read())
    return buf


if __name__ == "__main__":
    st = get_stdin()
    print("Hello %s, you fabulous person, you!!!!" % st)

