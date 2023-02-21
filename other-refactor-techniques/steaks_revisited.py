# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Meat:
    def __init__(self, time, temp, pressure, desired_state):
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * COOKED_CONSTANT

    def is_medium(self):
        if WELL_DONE > self.get_cooking_progress() >= MEDIUM:
            return 'medium'
        else:
            return -1

    def is_well_done(self):
        if self.get_cooking_progress() >= WELL_DONE:
            return 'well-done'
        else:
            return -1
            
    def cooked_criteria_satisfied(self):
        return self.is_well_done() == self.desired_state or self.is_medium() == self.desired_state

time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

meat = Meat(time, temp, pressure, desired_state)
print(meat.is_well_done(), '\n', meat.cooked_criteria_satisfied())