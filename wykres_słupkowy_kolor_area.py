import matplotlib.pyplot as plt

x = ['green', 'yellow', 'blue', 'pink']
y = [123, 56, 34.5, 90]

fig, ax = plt.subplots()

ax.bar(x, y, label='Area')

ax.set_xlabel('color')
ax.set_ylabel('area')
ax.set_title('Color area')

ax.legend()

ax.grid(True, axis='x', linestyle='--', alpha=0.7)

# Wyłącz ticki na obu osiach
ax.tick_params(axis='x', which='both', bottom=False, top=False)
ax.tick_params(axis='y', which='both', left=False, right=False)

plt.tight_layout()

plt.show()
