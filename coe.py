
class coe:
  def __init__(self,valor):
    self.soma=valor
  def fala(self):
    print("coé rapaziada",self.soma)

class Objeto:
  def fala(self):
    pass
	
class Proxy(Objeto):
  def fala(self):
    objetoReal=ObjetoReal()
    objetoReal.fala()
	
class ObjetoReal(Objeto):
  def fala(self):
    print("coé rapaziada funfou ")

class Client:
  # fazer 
  proxy = Proxy()

def main():
  client = Client()
  client.proxy.fala()

if __name__ == "__main__" :
  main()

