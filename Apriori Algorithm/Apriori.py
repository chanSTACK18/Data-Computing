
import numpy as np
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_excel('Online_Retail.xlsx')
data.head()