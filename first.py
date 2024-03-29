#%%
import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)  # Generate 100 points between -10 and 10
y = x**2  # Calculate y = x^2

plt.plot(x, y)  # Plot the graph
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x^2')
plt.grid(True)
plt.show()
# %%
