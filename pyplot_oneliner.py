import matplotlib.pyplot as plt

periodic_cycle = [60,70,80,90,45,60,21,89,102,56]

expected_cycles = periodic_cycle[1:-2] * 10

plt.plot(expected_cycles)

plt.show()

