import pandas
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

with open("makine.txt","w") as mak:
    mak.write("gender,age,genre\n")
    with open("By age.csv","r") as age:
      with open("By gender.csv", "r") as gen:
        linesage = list(enumerate(age))
        linesgen = list(enumerate(gen))
        ages = (linesage[0][1].strip().split(","))[1:]
        gens = (linesgen[0][1].strip().split(","))[1:]
        # print(ages)
        # print(gens)
        for i in range(1,len(linesage)):
          elementsage = linesage[i][1].split(",")
          elementsgen = linesgen[i][1].split(",")
          female_rate = int(elementsgen[1])
          male_rate = int(elementsgen[2])
          genre = elementsage[0].lower()
          for k in range(1, len(elementsage)):
            sayı = int(elementsage[k])
            male_sayısı = round((sayı/2)*(male_rate/100))
            female_sayısı = round((sayı/2)*(female_rate/100))
            for s in range(male_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              age = int(random.gauss((limits[0]+limits[1]//2), 1))
              # age = round(np.random.normal(((limits[0]+limits[1])//2),5))
              mak.write(f"1,{age},{genre}\n")
            for s in range(female_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              age = int(random.gauss((limits[0]+limits[1]//2), 1))
              # age = round(np.random.normal(((limits[0]+limits[1])//2),5))
              mak.write(f"0,{age},{genre}\n")

movie_data = pandas.read_csv("makine.txt")
y = movie_data["genre"]
X = movie_data.drop(columns=["genre"])
X_test, X_train, y_test, y_train = train_test_split(X, y, test_size= 0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)


scorebetween0and1= accuracy_score(y_test, predictions)
print(scorebetween0and1)