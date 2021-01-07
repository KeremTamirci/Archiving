import pandas
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier

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
            male_sayısı = round((sayı/2)*(male_rate/100))
            female_sayısı = round((sayı/2)*(female_rate/100))
            for s in range(male_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              if limits[0] < int(age_input) < limits[1]:
                mak.write(f"1,{ages[k-1]},{genre}\n")
            for s in range(female_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              if limits[0] < int(age_input) < limits[1]:
                mak.write(f"1,{ages[k-1]},{genre}\n")


  movie_data = pandas.read_csv("makine.txt")
  y = movie_data["genre"]
  X = movie_data.drop(columns=["genre"])
  X = movie_data.drop(columns=["age"])
  model = DecisionTreeClassifier()
  model.fit(X, y)
  a = model.predict([[gender_type, age_input]])[0]
  return a


list_of_genres = []
while True:
  a = find_genre()
  if a not in list_of_genres:
    list_of_genres.append(a)
  if len(list_of_genres) == 3:
    break
print(f"You can like these types of movies :\n{list_of_genres[0]},\n{list_of_genres[1]},\n{list_of_genres[2]}")

# a = find_genre()
# print(a)
