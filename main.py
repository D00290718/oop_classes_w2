from shapes import Rectangle
import random #your program should generate a random number between 1 and 10.

#29/09/2026 14:00-16:00
#D00290718

#new worksheet : Constructors & Encapsulation File PDF
#exercise B4

if __name__ == "__main__":

    objects = []

    for i in range(5):
        print(f"\n\n{i+1}/5")


        length = int(input("Length: "))
        width = int(input("Width: "))

        # Exercise A4 on new worksheet
        number = random.randint(1, 10)
        if number % 2 == 0:
            print(f"You got an even number so you are allowed to pick your own colour!")
            colour = str(input("Colour: ")).lower()
            obj = Rectangle(length, width, colour)
            obj.colour = colour
        else:
            print(f"You got an odd number so I chose the default colour for you.")
            obj = Rectangle(length, width)
            obj.colour = "blue"


        obj.length = length
        obj.width = width


        objects.append(obj)

    largest_area = {
        "value": 0,
        "details": ""
    }

    smallest_width = 99999
    smallest_width_list_pos = -1

    red_rectangles = []

    user_input_coloured_rectangles = []

    while True:
        #Ask the user to enter a colour,
        user_colour_to_find = input("\nPlease enter a colour to find: ").lower()
        if user_colour_to_find == "red":
            print("Error - Choose any other colour, just not red.")
        else:
            break

    _ = 0 #temp variable to get the list pos.
    for obj in objects:
        # Locate the Rectangle with the largest area and display its details using its display method.
        area = obj.calc_area()
        current_value = largest_area["value"]
        if area > current_value:
            details = obj.display()
            largest_area["value"] = area
            largest_area["details"] = details

        #Locate the Rectangle with the smallest width and display its position in the list

        width = obj.width
        if width < smallest_width:
            smallest_width = width
            smallest_width_list_pos = _

        #Locate all Rectangles with the colour “red” (case-insensitive),

        if obj.colour.lower() == "red":
            red_rectangles.append(obj)
        elif obj.colour.lower() == user_colour_to_find:
            user_input_coloured_rectangles.append(obj)
        _ += 1

    #1:
    print("\n\nQ1. The Rectangle with the Largest Area:")
    print(f"Area: {largest_area["value"]}")
    print(f"Details: {largest_area["details"]}")


    #2:
    print(f"\n\nQ2. Rectangle with the Smallest Width: {smallest_width} in position {smallest_width_list_pos}")

    #3:
    if len(red_rectangles) == 0: #If there are no red Rectangles, display a message indicating this to the user
        print("\n\nQ3. Sorry, there are no red rectangles.")
    else:
        print(f"\n\nQ3. There are {len(red_rectangles)} red rectangles! Here they are:")
        for obj in red_rectangles:
            print(obj.display())

    #4:

    #ask the user to enter a colour, then repeat the above action to find, store and display all Rectangles of that colour.
    if len(user_input_coloured_rectangles) == 0: #If there are no red Rectangles, display a message indicating this to the user
        print(f"\n\nQ4. Sorry, the colour you chose there are no {user_colour_to_find} rectangles.")
    else:
        print(f"\n\nQ4. There are {len(user_input_coloured_rectangles)} {user_colour_to_find} rectangles! Here they are:")
        for obj in user_input_coloured_rectangles:
            print(obj.display())
