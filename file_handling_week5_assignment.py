# File Creation
try:
    # Open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Hello, World!\n")
        print("File 'my_file.txt' created successfully.")
except PermissionError:
    print("Permission denied. Unable to create the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()

# File Reading and Display
try:
    # Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File not found. Unable to read the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()

# File Appending
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("Line 4: Appended line 1.\n")
        file.write("Line 5: 98765\n")
        file.write("Line 6: Goodbye, World!\n")
        print("Three lines appended to 'my_file.txt'.")
except PermissionError:
    print("Permission denied. Unable to append to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()
