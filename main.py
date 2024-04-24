# This is a program to convert temperatures from Farenheit to Celcius.
# All the lines or portions of lines starting with # are comments.
# They help humans understand the program, but the computer ignores them when running the program.
# Comments are important because good programmers write programs which are easy for other humans to understand.

# A variable is a reserved memory location on the computer to store a piece of information.
# You can think of a variable as a "box" in which the piece of information can be placed.
# These pieces of information have different "types", such as
#.  * booleans, which can be only True or False
#.  * strings, which are sequences of characters (roughly, letters, numbers, and spaces), like "hello".
#.  * numbers. In Python, we use "int" for integers and "float" for decimals.
#
# Below we make a variable should_continue which holds whether the program should keep going.
# We start it off with the boolean value True. 
should_continue = "y"
 
# The while loop will run the instructions in the block within it as long as the test condition is True.
while should_continue: # <--- Test experssion

    # Next we need to ask the user for the temperature to convert. 
    # We do this by calling the function "input".  
    # A function is a miniature program.  
    # By building up programs from other "mini-programs"
    # we can build much more complex programs than we could on our own. 
    # *input* which displays a message to the user.
    # Once the user presses enter, the input function will return what they typed as a string value.
    # That string value will be stored in the degrees_farenheit_as_string variable.
    # What does the '\t' at the end of the text do?
    degrees_farenheit_as_string = input("Enter a temperature in degrees Farenheight (F):\t")

    # We can't do math with strings, only numbers, so we need to convert the value in degrees_farenheit_as_string
    # from a string to a number.  Luckily, Python has a built in function for this - int.
    degrees_farenheit_as_integer = int(degrees_farenheit_as_string)

    # Convert temperature from F to Celsius and store that in a new variable.
    # Python "knows" the math might result in a decimal value, so the result of this computation is of type float.
    degrees_celcius = (degrees_farenheit_as_integer - 32) * 5 / 9

    # We round the value in degree_celcius to two digits to make it easier to display.
    # We use the build-in function round, and we put the resulting value back into the same variable.
    degrees_celcius = round(degrees_celcius, 2)

    # Print the result to the screen using the built-in function print
    print ("\nTemperature in degrees C is:", degrees_celcius)

    # Check for temperature below freezing and print a cute message.
    # An if statement tests a condition. If the condition is True, it runs the block inside. Otherwise, it skips it.
    if degrees_celcius < 0: # <--- test condition
        print ("Pack long underwear!\n")

    # Check for it being a hot day and print a cute message
    if degrees_celcius > 35:
        print ("Remember to hydrate!\n")

    if input("Convert another temperature?\t") == "y":
        should_continue = True
    else: # <--- if we provide an "else" block to an if statement, it will be executed if the condition is False
        should_continue = False
    # Now we go back to while should_continue above!

# Exit the program

'''
Ideas to expand the program:
1. Change the messages to have different advice for extreme temperatures.
2. Change the message to show the temperature in F and C, i.e. 'The temperature 
   104 F is 40.0 C'
3. Add another temperature trigger check for very extreme temps.
4. Collect the person’s name before the loop starts (store in a variable) and 
   add this to the output messages.
5. Check for Y or Yes or yes in addition to checking for just y
6. Change to allow for numbers other than integers
7. Add option to change from F to C or C to F (advanced)

This example program is adapted from https://github.com/yelirkram/Troop-255-Programming-MB
'''