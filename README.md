# Dice set comparator for Savage Worlds RPG system
This project is a dice set comparator. It allows user to input any two
sets of dice and compare them for average roll result. It uses
'exploading dice' rules for rolling dice.

## Launching
To launch this program you'll need:
*  Python 3
*  Libraries: tkinter, matplotlib, pubsub, random, numpy

Clone this repository and run *controller.py* file.

## Interface
![Image](https://i.imgur.com/fFkyAfx.png)

* Compare!: Opens compare window with average results of two given set
* +: Adds new die to the set
* -: Removes die from the set
* Number of sides: Choose between 4, 6, 8, 10 or 12 - sided dice
* Modifier: Type in flat number added to the roll

## Use example
Let's say we want to check which weapon is better, a gunpowder rifle or
magic dagger.  
Rifle deals 2d6 (two 6-sided dies) + 1 damage and has 2 additional
damage from bonuses.  
Magic dagger deals (d8 - 3) + (2d4 +1). We enter our sets as seen below:

![Image](https://i.imgur.com/VAf0k1H.png)

After clicking "Compare!" we see new window with our results:

![Image](https://i.imgur.com/fE5FR8r.png)

We can deduct that Set A is better with 11.5 average roll. Set B has
only 9.7 average roll.

**Warning!** This program uses Exploading Dice rules. It means that
whenever die rolls maximum another roll is made and added to the result.
This is not suitable for comparing dice for other systems such as
Dungeons and Dragons or Pathfinder.
