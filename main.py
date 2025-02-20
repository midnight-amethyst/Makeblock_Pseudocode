class motor():
    def __init__(self, motorName):
        self.motorName = motorName

    def run(self, speed):
        print(f"{self.motorName} rotating at {speed}")

    def stop(self):
        print(f"Stopped rotating {self.motorName}")


motor1 = motor('motor1')
motor2 = motor('motor2')
motorArm = motor('Arm')

while true