# skip this test if pandas is not installed
try:
    import pandas as pd
except:
    from nose.plugins.skip import Skip
    raise Skip

import matplotlib.pyplot as plt
import numpy as np
import mpld3

df2_index = pd.DatetimeIndex(start="2010-01-01", periods=100, freq='D')
df2 = pd.DataFrame({'a': range(100)}, index=df2_index)
ax = df2.plot(title="Datetime DF")

import sys
with file(sys.argv[0].replace('.py', '.html'), 'w') as f:
    mpld3.save_html(plt.gcf(), f)
