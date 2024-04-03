#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


df = sqlite3.connect('Rj_Assignment_1(sqlite3).db')
cursor=df.cursor()


# In[ ]:


cursor.execute('''create table Ages (name VARCHAR(128), age INTEGER)''')


# In[3]:


cursor.execute("select * from Ages")


# In[4]:


rows = cursor.fetchall()


# In[5]:


for row in rows:
    print(row)


# In[6]:


cursor.execute('''INSERT INTO Ages VALUES ('Mara', 28),
                 ('Otto', 33),
                 ('Fyn', 31),
                 ('Neshawn', 17);''')


# In[7]:


cursor.execute('''select * from Ages''')


# In[8]:


rows = cursor.fetchall()


# In[9]:


for row in rows:
    print(row)


# ### How to show all the table results in hex encoded value

# In[19]:


cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')


# In[20]:


rows = cursor.fetchall()


# In[21]:


for row in rows:
    print(row)


# ### HOw to print only first row

# In[13]:


cursor.execute('''select * from ages limit 1''')


# In[14]:


rows = cursor.fetchone()


# In[15]:


for row in rows:
    print(row)


# ### HOw to show only the first row in hex encoded value

# In[22]:


cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X limit 1''')


# In[23]:


rows = cursor.fetchall()


# In[24]:


for row in rows:
    print(row)


# ### How to create a virtual table and showing the hex encoded value only for first row

# In[25]:


cursor.execute('''create view vhex as SELECT hex(name || age) AS X FROM Ages ORDER BY X''')


# In[26]:


cursor.execute('''select * from vhex limit 1''')


# In[27]:


rows = cursor.fetchall()


# In[1]:


for row in rows:
    print(row)


# In[ ]:




