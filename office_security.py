# Office Security System for FNAF 2 Fan Game

class OfficeSecurity:
    def __init__(self):
        self.doors_locked = False
        self.lights_on = True
        self.energy_consumed = 0

    def lock_doors(self):
        self.doors_locked = True
        print("Doors are locked.")

    def unlock_doors(self):
        self.doors_locked = False
        print("Doors are unlocked.")

    def toggle_lights(self):
        self.lights_on = not self.lights_on
        state = "on" if self.lights_on else "off"
        print(f"Lights are now {state}.")

    def consume_energy(self, amount):
        self.energy_consumed += amount
        print(f"Energy consumed: {self.energy_consumed} units.")

    def get_status(self):
        return {
            "doors_locked": self.doors_locked,
            "lights_on": self.lights_on,
            "energy_consumed": self.energy_consumed,
        }