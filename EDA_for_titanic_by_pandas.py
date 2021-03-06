#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.graphics.mosaicplot as stm


# In[ ]:





# In[9]:


titanic = pd.read_csv("C:/Users/chera/Desktop/train.csv")


# In[18]:


titanic.head(10) # шапка датафрейма с 10 первыми значениями и названия переменных. 


# In[33]:


titanic.info() # общая информация о типах данных, названии переменных и т.д. Переменные Ticket, Name, PassengerId - не содержат полезной информации и при дальнейшем анализе могут быть исключены из датафрейма.


# In[16]:


titanic.describe().T # оцениваем основные описательные характеристики; замечаем, что переменные: Pclass, SibSp, Parch, Survived - явно носят факторный характер (имеют несколько градаций).


# In[23]:


# для факторных и текстовых переменных оцениваем распределение
titanic["Sex"].value_counts()
# мужчин на борту было почти в два раза больше чем женщин


# In[29]:


titanic["Sex"].value_counts(normalize = True)


# In[30]:


titanic["Survived"].value_counts()


# In[31]:


titanic["Survived"].value_counts(normalize = True)
# большая часть пассажиров корабля погибло


# In[25]:


titanic["Parch"].value_counts() # содержит информацию о количестве детей/родителей у пассажира на борту судна


# In[26]:


titanic["SibSp"].value_counts() # содержит информацию о количестве братьев(сестёр)/супругов у пассажира на борту судна


# In[28]:


titanic["Pclass"].value_counts() # класс, в котором путешестовал пассажир


# In[32]:


titanic["Pclass"].value_counts(normalize = True)
# большая часть плыла третьим классом; остальные примерно пополам в первом или втором


# In[37]:


# Оцениваем содержание NaN в датафрейме
titanic.isnull().sum().sum()


# In[43]:


titanic.isnull().sum() # большая часть NaN приходится на переменную Cabin, поэтому в дальнейшем анализе её также можно исключить.


# In[81]:


titanic_mode = titanic.drop(columns = ["PassengerId", "Ticket", "Name", "Cabin"]) # удаляем переменные, которые не имеют рспределения и характеризуют индивидуальный объект
titanic_mode["dummy_sex"] = titanic_mode["Sex"].map({"female":0, "male":1})


# In[82]:


titanic_mode.hist(figsize = (8,10))


# In[77]:


titanic_mode["Sex"].hist()


# In[88]:


titanic_mode.corr().style.background_gradient(cmap = "coolwarm") # на графике корреляций видно, что переменная Survived более всего коррелирует с переменными Pclass и Sex. Переменная Age иммеет наибольшую корреляцию с Pclass и SibSp. Также наблюдается корреляция между Fare (транспортные расходы) и Pclass. Коэфициент корреляции для переменных SibSp и Parch тажке выше 0.4


# In[89]:


titanic_mode.pivot_table(values = ["Survived", "Age"], index=["Sex", "Pclass"], aggfunc = "mean")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




