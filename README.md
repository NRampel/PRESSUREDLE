![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Spotipy](https://img.shields.io/badge/Spotipy-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![HTML](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)


# Pressuredle (WIP) 



Welcome to **Pressuredle**, a browser game similar to Wordle that was based on PRESSURE, a Roblox Survival-Horror Game


## 📜 Credits:
* **PRESSURE** was created, designed and programmed by Zeal and his developer team
* **WORDLE** was created by Josh Wardle and the New York Times

## 📖 Project Description: 
* **Pressuredle** will select a random monster/entity fom **PRESSURE**
* Will prompt the user to guess what monster it picked.
* The number of guesses is determined by the use.
* If the user runs out of guesses, then the user loses the game.
* If the user successfully guesses the monster, then the user wins the game. 

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask, Pandas, Spotipy, Pillow
* **Data:** Custom CSV datasets for the monsters and their information

## 🎮 How to Play: 
1. Enter your difficulty in the difficulty bar (or don't)
2. Enter your guess in the guessing bar, game will provide feedback:
   * **🟩 Green** Indicates correctness
   * **🟥 Red** Indicates incorrectness
   * **⬆️⬇️ Arrows** (Coming Soon) Indicates how incorrect you are for the numerical traits 
3. To navigate through the site, click on the links above the difficulty bar

## ⚡ Key Features: 
* **Data Driven Logic:** Uses **Pandas** to efficiently compare monster stats from a custom datasheet
* **Immersive Audio:** Uses **Spotipy** to play random songs from PRESSURE's ost
* **Dynamic Web Server:** Built on **Flask** to handle game state adequately
* **CI/CD Pipeline:** Uses a workspace to automatically lint code and test the game engine and spotify server on every commit

## 🚀 Installation & Setup: 
### To run this game on your local machine, follow the steps below: 
1. **Download The Latest Release:**
   * Click the zip with the source code
   * Unzip the zip file
   * Using powershell or command prompt, cd over to the folder
2. **Create and Activate a Virtual Environment**
     * **Windows:** python -m venv venv  (if the former executed) venv\Scripts\activate
     * **Mac/Linux:** python3 -m venv venv (if the former executed) source venv/bin/activate
3. **Install Dependancies:**
     * **pip install -r requirements.txt**
4. **Run the Application:**
     * Type: flask run
     * Open your browser to 'http://127.0.0.1:5000' to play!
  
## ⬆️ Future Updates: 
* Configuring Images so people can see the monster the game selected
* Configuring Spotify so that music will play from the webpage
* Ability to turn off music if the user desires 
     
   



