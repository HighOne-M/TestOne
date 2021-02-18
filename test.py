
hilf = "Dilara ist sehr klein"




class Zwerg:
    def __init__(self, p_name):
        self.name = p_name
    def pd(self):
        for i in range(21):
           print(hilf[i])

dilara = Zwerg("Dilara")
dilara.pd()