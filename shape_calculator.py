class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return '\n'.join(['*' * self.width for _ in range(self.height)]) + '\n'

    def get_amount_inside(self, quadrilateral):
        return self.height // quadrilateral.height * self.width // quadrilateral.width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = self.height = side
