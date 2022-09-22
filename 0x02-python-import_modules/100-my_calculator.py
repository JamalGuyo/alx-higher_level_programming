#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == '__main__':
    count = len(argv) - 1
    if count == 3:
        if argv[2] not in ['+', '-', '*', '/']:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
        else:
            if argv[2] == '+':
                print("{} {} {} = {}"
                      .format(argv[1], argv[2], argv[3],
                              add(int(argv[1]), int(argv[3]))))
            if argv[2] == '-':
                print("{} {} {} = {}"
                      .format(argv[1], argv[2], argv[3],
                              sub(int(argv[1]), int(argv[3]))))
            if argv[2] == '*':
                print("{} {} {} = {}"
                      .format(argv[1], argv[2], argv[3],
                              mul(int(argv[1]), int(argv[3]))))
            if argv[2] == '/':
                print("{} {} {} = {}"
                      .format(argv[1], argv[2], argv[3],
                              div(int(argv[1]), int(argv[3]))))
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        print(f'Count is ::::: {count}')
        exit(1)
