
class Vehicle:

    def __init__(self, make, colour, num_seats):
        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __str__(self) -> str:
        """
        Returns all the vehicle information as a string.

        Returns:
            str: The vehicle's make, colour and amount of seats
        """

        return f"Make: {self.make}\nColour: {self.colour}\nNumber of Seats: {self.num_seats}"