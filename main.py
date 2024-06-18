import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

replacement = {
    'robot': 1,
    'human': 2
}

data['whoAmI'] = data['whoAmI'].replace(replacement)

data['is_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 1 else 0)
data['is_human'] = data['whoAmI'].apply(lambda x: 1 if x == 2 else 0)

data.drop('whoAmI', axis=1, inplace=True)

print(data)