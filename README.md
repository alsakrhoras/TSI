# The Space Invader
---


### Video Demo: https://youtu.be/ERAhUDj3VNQ
---
---
## **Description**
---
### Shoot them All type Game. With some changes it's like the arcad game "space invaders", This called The Space Invader, as some kind of indication that The Player is the one who invading the Space.
---
---
## modules used
---
 -   cx_freeze
 -   pygame

 ---
 ---
## Project Files
---
- **images (Folder)**: Contains The images used in the Game in bmp (for the exe file).
 - **tracks (Folder)**: Contains the Sound used in the Game.
 - ***project.py***: The Main File that will run The Space Invader Game
 - ***test_projest.py***: The Test file for the project
 - ***setup.py***: The File that will buil an exe or egg by Command (python setup.py build) in Windows or Linux. And will Build a Microsoft Installer by Command (python setup.py bdist_msi) or Linux Installer by Command (python setup.py bdist_wheel)
 - ***requirements.txt***: Containes the pip-installable libraries that the project required, can be installed by the Command (pip install -r requirements.txt).
 - ***README.md***: Contains Information about the Project.

---
---
## The Game
---
### Its a Keycoard GameThe Player moves by using the araws and shoot by Space the Player win if they reached Score of 150 and loses if his health doped beneath 0, The Game can be Paused by P Button, Closed by Q in addition to windows exiting methods. And The Game can be Replaied in the cases of win and loss by the R button.
### the Player can move in all direction and The game uses (the Open Window) if the player moved beyond the right of the screen they will appear at the left, beyond the top they will appear at the buttom and so on.
### The opponents (the Aliens) move in the X coordinate and when they reach its screen limit they drop on the Y coordinate. When the Shot or Wint beyond Screen Limit they Reappear again Randomly
### Player win if they shot 150 Alien, and losses if the health droped below 0, the health drop by colliding with the Aliens or if enough of them reached the screen buttom.
---
---
---
# Thank you Professor David and all CS50 Team, Thank you very much.







