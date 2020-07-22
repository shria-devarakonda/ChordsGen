import random

def generate():    
    
    majors = ["A", "B", "C", "D", "E", "F", "G"]
    minors = ["Am", "Bm", "Cm", "Dm", "Em", "Fm", "Gm"]
    subject =["Love", "Death", "Loneliness", "Power", "Alcohol", "Enemy", "Coronavirus", "Beauty"]
    print(majors[random.randint(0,6)])
    print(minors[random.randint(0,6)])

    print(majors[random.randint(0,6)])
    print(minors[random.randint(0,6)])

    print("Sing about", subject[random.randint(0,8)])

generate()


