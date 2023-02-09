# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    WELL_DONE = time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    MEDIUM = time * temperature * pressure * COOKED_CONSTANT >= MEDIUM
    if WELL_DONE:
        return True
    elif MEDIUM:
        return True
    else:
        return False
