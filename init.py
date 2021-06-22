class computer:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu

    def config(self):
        print("SYSTEM",self.cpu,self.ram)

com1 = computer("bg,ram")
com2 = computer("dell,500gb")

com1.config()
com2.config()
