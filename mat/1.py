import matplotlib.pyplot as plt

x=[10,20,30,40]
y=[100,200,300,400]
plt.plot(x,y,color="blue",marker="o")
plt.savefig("plot.png",dpi=3000)
plt.show()