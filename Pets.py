class Pet:
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = ''

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = input('Enter the pet\'s name: ')
    age = input('Enter the pet\'s age:' )
    animal = input('Enter the type of animal of your pet: ')
    users_pet = Pet()
    users_pet.set_name(name)
    users_pet.set_age(age)
    users_pet.set_animal_type(animal)
    print('The pet\'s name is', users_pet.get_name(), 'and is a', users_pet.get_animal_type(), 'and is', users_pet.get_age(), 'years old.')

main()