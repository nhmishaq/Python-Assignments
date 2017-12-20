class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_of_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_of_call = reason_of_call
    
    def display (self):
        print "Unique ID: " + str(self.unique_id) + "Caller Name: " + str(self.caller_name) + "Caller Phone Number: " + str(self.caller_phone_number) + "Time Of Call: " + str(self.time_of_call) + "reason_of_call: " + str(self.reason_of_call)
    
class Call_center(Call):
    def __init__(self, calls, queue_size):
        self.calls = calls
        self.queue_size = queue_size    
    
    def add(self, caller_to_add):
        self.append(caller_to_add)
        print self.unique_id

angry_caller = Call (3433, "Grumpy Grandpa", 2401113333, 2322, "pissed off about service")

angry_caller.add()
print angry_caller

#check if this crap works plus work on call_center class