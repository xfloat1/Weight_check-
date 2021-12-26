#!/usr/bin/env python
# coding: utf-8

# In[3]:


name = "Коля"
sex = "man"
weight = float(78)
height = float(180)
HW = height - weight - int(100)
WH = int(100) - (height - weight)

if height <= 140 or weight <= 35:
    print("возникла ошибка, сделайте скриншот сайта и вышлите нам на почту pochta@mail.com")
else:
    if sex == "woman" and height - weight > int(100):
        print(name + " ты не достигла нормы" + ", тебе нужно набрать еще " + str(round(HW,2)) + " кг")
    if sex == "man" and height - weight > int(100):
        print(name + " ты не достиг нормы" + ", тебе нужно набрать еще " + str(round(HW,2)) + " кг")
    if sex == "woman" and height - weight == int(100):
        print(name + " ты достигла нормы!")
    if sex == "man" and height - weight == int(100):
        print(name + " ты достиг нормы!")
    if sex == "woman" and height - weight < int(100):
        print(name + " ты набрала лишний вес" + ", тебе нужно скинуть " + str(round(WH,2))+ " кг")
    if sex == "man" and height - weight < int(100):
        print(name + " ты набрал лишний вес" + ", тебе нужно скинуть " + str(round(WH,2))+ " кг")

