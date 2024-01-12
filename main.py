import matplotlib.pyplot as plt
import numpy as np

sizes = np.array([1, 2, 3, 4, 5])
times = sizes * 2 

plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o')
plt.title('kouritu')
plt.xlabel('size')
plt.ylabel('time')
plt.grid(True)
plt.show()
