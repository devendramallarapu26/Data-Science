import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [i ** 2 for i in x]
plt.title("Power graph")
plt.xticks([1,2,3,4])
plt.yticks([1,2,3,4,5,6,7,8])
plt.ylabel("power")
plt.xlabel("unit")
colors = ['red','orange']
plt.bar(x,y,color=colors)
plt.show()
