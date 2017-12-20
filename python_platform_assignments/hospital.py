class Patient(object):
    def __init__(self, id, name, allergies, bed_number):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

class Hospital (object):
    def __init__(self, patients, name, capacity):
        self.patients = patients 
        self.name = name
        self.capacity = capacity

    def admit(self):
        if Hospital.patients < capacity:
            patients += Patient()
            Patient.bed_number = 77
            print "patient successfully added"
        else:
            return "Sorry, hospital is full"

    def discharge(self, find_this_guy):
        dude = patients.find(find_this_guy)
        patients.pop(dude)
        patients(dude).bed_number = 0
        print patients.dude()

#fix bugs in this crap and check if it actually works