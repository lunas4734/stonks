#example plot that safes a figure to jped

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.close('all')

ts = pd.Series(np.random.randn(500), index = pd.date_range ('1/2/2020', periods = 500))

ts = ts.cumsum()

ts.plot()

plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()