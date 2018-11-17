import matplotlib.pyplot as plt

x_values = list(range(1, 501))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues,edgecolor='none', s=40)
plt.title('Number Cube',fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()