#!/usr/bin/env python3

from argparse import ArgumentParser
from secrets import choice
from pyperclip import copy
import string

parser = ArgumentParser(description="A secure random password generator!")

NUMBER = string.digits
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SYMBOL = string.punctuation


def main():
    addArgument()
    args = parser.parse_args()

    args.verbose and print("You are running the program in verbose mode")
    args.verbose and print("The following characters are chosen for password generation.")

    characters = ""

    if args.custom is not None:
        args.verbose and print("Using customized characters: {0}".format(args.custom))
        characters = args.custom

    else:
        if args.symbol:
            args.verbose and print("Including symbols: {0}".format(SYMBOL))
            characters += SYMBOL

        if not args.excludeNumber:
            args.verbose and print("Including numbers: {0}".format(NUMBER))
            characters += NUMBER

        if not args.excludeLowercase:
            args.verbose and print("Including lowercase letters: {0}".format(LOWERCASE))
            characters += LOWERCASE

        if not args.excludeUppercase:
            args.verbose and print("Including uppercase letters: {0}".format(UPPERCASE))
            characters += UPPERCASE

        args.verbose and print("Password(s) will be generated from these characters:\n\n{0}\n".format(characters))

    args.verbose and print(f"Generating {args.number} set{'s'[:args.number^1]} of password.\n")

    for _ in range(args.number):
        password = ''.join(choice(characters) for _ in range(args.length))
        print(password)

    copy(password)

    args.verbose and print("The last password has been copied to the clipboard.")


def addArgument():
    parser.add_argument("-l", "--length", type=int, help="Password Length (default 16)", default=16)
    parser.add_argument("-s", "--symbol", action='store_true', help="Includes symbols (e.g. @#$%%)")
    parser.add_argument("--excludeNumber", action='store_true', help="Excludes numbers")
    parser.add_argument("--excludeLowercase", action='store_true', help="Excludes lowercase letters")
    parser.add_argument("--excludeUppercase", action='store_true', help="Excludes uppercase letters")
    parser.add_argument("-n", "--number", type=int, help="Numbers of password to be generated", default=1)
    parser.add_argument("-c", "--custom", type=str, help="Provides customized characters as a string")
    parser.add_argument("-v", "--verbose", action='store_true', help="Run the program in verbose mode")


if __name__ == "__main__":
    main()
