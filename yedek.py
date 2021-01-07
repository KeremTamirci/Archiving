import pandas
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

age_data = pandas.read_csv("By age.csv")
# print(age_data,"\n")

gender_data = pandas.read_csv("By gender.csv")
# print(gender_data)

while True:
  gender_input = input("Your gender?: ").strip()
  if gender_input.lower() == "male":
    gender_type = 1
    break
  elif gender_input.lower() == "female":
    gender_type = 0
    break
while True:
  age_input = input("Your age?: ").strip()
  if 18 <= int(age_input) <= 80:
    break



def find_genre():
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
            male_sayısı = round((sayı/2)*(male_rate)*10)
            female_sayısı = round((sayı/2)*(female_rate)*10)
            for s in range(male_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              age = int(random.randint(limits[0],limits[1]))
              # age = round(np.random.normal(((limits[0]+limits[1])//2),5))
              mak.write(f"1,{age},{genre}\n")
            for s in range(female_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              age = int(random.randint(limits[0],limits[1]))
              # age = round(np.random.normal(((limits[0]+limits[1])//2),5))
              mak.write(f"0,{age},{genre}\n")

# find_genre()
movie_data = pandas.read_csv("makine.txt")
y = movie_data["genre"]
X = movie_data.drop(columns=["genre"])

model = DecisionTreeClassifier()
model.fit(X, y)
a = model.predict([[gender_type, age_input]])[0]



# list_of_genres = []
# while True:
#   if a not in list_of_genres:
#     list_of_genres.append(a)
#   if len(list_of_genres) == 3:
#     break
# print(f"You can like these types of movies :\n{list_of_genres[0]},\n{list_of_genres[1]},\n{list_of_genres[2]}")

# a = find_genre()
print(a)


X_test, X_train, y_test, y_train = train_test_split(X, y, test_size= 0.8)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)


scorebetween0and1= accuracy_score(y_test, predictions)
print(scorebetween0and1)
