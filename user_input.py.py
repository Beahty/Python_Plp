# Task: Write a program that asks the user for their name, age, and location and then prints out a personalized message.
# Instructions:
# Create a new Python file and name it "user_input.py"
# Use the input() function to ask the user for their name and store it in a variable called "name".
name=str(input("Enter your name: "))
# Use the input() function to ask the user for their age and store it in a variable called "age".
age=int(input("Enter your age: "))
# Use the input() function to ask the user for their location and store it in a variable called "location".
location=str(input("Enter your location: "))
# Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
print("Hello "+str(name)+" you are "+str(age)+" years old and lives in "+str(location))
#  Save and run the program to see the output.