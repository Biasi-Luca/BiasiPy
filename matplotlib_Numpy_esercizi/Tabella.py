
import matplotlib.pyplot as plt

data = {'3-5 anni': 19.9, '6-10 anni': 47.2, '11-14 anni': 74.3, '15-17 anni': 83.2, '18-19 anni': 79.3, '20-24 anni': 80.3, '25-34 anni': 74, '35-44 anni': 69.1, '45-54 anni': 66.5, '55-59 anni' : 56.1, '60-64 anni': 49, '65-74 anni': 29.6, '75 anni e più': 8.9}
names = list(data.keys())
values = list(data.values())

plt.scatter(values, names)

plt.show()