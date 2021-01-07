import pandas
import random
from sklearn.tree import DecisionTreeClassifier

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


def create_data():
  """Verilen tablolara göre kullanıcı bilgileri oluşturur."""
  with open("makine.txt","w") as mak:
    mak.write("gender,age,genre\n")
    with open("By age.csv","r") as age:
      with open("By gender.csv", "r") as gen:
        linesage = list(enumerate(age))
        linesgen = list(enumerate(gen))
        ages = (linesage[0][1].strip().split(","))[1:]
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
              mak.write(f"1,{age},{genre}\n")
            for s in range(female_sayısı):
              limits = []
              rang = ages[k-1].split("-")
              for i in rang:
                limits.append(int(i))
              age = int(random.randint(limits[0],limits[1]))
              mak.write(f"0,{age},{genre}\n")


# create_data()
movie_data = pandas.read_csv("makine.txt")
y = movie_data["genre"]
X = movie_data.drop(columns=["genre"])

model = DecisionTreeClassifier()
model.fit(X, y)
a = model.predict([[gender_type, age_input]])[0]
print(a)
