
import abc

class coe:
  def __init__(self,valor):
    self.soma=valor
  def fala(self):
    print("coé rapaziada",self.soma)



class Objeto(object):
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def fala(self):
    return

class Proxy(object):
  def __init__(self):
    self.objetoReal=ObjetoReal()

  def fala(self):
    self.objetoReal.fala()
class ObjetoReal(object):
  def fala(self):
    print("coé rapaziada funfou ")

class Client:
  # fazer 
  proxy = Proxy()


def main():
  client = Client()
  client.proxy.fala()

if __name__ == "__main__":
  main()


