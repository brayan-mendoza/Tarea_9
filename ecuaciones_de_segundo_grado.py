#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Ecuaciones de segundo grado ax^2+bx+c")
a = int(input("introduce el valor del termino al cuadrado a : "))
b = int(input("introduce el valor de termino lineal b : "))
c = int(input("introduce el valor de termino independiente c : "))

print("la ecuacion quedo como : " + str(a) + "x^2 + " + str(b) +  "x + "  + str(c) +  " = 0 ")

if b*b > (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


if b**2 < (4*a*c):
    ei = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("El resultado tiene numeros complejos")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


# In[ ]:





# In[ ]:




