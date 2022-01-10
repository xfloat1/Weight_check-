name1,name2,name3 = "Катя", "Лиза", "Влад"
sex1,sex2,sex3 = "woman","woman","man"
weight1,weight2,weight3 = float(70),float(70),float(70)
height1,height2,height3 = float(165),float(170),float(180)
def function_weight(name,weight,height,sex):
    
    result_weight = height-weight
    difference1 = result_weight - int(100) 
    difference2 = int(100) - result_weight
    
    
    if height <= 140 or weight <= 35:
        print("Вы ввели некорректные данные о росте или весе у пользователя " + name)
    else:
        if sex == "man":
            if result_weight > int(100):
                print(name + " ты не достиг нормы" + ", тебе нужно набрать еще " + str(round(difference1,2)) + " кг")
            if result_weight == int(100):
                print(name + " ты достиг нормы!")
            if result_weight < int(100):
                print(name + " ты набрал лишний вес" + ", тебе нужно скинуть " + str(round(difference2,2)) + " кг")
        if sex == "woman":
            if result_weight > int(100):
                print(name + " ты не достигла нормы" + ", тебе нужно набрать еще " + str(round(difference1,2)) + " кг")
            if result_weight == int(100):
                print(name + " ты достигла нормы!")
            if result_weight < int(100):
                print(name + " ты набрала лишний вес" + ", тебе нужно скинуть " + str(round(difference2,2)) + " кг")
        else:
            if sex != "man" and "woman":
                print("Вы ввели некорректные данные о поле пользователя " + name)
    
man1 = function_weight(name1,weight1,height1,sex1)
man2 = function_weight(name2,weight2,height2,sex2)
man3 = function_weight(name3,weight3,height3,sex3)
