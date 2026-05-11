class Kitty:
  
  def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
    self.arm = arm_length
    self.leg = leg_length
    self.num = num_eyes
    self.tail = has_tail
    self.furry = is_furry
    
  def printKitty(self):
    print("Arm Length: " + str(self.arm) + " inches \nLeg Length: " + str(self.leg) 
      + " inches \nNumber of eyes: " + str(self.num))
    if self.tail:
      print("This animal has a tail.")
    else:
      print("This animal has no tail.")
      
    if self.furry:
      print("This animal is furry.")
    else:
      print("This animal is not furry.")
      

if __name__ == "__main__":
  k1 = Kitty(10.5, 11.2, 2, True, True)
  k1.printKitty()
