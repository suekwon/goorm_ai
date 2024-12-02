import matplotlib.pyplot as plt
import numpy as np

# Graph 1: Line Plot
plt.figure()
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('line_plot.png')

# Graph 2: Bar Chart
plt.figure()
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.savefig('bar_chart.png')

# Graph 3: Scatter Plot
plt.figure()
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('scatter_plot.png')
