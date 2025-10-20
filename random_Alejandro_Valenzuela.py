import random        #se importa la libreria random 
random_number = random.randint(1, 6) #modulo random elige un elemento random 

def get_random_dice_roll(): #Se define la funcion para recibir un numero al azar de un dado 
    #Returns a random integer from 1 to 6
      return random.randint(1,6)
print(get_random_dice_roll()) #imprime el numero random 4 veces 
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())