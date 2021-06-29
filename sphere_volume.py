import math

pi = math.pi #Число Пи. Примерно, равное 3.141592653589793

def calculate_sphere_volume(r):
    try:
        x = int(r)
        if r >= 0:
            return 4/3*pi*r**3
        else:
            return 'Радиус сферы не может быть отрицательным'
    except ValueError:
        return r


print(calculate_sphere_volume('for'))
