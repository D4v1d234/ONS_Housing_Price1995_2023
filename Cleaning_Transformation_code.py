
# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import cumsum
from math import pi


# In[2]:


# File location
df = pd.read_csv(r'C:\Users\ddiol\OneDrive\Python\Project\Housing\UK_Property.csv')
df.head()


# In[3]:


# Define the new column names
column_names = ['Transaction_unique_identifier', 'Price', 'Date_of_Transfer', 'Postcode', 'Property_Type', 'Old/New', 'Duration', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District', 'County', 'PPDCategory_Type', 'Record_Status - monthly_file_only']

# Rename the columns
df.columns = column_names


# In[4]:


# Drop missing values in 'Postcode' column
df = df.dropna(subset=['Postcode']).reset_index(drop=True)

# Fill missing values in 'SAON', 'Street', and 'Locality' columns using .loc
df.loc[:, 'SAON'] = df['SAON'].fillna('Unknown')
df.loc[:, 'Street'] = df['Street'].fillna('Unknown')
df.loc[:, 'Locality'] = df['Locality'].fillna('Unknown')


# In[5]:


# Convert 'Date_of_Transfer' to datetime
df['Date_of_Transfer'] = pd.to_datetime(df['Date_of_Transfer'])


# In[6]:


# Extract date components
df['date'] = df['Date_of_Transfer'].dt.date
df['day'] = df['Date_of_Transfer'].dt.day
df['month'] = df['Date_of_Transfer'].dt.month
df['year'] = df['Date_of_Transfer'].dt.year


# In[7]:
# Calculate count of entries per county
county_count = df['county'].value_counts().reset_index()
county_count.columns = ['county', 'count']

# Define regions
england = ['BEDFORDSHIRE', 'DEVON', 'HEREFORDSHIRE', 'NORTHAMPTONSHIRE', 'SURREY', 'BERKSHIRE', 'DORSET', 'HERTFORDSHIRE', 'NORTHUMBERLAND', 'TYNE AND WEAR', 'BRISTOL', 'COUNTY DURHAM', 'ISLE OF WIGHT', 'NOTTINGHAMSHIRE', 'WARWICKSHIRE', 'BUCKINGHAMSHIRE', 'EAST RIDING OF YORKSHIRE', 'KENT', 'OXFORDSHIRE', 'WEST MIDLANDS', 'CAMBRIDGESHIRE', 'EAST SUSSEX', 'LANCASHIRE', 'RUTLAND', 'WEST SUSSEX', 'CHESHIRE', 'ESSEX', 'LEICESTERSHIRE', 'SHROPSHIRE', 'WEST YORKSHIRE', 'CITY OF LONDON', 'GLOUCESTERSHIRE', 'LINCOLNSHIRE', 'SOMERSET', 'WILTSHIRE', 'CORNWALL', 'GREATER LONDON', 'MERSEYSIDE', 'SOUTH YORKSHIRE', 'WORCESTERSHIRE', 'CUMBRIA', 'GREATER MANCHESTER', 'NORFOLK', 'STAFFORDSHIRE', 'DERBYSHIRE', 'HAMPSHIRE', 'NORTH YORKSHIRE', 'SUFFOLK']
wales = ['ISLE OF ANGLESEY', 'GWYNEDD', 'CONWY', 'DENBIGHSHIRE', 'FLINTSHIRE', 'WREXHAM', 'CEREDIGION', 'POWYS', 'PEMBROKESHIRE', 'CARMARTHENSHIRE', 'SWANSEA', 'NEATH PORT TALBOT', 'BRIDGEND', 'VALE OF GLAMORGAN', 'RHONDDA CYNON TAFF', 'CARDIFF', 'MERTHYR TYDFIL', 'CAERPHILLY', 'NEWPORT', 'TORFAEN', 'BLAENAU GWENT', 'MONMOUTHSHIRE']

wales_data = df[df['County'].str.strip().isin(wales)]
england_data = df[df['County'].str.strip().isin(england)]


# In[8]:


# Define the new property type mapping
property_type_mapping = {
    'O': 'Other',
    'F': 'Flat/Maisonette',
    'D': 'Detached',
    'S': 'Semi-detached',
    'T': 'Terraced'
}

# Update the 'Property_Type' column using the mapping
df['Property_Type'] = df['Property_Type'].map(property_type_mapping)

# Display the first few rows to verify the changes
df.head()


# In[9]:


# Rename entries in 'Old/New' column
df['Old/New'] = df['Old/New'].map({'N': 'New', 'Y': 'Old'})


# In[10]:


# Combine address components
df['Full_Address'] = df[['PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District', 'County', 'Postcode']].astype(str).apply(', '.join, axis=1)







# In[ ]:





# In[ ]:





# In[ ]:




