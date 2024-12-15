# file2.py

from file1 import one
# from file1 import _this_should_not_be_imported  # Importing this would break convention.

def main():
    one.this_can_be_imported()  # This will work
    one._this_should_not_be_imported()  # Uncommenting this would work, but goes against Python conventions

main()
