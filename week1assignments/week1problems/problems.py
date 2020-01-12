#this is 1-1
from functions.functions import song_info2
from functions.functions import song_create

playlist  = []
while True:

    song_name = input("Enter Song name: ")
    artist_name = input("Enter artist name: ")
    playlist.append(song_info2(song_name, artist_name))

    if artist_name == 'q' or song_name == 'q':
        print("Quitting")
        break
    
song_create(playlist)
 
#this is 1-2
import functions.namefunction

name = input("what is your name? ")
age = input("what is your age? ")

functions.namefunction.some_func(name,age)

#this is 1-3
from classes.shirtclass import shirt

my_shirt = shirt("L", "Black")
print("My shirt size is: " + my_shirt.size)
print("My shirt color is: " + my_shirt.color)

my_shirt.shirtInfo()


my_other_shirt = shirt("XL" , "White")
print("My other shirt size is: " + my_other_shirt.size)
print("My other shirt color is: " + my_other_shirt.color)

my_other_shirt.shirtInfo()

#this is 1-4
from classes.clothing import Clothing
from classes.shirtinherit import ShirtInherit

my_other_new_shirt = ShirtInherit("XL", "Blue", 2, "Long Sleeves", "American Eagle")
my_other_new_shirt.quantityIncrease(4)
print("Other New Shirt Quantity: "+ str(my_other_new_shirt.quantity))
my_other_new_shirt.printMessage()