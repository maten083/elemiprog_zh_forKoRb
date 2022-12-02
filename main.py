#1.feladat - importoltuk a szarokat, és numpy syntaxát alkalmaztuk
import math
import matplotlib.pyplot as plt
import numpy as np
#itt deklaráljuk hogy mit akarunk beolvasni, illetve hagyunk-e ki sort
ascii_grid = np.loadtxt("hill3.asc",skiprows=6)
#Ha textként loadolva lett a szöveg akkor plotba vele, majd a mathplot kiírja
plt.plot(ascii_grid)
#plt.show()  --->eddig tartott az 1.feladat

#2.feladat: numpy syntax [row, column] aztán x:y a range

cut = ascii_grid[:,90:270]
plt.plot(cut)
plt.show()
#3.feladat - ez rák
#itt az alap tárolt raszert deklaráltuk egy újként
#szintén numpy syntax: raster(raster > adott pixel) = érték (pl float('nan'))
newraster = np.array(ascii_grid);
newraster[newraster > 200] = float('nan')
plt.plot(newraster)
plt.show()
