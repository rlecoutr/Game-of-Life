# Game-of-Life

This old project made for fun is based on the famous John Conway's game of life. You can find 2 .py files here : 

The first one, PtitScript.py, is the common game of life recreated, with a few features included.
The second one, Feu.py, is an adaptation of the game of life for the spread of a fire in a forest.

## Getting started

### Prerequisites

You will need a python compiler with tkinter included to run this project.
This project has been made for french users : Each button or indication in the programs will indeed be in french. Traductions will be done below.

### PtitScript.py

Once run, you will find a blank program with a little GUI on the bottom.

You can click anywhere on the canvas to create a cell (or to destroy it if the cell was already created).

The buttons "Départ" and "Arrêt" will respectively start and stop the evolution of the cells.
The button "Configuration notable" will set up the famous Gosper's glider Gun (once the "Départ" button clicked on)

You can set up the speed of the evolution (the delay between each step, in ms) with the "Vitesse (durée d'un tour)" line edit text (followed by Enter)

Finally, you can find the number of cells alive next to "Nombre de cellules vivantes".

### Feu.py

Once run, you will find this time a canvas already filled with green cells representating the trees of the forest (You can change the density of the forest in the code, which is currently 70% trees)

You can click anywhere on the canvas to create a fire cell.

The buttons "Départ" and "Arrêt" will respectively start and stop the evolution of the fire spreading.
The "Relancer" button will restart the program by drawing a new forest on the canvas.

You can set up the speed of the evolution (the delay between each step, in ms) with the "Vitesse de l'animation" line edit text (followed by Enter)
