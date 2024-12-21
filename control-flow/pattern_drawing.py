# User Input For the size of pattern
size = int(input("Enter the size of the pattern: "))
# Validate Input
if size > 0:
    row = 0
    # Use A while to handle rows
    while row < size:
        # Use a for loop to handle coolumns
        for col in range(size):
            print("*", end="") 
        print() # Move to the next line after row has complete
        row += 1
else:
    print ("Please enter a positive interger.")
