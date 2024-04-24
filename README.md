# Flashcards

This repo contains my implementation of project Flashcards from JetBrains Academy (https://hyperskill.org/projects/127)

### Usage

Flashscards allows to practice knowledge by learning ```definition``` of the ```term```. User will be asked to provide definitions of selected terms. 
For example, when learning translation from Polish to English, term would be word in Polish and definition its translation in English. Program also keeps track of mistakes made with any given term.

To run the program type ```python flashcards --import_from={filename} --export_to={filename}```, where ```--import_from``` (optional) allows to import flashcards from a file at the start of the program 
and ```--export_to``` (optional) allows to export flashcards to a file at the end of the program. Files follow the structure, where each flashcards takes 3 lines like this:  
```term```  
```definition```  
```mistakes count```  
 
At the start of the program user is prompted to select one of these options:
* ```add``` - manually add new flashcard
* ```remove``` - remove flashcard from the deck
* ```import``` - import additional cards from the file
* ```export``` - export cards to a file
* ```ask``` - ask for definitions of selected terms
* ```exit``` - exits program
* ```log``` - save content of the terminal to a file
* ```hardest card``` - provides information about the card for which user made the most mistakes
* ```reset stats``` - sets mistake count for all cards to 0
