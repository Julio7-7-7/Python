class fraccion 
  num=1
  den=1

  def __init__ (self, a,b):
      self.num = a
      self.den = b
    
  def set_num (self, a):
      self.num = a
  
  def set_den (self, b):
      self.den = b

  def get_num(self):
      return self.num

  def get_den(self):
      return self.den

aux = fraccion(18 ,54)
print (str(aux.get_num())+ "/" +str(aux.get_den()))
print("")
print("")

for i in range (2 , aux.get_den()):
    while ((aux.get_num()% i == 0) and (aux.get_den() % i == 0)):
        aux.set_num(aux.get_num() // i )
        aux.set_den(aux.get_den() // i )
    print(str(aux.get_num())+ "/" + str(aux.get_den()))
    
print (str(aux.get_num())+ "/" + str(aux.get_den()))