class motor():
    def __init__(self, motorName):
        self.motorName = motorName

    def run(self, speed):
        print(f"{self.motorName} rotating at {speed}")

    def stop(self):
        print(f"Stopped rotating {self.motorName}")

