#pet shop application
#this will be like a mini inventory system

# import
# class
#     --add
#     --remove
#     --save
#     --load
#     Main
#     Test


#import
import json
import os.path

class Inventory:
    pets = {}

    def __init__(self):
        self.load()
        pass

    def add(self,key,qty):
        q = 0 # q for short version of quantity
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: total = {self.pets[key]}')


    def remove(self,key,qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'removed {qty} {key}: total = {self.pets[key]}')



    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')



    def save(self):
        print('Saving Inventory...')
        with open('Inventory.txt','w') as f:
            json.dump(self.pets,f)
        print('Saved')


    def load(self):
        print('Loading Inventory...')

        if not os.path.exists('Inventory.txt'): #checking to see if Inventory.txt is in the current file directory
            print("Skipping, nothing to load")
            return
        with open('Inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded!')


def main():
    inv = Inventory()

    while True:
        decision = input('Actions: add, remove, list, save, exit:')
        if decision == 'exit':
            break

        if decision == 'list':
            inv.display()

        if decision == 'save':
            inv.save()

        if decision == 'add' or 'remove':
            key = input('Enter the animal: ')
            qty = int(input('Enter the qty: '))

            if decision == 'add':
                inv.add(key,qty)
            if decision == 'remove':
                inv.remove(key,qty)


        if decision == 'exit':
            break

    inv.save()

#exit

if __name__ == "__main__":
    main()

# andy = {"name":"Andy","color":"red"}
# for key,values in andy.items():
#     print(f'{key} = {values}')
