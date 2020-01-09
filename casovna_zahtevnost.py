import matplotlib.pyplot as mpl

x = [5, 10, 20, 30, 50, 80, 100, 200, 300, 500]
y1 = [0.000675, 0.004748, 0.03257, 0.10143, 0.69378, 4.97926, 11.3602,
      194.093, 1127.92, 7912.40]
y2 = [0.000276, 0.000600, 0.00801, 0.01806, 0.18529, 0.534838, 1.97813,
      22.9016, 162.040, 402.52]
y3 = [0.000154, 0.000611, 0.01151, 0.04639, 0.30218, 1.38603, 2.31723,
      13.7700, 94.0348, 496.36]

mpl.plot(x,y1,c='r',label='2-opt')
mpl.plot(x,y2,c='g',label='3-opt')
mpl.plot(x,y3,c='b',label='LK')
 
mpl.title("Časovna zahtevnost v praksi")
mpl.xlabel("n")
mpl.ylabel("Čas [s]")

mpl.ylim(0, 10000)
 
mpl.legend()
mpl.show()

x = [5, 10, 20, 30, 50, 80, 100]
y1 = [0.000675, 0.004748, 0.03257, 0.10143, 0.69378, 4.97926, 11.3602]
y2 = [0.000276, 0.000600, 0.00801, 0.01806, 0.18529, 0.534838, 1.97813]
y3 = [0.000154, 0.000611, 0.01151, 0.04639, 0.30218, 1.38603, 2.31723]

mpl.plot(x,y1,c='r',label='2-opt')
mpl.plot(x,y2,c='g',label='3-opt')
mpl.plot(x,y3,c='b',label='LK')
 
mpl.title("Časovna zahtevnost v praksi")
mpl.xlabel("n")
mpl.ylabel("Čas [s]")

mpl.ylim(0, 12)
 
mpl.legend()
mpl.show()
