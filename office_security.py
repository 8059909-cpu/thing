class DoorState:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False


class LightState:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


class Door:
    def __init__(self, door_id):
        self.door_id = door_id
        self.state = DoorState()

    def toggle(self):
        if self.state.is_open:
            self.state.close()
        else:
            self.state.open()


class Light:
    def __init__(self, light_id):
        self.light_id = light_id
        self.state = LightState()

    def toggle(self):
        if self.state.is_on:
            self.state.turn_off()
        else:
            self.state.turn_on()


class PowerManager:
    def __init__(self):
        self.power_consumed = 0

    def calculate_power(self, devices):
        for device in devices:
            if isinstance(device, Light) and device.state.is_on:
                self.power_consumed += 10  # Assume each light consumes 10W when on
            if isinstance(device, Door) and device.state.is_open:
                self.power_consumed += 5  # Assume open door consumes 5W

    def report_power_usage(self):
        return self.power_consumed


class OfficeSecuritySystem:
    def __init__(self):
        self.doors = []
        self.lights = []
        self.power_manager = PowerManager()

    def add_door(self, door):
        self.doors.append(door)

    def add_light(self, light):
        self.lights.append(light)

    def manage_security(self):
        self.power_manager.calculate_power(self.lights + self.doors)

    def handle_blackout(self):
        for door in self.doors:
            door.state.close()
        for light in self.lights:
            light.state.turn_off()

    def report_status(self):
        return {"doors": [door.state.is_open for door in self.doors], 
                "lights": [light.state.is_on for light in self.lights], 
                "power_usage": self.power_manager.report_power_usage()}