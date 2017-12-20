class Math_dojo (object):
    def __init__(self, number, value_to_play_with):
        self.number = number
        self.value_to_play_with = value_to_play_with
    def add (self, number_parameter, value_to_play_with): 
        sum = 0
        for i in value_to_play_with:
            sum += i
        self.number = number_parameter + sum
        print self.number
    def subtract (self, number_parameter, dif_value_to_play_with):
        difference = 0
        for i in dif_value_to_play_with:
            difference -= i
        self.number = number_parameter - difference
        print self.number
         
big_boy = Math_dojo(3, [1, 4, 5, 33])
big_boy.add(8, [1, 4, 5, 33])
big_boy.subtract(3, [38, 3, 2, 22])


#work on part III of this jaunt