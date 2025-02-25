#Lab2
# Lab2: Write a Pandas program to create and display a DataFrame from a
# specified dictionary data which has the index labels.

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

#index labels
index_labels=[0,1,2,3,4,5,6,7,8,9]
#dictionary in dataframe with index labels
df=pd.DataFrame(exam_data,index=index_labels)
print("Data Frame with index labels:\n",df)