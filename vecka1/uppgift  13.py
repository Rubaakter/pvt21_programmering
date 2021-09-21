import random
dictionary = {"laddas ned till mobiltelefonen" : "beställas på posten",
              "finländare":"skåningar",
              "kommit nära":"chattat med",
              "coronaviruset":"vattkoppor",
              "Jag":"Du",
              "ni":"vi"}
mobiltelefonen = ["mobil","telephone","smartphone"]
finländare =["den från Finland", "finskarna"]
coronaviruset =["evil sjukdomen", "viruset"]
ni=["du", "vi","jag"]

mobiltelefonen = random.choice(mobiltelefonen)
finländare = random.choice(finländare)
coronaviruset = random.choice(coronaviruset)
ni = random.choice(ni)

print(f"""En app som kan laddas ned till {mobiltelefonen} ska varna {finländare} \n
som kommit nära någon som smittats med {coronaviruset}. \n
Jag tycker att {ni} i Sverige borde överväga att göra något as på posten""")









