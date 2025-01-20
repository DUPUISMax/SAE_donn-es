import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 3, 5]
y2 = [1, 3, 5, 2, 4]

plt.plot(x, y1, label='Courbe 1', color='blue', linestyle='-')
plt.plot(x, y2, label='Courbe 2', color='red', linestyle='--')

plt.title('Graphique avec plusieurs courbes')
plt.xlabel('Axe des x')
plt.ylabel('Axe des y')
plt.legend()

plt.show()