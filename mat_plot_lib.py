from matplotlib import pyplot as plt
import  numpy as np

#Lineplot
x = np.arange(1,11)
print(x)
y = 2*x
print(y)
z= 4*x
print(z)
plt.plot(x,y,color= "purple",linewidth=3,linestyle="--")
plt.plot(x,z,color="yellow",linewidth=3,linestyle=":")
plt.title("Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
print(plt.show())

#Barplot
students = {"Tanu":10,"Bhanu":20,"Chinu":30}
Names = list(students.keys())
Marks = list(students.values())
plt.bar(Names,Marks,color="red")
plt.title("Marks of Students")
plt.xlabel("Name")
plt.ylabel("Scores")
plt.grid(True)
print(plt.show())
# If we use plt.barh , then we get horizontal graph instead of vertical

#Scatter-plot
a = [2,6,7,9,3,0,3]
b = [7,4,10,4,1,6,3]
c = [0,9,8,7,6,5,4]
plt.scatter(a,b)
plt.scatter(a,c,color="yellow")
plt.grid(True)
print(plt.show())

#Histograms
import pandas as pd
iris = pd.read_csv("iris.csv")
print(iris.head())
plt.hist(iris["Sepal.Length"],bins=25)
print(plt.show())

#boxplots
iris.boxplot(column="Petal.Length",by="Species")
print(plt.show())

import  seaborn as sns
sns.boxplot(x = iris["Species"],y = iris["Petal.Width"])
plt.show()

#Piechart
fruits = ["apple","banana","guava","grapes"]
cost = [40,60,80,100]
plt.figure(figsize=(8,8))
plt.pie(cost,labels=fruits,autopct="%0.1f%%",shadow=True)
plt.show()



