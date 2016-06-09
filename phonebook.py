#!/usr/bin/env python

from terminaltables import AsciiTable
import os
import sys


def check_phonebook_existence(f):
    def wrapper(*args):
        phonebook = args[-1]
        if not os.path.isfile(phonebook + ".pb"):
            print "Phonebook does not exists!"
            exit(1)
        return f(*args)
    return wrapper


def create(phonebook):
    if os.path.isfile(phonebook + ".pb"):
        print "Phonebook already exists!"
        exit(1)
    f = open(phonebook + ".pb", "w")
    f.close()
    print "{} created".format(phonebook)


def names_and_numbers(f):
    for line in f:
        yield line.strip().split(":")


@check_phonebook_existence
def add(name, number, phonebook):
    f = open(phonebook + ".pb", "r+w")
    for line_name, line_number in names_and_numbers(f):
        if line_name == name:
            print "Error: name already exists: {}".format(
                name
            )
            f.close()
            exit(1)
    f.write(name + ":" + number + "\n")
    f.close()
    print "{} added with number {}".format(name, number)


@check_phonebook_existence
def lookup(name, phonebook):
    f = open(phonebook + ".pb")
    for line_name, line_number in names_and_numbers(f):
        if line_name == name:
            print "Phone number for {} is: {}".format(
                line_name, line_number
            )
            f.close()
            exit(0)
    print "Error: {} not found".format(name)
    f.close()
    exit(1)

@check_phonebook_existence
def reverse_lookup(number, phonebook):
    f = open(phonebook + ".pb")
    for line_name, line_number in names_and_numbers(f):
        if line_number == number:
            print "Name for {} is: {}".format(
                line_number, line_name
            )
            f.close()
            exit(0)
    print "Error: {} not found".format(number)
    f.close()
    exit(1)


@check_phonebook_existence
def show(phonebook):
    f = open(phonebook + ".pb")
    table_cells = [["Name", "Number"]]
    table_cells += list(names_and_numbers(f))
    table = AsciiTable(table_cells)
    print table.table
    exit(0)


# parseing arguments

CMDS = {
    "create": create,
    "add": add,
    "lookup": lookup,
    "reverse_lookup": reverse_lookup,
    "show": show,
}


def main():
    cmd = CMDS[sys.argv[1]]
    cmd(*sys.argv[2:])

if __name__ == "__main__":
    main()
