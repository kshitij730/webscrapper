#!/usr/bin/env python
# coding: utf-8

# In[88]:


import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging


# In[89]:


flipkart_url = "https://www.flipkart.com/search?q=" + "redmi"


# In[90]:


flipkart_url


# In[91]:


urlclient = urlopen(flipkart_url)


# In[92]:


urlclient


# In[93]:


flipkart_page = urlclient.read()


# In[94]:


flipkart_html = bs(flipkart_page,'html.parser')


# In[95]:


"https://www.flipkart.com/"+"apple-iphone-12-pro-silver-256-gb/p/itm41ac927e82906?pid=MOBFWBYZMZTJZTWK&lid=LSTMOBFWBYZMZTJZTWKASW35U&marketplace=FLIPKART&q=iphone12pro&store=tyy%2F4io&srno=s_1_1&otracker=search&fm=organic&iid=71960d02-a964-48b3-a5a4-69d714b4acde.MOBFWBYZMZTJZTWK.SEARCH&ppt=None&ppn=None&ssid=48dzb19y0g0000001693656063493&qH=712933e6bd68e7b9"


# In[96]:


bigbox = flipkart_html.findAll("div" , {"class" : "_1AtVbE col-12-12"})


# In[97]:


len(bigbox)


# In[98]:


del bigbox[0:3]


# In[99]:


product_link = "https://www.flipkart.com"+bigbox[4].div.div.div.a['href']


# In[100]:


product_req = requests.get(product_link)


# In[101]:


product_link


# In[102]:


product_html = bs(product_req.text,'html.parser')


# In[103]:


comment_box = product_html.findAll("div",{"class" : "_16PBlm"})


# In[104]:


len(comment_box)


# In[105]:


for i in comment_box:
    print(i.div.div.findAll("p",{"class" : "_2sc7ZR _2V5EHH"})[0].text)


# In[106]:


for i in comment_box:
    print(i.div.div.div.div.text)


# In[107]:


for i in comment_box:
    print(i.div.div.div.p.text)


# In[108]:


for i in comment_box:
    print(i.div.div.findAll("div",{"class" : ''})[0].div.text)


# In[ ]:





# In[109]:


for i in bigbox:
    print("https://www.flipkart.com"+i.div.div.div.a['href'])


# In[ ]:




