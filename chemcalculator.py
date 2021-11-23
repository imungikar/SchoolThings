import numpy as np
def closest(lst, K):
      
     lst = np.asarray(lst)
     idx = (np.abs(lst - K)).argmin()
     return lst[idx]
precipitate = float(input("Mass of precipitate: "))
gramso = (precipitate / 233.38 * 96.06)
print("You have " + str(gramso) + " grams of SO4")
sample = float(input("Mass of sample: "))
percentmass = (gramso/sample*100)
print("Your percent mass is " + str(percentmass) + "%")

percentdict = {
  "Mg":79.8,
  "Al":84.2,
  "Na":67.6,
  "Ni":62,
  "K":55.1,
  "NH4":72.6,
  "Cd":46.1
}

values=percentdict.values()
listvalues=list(values)
closestdistance = closest(listvalues,percentmass)
myvalue = list(percentdict.keys())[list(percentdict.values()).index(closestdistance)]
print("Sample is closest to " + str(myvalue) + ".")