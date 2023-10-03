sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
print(subtotal_to_total)

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel", "Sofia"] ,"geografia":"estefania","notas": [ "3", "5"]}
print(students_in_classes)


""" Diccionario Vacio """
animals_in_zoo={}
print(animals_in_zoo)
animals_in_zoo["Lions"] = 24
print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "sing "}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

postres = ["cake", "muffin", "cheescake"]
Calorias = ["45", "60", "120"]
zipped_postres =zip(postres, Calorias)
postres_to_calorias={key:value for key, value in zipped_postres}
print(postres_to_calorias)
               