# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
    def find_speed(self, time):
        if self.unit != 'km':
            if self.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
                # convert from light-year to km unit
                in_km = self.value * 9.461e12
                distance = Distance(in_km, "km")
            else:
                print ("unit is Unknown")
                return
        speed = distance.value/time # [km per sec]
        return speed

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    def find_mass(self):
        if self.unit != 'kg':
            if self.unit == "solar-mass":
                # convert from solar mass to kg
                value = self.value * 1.98892e30 # [kg]
                mass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return
        return mass.value

def calculate_kinetic_energy(found_mass, found_speed):
    kinetic_energy = 0.5 * found_mass * found_speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
found_mass = mass.find_mass()
distance = Distance(2, 'ly')
found_speed = distance.find_speed(3600e20)
print(calculate_kinetic_energy(found_mass, found_speed))
