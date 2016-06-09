from terminaltables import AsciiTable
import os
import sys


def create(phonebook):
    if os.path.isfile(phonebook + ".pb"):
        print "Phonebook already exists!"
        exit(1)
    f = open(phonebook + ".pb", "w")
    f.close()


def add(name, number, phonebook):
    if not os.path.isfile(phonebook + ".pb"):
        print "Phonebook does not exist!"
        exit(1)
    f = open(phonebook + ".pb", "r+w")
    for line in f.readlines():
        line_name, line_number = line.strip().split(":")
        if line_name == name:
            print "Error: name already exists: {}".format(
                name
            )
            f.close()
            exit(1)
    f.write(name + ":" + number + "\n")
    f.close()


def lookup(name, phonebook):
    if not os.path.isfile(phonebook + ".pb"):
        print "Phonebook does not exist!"
        exit(1)
    f = open(phonebook + ".pb")
    for line in f.readlines():
        line_name, line_number = line.strip().split(":")
        if line_name == name:
            print "Phone number for {} is: {}".format(
                line_name, line_number
            )
            f.close()
            exit(0)
    print "Error: {} not found".format(name)
    f.close()
    exit(1)


def reverse_lookup(number, phonebook):
    if not os.path.isfile(phonebook + ".pb"):
        print "Phonebook does not exist!"
        exit(1)
    f = open(phonebook + ".pb")
    for line in f.readlines():
        line_name, line_number = line.strip().split(":")
        if line_number == number:
            print "Name for {} is: {}".format(
                line_number, line_name
            )
            f.close()
            exit(0)
    print "Error: {} not found".format(number)
    f.close()
    exit(1)


def show(phonebook):
    if not os.path.isfile(phonebook + ".pb"):
        print "Phonebook does not exist!"
        exit(1)
    f = open(phonebook + ".pb")
    table_cells = [["Name", "Number"]]
    for line in f.readlines():
        cell = list(line.strip().split(":"))
        table_cells.append(cell)
    table = AsciiTable(table_cells)
    print table.table
    exit(0)


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
