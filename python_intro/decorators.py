#!/usr/bin/env python3


def announce(f):
    def wrapper():
        print("About to run..")
        f()
        print("Done!")
    return wrapper


@announce
def hello():
    print('Hello, world!')


if __name__ == '__main__':
    hello()
