# Unterschied Instanz-Members und statische Members
# Erstellt: 27/10/20

class Test:

  def Allgemein():
      print("*** Eine statische Methode ***")
      
    
  def __init__(self):
      pass
      
  def Speziell(self):
      print("*** Eine Instanzen-Methode ***")
      Test.Allgemein()
      
      
t1 = Test()
t1.Speziell()
 
Test.Allgemein()