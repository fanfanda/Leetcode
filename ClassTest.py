class Car:
    def __init__(self, brand):
        self.brand = brand

        if brand == 'BMW':
            self.max_speed = 180
        else:
            self.max_speed = 150

    def print_speed(self):
        print('The {} car\'s max speed is {}km/h.'.format(self.brand, self.max_speed))

ffd = Car('FFd') 
ffd.print_speed()
