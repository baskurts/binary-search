from binarysearch import *

def main():
    # set up local variables to store the list, first, and target
    a = []
    first = 0
    target = 0

    # prompt the user for the elements and input them into the list
    a = list(map(int, input("Enter ten numbers separated by a space: ").split()))

    # prompt the user for the index at which the search will begin
    first = int(input("Enter the index at which the search will begin: "))

    # prompt the user for thhe target
    target = int(input("Enter the target value to search for: "))

    # call search and display its return
    print('Target found at index ...', search(a, first, target))


if __name__ == "__main__":
    main()