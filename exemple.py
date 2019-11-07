"""Exemple de résolution """

import numpy as np
import matplotlib.pyplot as plt


from pystrat.strategie import strategie

from pystrat.evaluate import evaluate_strategy


gen1 = evaluate_strategy(strategie, 50)
res1 = list(gen1)
res1.sort()
print(res1)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.bar(np.arange(len(res1)) + 0.4, res1, color="orange",
       label="strategie", width=0.4)
ax.set_title("Résultats de notre stratégie")
ax.legend()

plt.show()