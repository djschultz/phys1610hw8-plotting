import numpy as np
import matplotlib.pyplot as plt


cores = np.linspace(1,16,16)
diffusion1d = np.array([123, 133, 102, 110, 118, 128, 146, 159, 159, 170, 179, 184, 210, 221, 227, 253])
diffring = np.array([538, 361, 278, 230, 198, 182, 161, 143, 131, 121, 113, 112, 108, 102, 97, 91])

a = 600
b = 60

plt.plot(cores, diffusion1d)
plt.plot(cores, diffring)
plt.plot(cores, a*np.reciprocal(cores) + b)
plt.xlabel("number of cores")
plt.ylabel("runtime (seconds)")
plt.legend(["diffusion1d", "diffring", "diffring fit"])
plt.savefig("runtimes.pdf")
