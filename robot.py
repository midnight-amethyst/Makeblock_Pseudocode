class Motor:
    def __init__(self, motorname):
        self.motorName = motorname

    def run(self, speed):
        print(f"{self.motorName} rotating at {speed}")

    def stop(self):
        print(f"Stopped rotating {self.motorName}")


class Sensor:
    def __init__(self):
        self.distance = None

    def measure_distance(self):
        pass