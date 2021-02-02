import matplotlib.pyplot as plt

data = {'Stati Uniti': 284000, 'Italia': 60606, 'Inghilterra': 53747, 'Francia': 55.521}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Morti coronavirus')


plt.show()
