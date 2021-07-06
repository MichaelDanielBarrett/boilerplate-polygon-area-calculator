class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        pic = ''
        if max(self.width, self.height) > 50:
            pic += 'Too big for picture.'
        else:
            for i in range(0, self.height):
                pic += f'{"*" * self.width}\n'
        return pic

    def get_amount_inside(self, other):
        return ((self.width // other.width) * (self.height // other.height))


class Square(Rectangle):

    def __init__(self, l):
        self.length = l
        self.width = l
        self.height = l

    def __repr__(self):
        return f'Square(side={self.length})'
        
    def set_side(self, l):
        self.length = l
        self.width = l
        self.height = l

    def set_width(self, l):
        self.set_side(l)

    def set_height(self, l):
        self.set_side(l)

    


