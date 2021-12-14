#Define a function
def function():
    total = 0

    #Make a clear list
    numbers = []
    total_numbers = int(input("How many numbers you want to enter?: "))
    print("This programm will ask you to enter number(s)", total_numbers, "time(s)")

    #Make a loop to append numbers
    for num in range(total_numbers):
        append_number = int(input("Enter the number: "))
        numbers.append(append_number)

    #Print the final list items
    print("Here is the list",numbers)
    
    remove = 1
    
    #Remove the list
    remove_list = int(input("Do you want to clear the list? Press 1 for yes or any other integer for no: "))

    if remove == 1:
        numbers.clear()
        print("List is cleared")
    else:
        print("Ok, here is the list again",remove_list)

function()