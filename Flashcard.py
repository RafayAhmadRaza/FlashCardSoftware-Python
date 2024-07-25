#Flashcard Software Python By Rafay Ahmad Raza 
import numpy as np
import csv
import os
from pathlib import Path
def getCSVFiles():
    csvFiles=[]
    for filename in os.listdir(Path.cwd()):
        if filename.endswith('.csv'):
            csvFiles.append(os.path.join(Path.cwd(),filename))
    return csvFiles
    
class Card():
    def __init__(self,Question,Answer):
        self.Question = Question
        self.Answer = Answer

    def __repr__(self) -> str:
        return f"Question: {self.Question}, Answer:{self.Answer}"

class Deck():

    def __init__(self,name,DeckDict=None):
        self.name = name
        self.DeckDict=DeckDict if DeckDict is not None else {}

    def AddCard(self,card):
        if isinstance(card,Card):
            self.DeckDict[card.Question]  = card
        else:
            print("Invalid card. Must be an instance of card")

    def remove_card(self,question):

        if question in self.DeckDict:
            del self.DeckDict[question]
        else:
            print("Card not found in the deck")
    def getCard(self,question):
        return self.DeckDict.get(question,"Card not found")
    
    def displayDeck(self):
        if not self.DeckDict:
            print("The deck is empty")
        else:
            for card in self.DeckDict.values():
                print(card)

    def getAllCardList(self):
        cards=[]
        if not self.DeckDict:
            print("Deck is empty")
        else:
            for card in self.DeckDict.values():
              cards.append(card)
            return cards  
            
    def __repr__(self) -> str:
        return f"{self.name} Deck:" + ",".join(str(card) for card in self.DeckDict.values())
    
    
    def SaveDeckCSV(self):
        try:
            with open(f'{self.name}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Question','Answers'])
                for card in self.getAllCardList():
                    writer.writerow([card.Question, card.Answer])
            print(f"Deck saved to {self.name}.csv")
        except Exception as e:
            print(f"Error saving deck: {e}")

    def openDeckCSV():
        CSVFILES = getCSVFiles()

        rows= []
        try:
            for path in CSVFILES:
                with open(path,'r',newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        rows.append(row)
        except Exception as e:
            print(f"Error reading {path}: {e}")

        return rows

    def openDeck(name):
        deck_name= name+'.csv'

        if Path(deck_name).exists():
            deck = Deck(name)

            with open(deck_name,'r',newline='') as file:
                reader= csv.reader(file)
                for row in reader:
                    if row:
                        question,answer = row
                        card = Card(question,answer)
                        deck.AddCard(card)
            return deck
        else:
            print(f"No deck named{name}")
            return None


 
    

if __name__ == "__main__":

    print("Hello Welcome to my Flashcard Creator!")
    print("What do you want to do?")
    csvfiles = getCSVFiles()
    deckNames = [Path(csvF).name for csvF in csvfiles]
    print(deckNames)
    while True:

        choice=input("1-Create Deck 2- Add Cards to Existing Deck/s 3- Get All Cards in Deck 4- Del Card from a deck 5- exit\n")


        if choice == '1':
            Name = input("Enter the name of Deck: ")
            deck = Deck(name=Name)
            print("New deck added")
        elif choice == '2':
            Name = input('input deck name, write 0 if just created: ')

            if Name == '0':
                question = input("Enter your question: ")
                answer = input("Enter your answer: ")
                card = Card(question,answer)
                deck.AddCard(card)
                print("New card added")
            else:
                if Name+".csv" in deckNames:
                    deck = Deck.openDeck(name=Name)
                    if deck == None:
                        continue
                    question = input("Enter your question: ")
                    answer = input("Enter your answer: ")
                    card = Card(question,answer)
                    
                    deck.AddCard(card)
                    print("New card added")
            
            deck.SaveDeckCSV()
                    




            
        elif choice == '3':
            Name = input("Enter deckName: ")


            if Name in deckNames:
                try:
                    with open(Name,'r',newline='') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print(row)
                except Exception as e:
                    print(f"Error reading {Name}: {e}")

 
        elif choice == '4':
            question = input("Enter question to be deleted: ")
            deck.remove_card(question)


        elif choice == '5':
            deck.SaveDeckCSV()
            break    

        
    


           