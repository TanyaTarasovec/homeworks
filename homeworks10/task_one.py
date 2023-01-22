class Country:
    def __init__(self):
        pass


class Russia(Country):
    def __init__(self, Population_R):
        self._Population_R = Population_R


class Canada(Country):
    def __init__(self, Population_C):
        self._Population_C = Population_C


class Germany(Country):
    def __init__(self, Population_G):
        self._Population_G = Population_G


@property
def Population_R(self):
    return self._Population_R


@property
def Population_C(self):
    return self._Population_C


@property
def Population_G(self):
    return self._Population_G


@Population_R.setter
def Poputation_R(self, value):
    self._Population_R = value


@Population_C.setter
def Poputation_C(self, value):
    self._Population_C = value


@Population_G.setter
def Poputation_G(self, value):
    self._Population_G = value


R = Russia("Population of Russia - 144000000")
C = Canada("Population of Canada - 39000000")
G = Germany("Population of Germany - 83000000")

print(R._Population_R, C._Population_C, G._Population_G)
