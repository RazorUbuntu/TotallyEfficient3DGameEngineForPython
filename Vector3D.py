from math import sqrt  # import the math module for the square root function


class Vector3D:
    # create a class attribute to keep track of the number of vector objects
    counter = 0

    def __init__(self, *args, constant=None) -> None:
        # set the default values of x, y, z, and alpha
        self.x = 0
        self.y = 0
        self.z = 0
        self.alpha = 1

        # check if a constant value is given and call the set constant vector method if it is
        if constant is not None:
            self.set_constant(constant)
            pass

        # check the length of args and assign the values accordingly
        elif len(args) == 0:  # if no arguments are given
            pass  # do nothing, use the default values

        elif len(args) == 3:  # if only x, y, and z are given
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        elif len(args) == 4:  # if x, y, z, and alpha are given
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.alpha = args[3]

        else:  # if invalid number of arguments are given
            raise ValueError("Invalid number of arguments for Vector3D")

        # generate a unique ID for each vector object using the counter
        self.id = Vector3D.counter
        # increment the counter by one
        Vector3D.counter += 1

    def __add__(self, other):  # vector addition

        if isinstance(other, Vector3D):  # check if other is a Vector3D object
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Cannot add a Vector3D with a non-Vector3D object")

    def __sub__(self, other):  # vector subtraction

        if isinstance(other, Vector3D):  # check if other is a Vector3D object
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Cannot subtract a non-Vector3D object from a Vector3D")

    def __repr__(self) -> str:  # represent function
        return f"Vector3D({self.x}, {self.y}, {self.z}, {self.alpha}) with ID:{self.id}"

    def __mul__(self, scalar):  # multiply with constant
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):  # divide by constant

        try:
            return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")

    def dot(self, other):  # dot product

        if isinstance(other, Vector3D):  # check if other is a Vector3D object
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Cannot compute the dot product of a Vector3D with a non-Vector3D object")

    def cross(self, other):  # cross product

        if isinstance(other, Vector3D):  # check if other is a Vector3D object
            return Vector3D(self.y * other.z - self.z * other.y,
                            self.z * other.x - self.x * other.z,
                            self.x * other.y - self.y * other.x)
        else:
            raise TypeError("Cannot compute the cross product of a Vector3D with a non-Vector3D object")

    def set_constant(self, constant):  # set constant vector method
        # set the x, y, and z attributes to the constant value
        self.x = constant
        self.y = constant
        self.z = constant

    def length(self):  # vector length method
        # calculate and return the magnitude of the vector
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):  # vector normalize method

        # calculate the length of the vector
        length = self.length()

        # check if the length is not zero, otherwise return None
        if length != 0:
            # create and return a new vector object with the same direction but unit length
            return Vector3D(self.x / length, self.y / length, self.z / length, self.alpha)

        else:
            return None


if __name__ == "__main__":
    vec1 = Vector3D()
    print(vec1)
