"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    lst = []  # Make an empty list to store things in

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
