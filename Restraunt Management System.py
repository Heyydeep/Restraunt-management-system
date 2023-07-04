#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Club:
    def restraunts(rp):
        print("\t\t\t\t Club")
        print("\t\t\t\t\t\t Since-1990")
        print("Menu")
        
    def food(rp):
        x=["Indian","German","Korean"]
        for k in x:
            print(k)
            
    def German(rp):
        x=["Beef","Knuckle","Roll"]
        y=[450,320,890]
        german_={"German food types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(German)
        print("German foods")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("enter the value position"))
            c=int(input("enter the quantity"))
            z=german_["price"][b]
            
            y=z*c
            
            d.append(y)
            x=input("you want to reorder (yes/no)")
            if(x=="no"):
                print("thank you")
                break
                
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("service tax = 5%")
        print("total amount",t,"rupees")
        print("total amount after tax",t,"rupees")
        
    def Korean(rp):
        x=["Kimchi","Bulgogi","Fried chicken"]
        y=[850,520,440]
        Korean_={"Korean food types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(Korean)
        print("Korean foods")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("enter the value position"))
            c=int(input("enter the quantity"))
            z=Korean_["price"][b]
            
            y=z*c
            
            d.append(y)
            x=input("you want to reorder (yes/no)")
            if(x=="no"):
                print("thank you")
                break
                
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("service tax = 5%")
        print("total amount",t,"rupees")
        print("total amount after tax",t,"rupees")
        
    def Indian(rp):
        x=["Daal bhati","Lasagnia","Sushi"]
        y=[321,777,690]
        Indian_={"Indian food types":x,"Price":y}
        import pandas as pd
        df=pd.DataFrame(Indian_)
        print("Indian foods")
        print(df)
        d=[]
        while x:
            x=True
            b=int(input("enter the value position"))
            c=int(input("enter the quantity"))
            z=Indian_["Price"][b]
            
            y=z*c
            
            d.append(y)
            x=input("you want to reorder (yes/no)")
            if(x=="no"):
                print("thank you")
                break
                
        t=sum(d)
        m=(sum(d)*0.05)
        k=t+m
        print("service tax = 5%")
        print("total amount",t,"rupees")
        print("total amount after tax",t,"rupees")


# In[2]:


obj=Club()
obj.restraunts()
obj.food()


# In[4]:


x=input()
if x=="indian":
    print(obj.Indian())
elif x=="German":
    print(obj.German())
else:
    print(obj.Korean())


# In[ ]:




