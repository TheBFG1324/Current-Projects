#patient.py

class Patient:
    def __init__(self, _list):
        input_list=_list[1::]
        self.first_name=input_list[0]
        self.last_name=input_list[1]
        self.age=input_list[2]
        self.illness=input_list[3]
        self.serverity=input_list[4]
    
    def __lt__(self, other):
        if isinstance(other, Patient):
            return self.serverity<other.serverity
        else:
            raise IndexError("Invalid Type")
    def __gt__(self, other):
        if isinstance(other, Patient):
            return self.serverity>other.serverity
        else:
            raise IndexError("Invalid Type")
    
    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.serverity==other.serverity
        else:
            raise IndexError("Invalid Type")
    def __str__(self):
        return "name: "+self.first_name+" "+self.last_name+"\nAge: "+str(self.age)+"\nSuffers from: "+self.illness+"\nIllness Serverity: "+str(self.serverity)