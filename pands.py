import pandas as pd
s1 = pd.Series([10,20,30,40,50])
print(s1)

s2 = pd.Series([10,20,30,40,50],index=["a","b","c","d","e"])
print(s2)

d1 = {"k1":10,"k2":20,"k3":30,"k4":40,"k5":50}
s3 = pd.Series(d1)
print(s3)

#DataFrame
dict1 = {"NAME":["Tanu","Chinu","Bhanu"],"MARKS":[70,80,90]}
d1 = pd.DataFrame(dict1)
print(d1)

iris = pd.read_csv("C:\\Users\\deepa\\Downloads\\iris.csv")
p1 = iris.head()
print(p1)
print(iris.head(100))

p2 = iris.tail()
print(p2)
print(iris.tail(10))

p3 = iris.describe()
print(p3)

i1 = iris.iloc[91:101,2:4]
print(i1)
i2 = iris.iloc[11:21,[0,4]]
print(i2)

i3 = iris.loc[31:41,("Sepal.Length","Sepal.Width")]
print(i3)

a = iris["Sepal.Length"]>5
print(a)
b = iris[iris["Sepal.Length"]>5]
print(b)
c= iris[(iris["Petal.Length"]<2) & (iris["Species"]=="setosa")]
print(c)



