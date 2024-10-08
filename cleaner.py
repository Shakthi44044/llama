#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[ ]:


import pandas as pd

# Load the CSV file
file_path = 'path_to_your_file/medicinenetscraped_data4.csv'
data = pd.read_csv(file_path)

# Apply forward-fill to propagate the last valid 'Title' for missing values
data_ffill = data.ffill()

# Save the cleaned data
cleaned_file_path = 'path_to_save/medicinenetscraped_data4_cleaned.csv'
data_ffill.to_csv(cleaned_file_path, index=False)

print("File cleaned and saved as:", cleaned_file_path)


# In[ ]:





# In[ ]:




