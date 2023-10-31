# Standard python libs
import importlib 
import subprocess
import tkinter as tk
import json
import webbrowser
import time
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
installedlibs = False # Please change it to True later!
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
required_libraries = ['pyautoit', 'keyboard', 'discord-webhook', 'pypresence', "opencv-python", 'pyautogui', 'pillow']

missing_libraries = []
if installedlibs == False:

    for library in required_libraries:
     try:
        importlib.import_module(library)
     except ImportError:
        missing_libraries.append(library)

if missing_libraries:
    print("Installing needed libraries...")
    for library in missing_libraries:
        subprocess.check_call(['pip', 'install', library])
else:
    print("All required libraries are already installed.")

# Required imports
import autoit
import keyboard as key
from discord_webhook import DiscordWebhook, DiscordEmbed
from pypresence import Presence
import pyautogui



root = tk.Tk()

# Set the appearance to dark mode
root.configure(bg='black')
root.tk_setPalette(background='black', foreground='white')


# Variables for the settings
Viplink = tk.StringVar()
LoadingWaitTime = tk.IntVar()
webhooklink = tk.StringVar()
client_id = tk.StringVar()
MainUnitSlot = tk.StringVar()
discordid = tk.StringVar()

# Function to load settings from the JSON file
def load_settings():
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
            Viplink.set(settings.get("Viplink", ""))
            LoadingWaitTime.set(settings.get("LoadingWaitTime", 0))
            webhooklink.set(settings.get("webhooklink", ""))
            client_id.set(settings.get("client_id", ""))
            MainUnitSlot.set(settings.get("MainUnitSlot", ""))
            discordid.set(settings.get("discordid", ""))
    except FileNotFoundError:
        pass


# Function to save settings to the JSON file
def submit():
    global Viplink, LoadingWaitTime, webhooklink, client_id, MainUnitSlot, discordid
    Viplink = entry_viplink.get()
    LoadingWaitTime = int(entry_loadingtime.get())
    webhooklink = entry_webhooklink.get()
    client_id = entry_clientid.get()
    MainUnitSlot = entry_mainunitslot.get()
    discordid = entry_discordid.get()
    
    # Save the settings to a JSON file
    settings = {
        "Viplink": Viplink,
        "LoadingWaitTime": LoadingWaitTime,
        "webhooklink": webhooklink,
        "client_id": client_id,
        "MainUnitSlot": MainUnitSlot,
        "discordid": discordid
    }
    
    with open("settings.json", "w") as file:
        json.dump(settings, file)
    
    root.destroy()

# Load settings from the JSON file
load_settings()

# Create labels and entry fields for the settings
label_viplink = tk.Label(root, text="Viplink:", bg="black", fg="white")
label_viplink.pack()
entry_viplink = tk.Entry(root, textvariable=Viplink, bg="black", fg="white")
entry_viplink.pack()

label_loadingtime = tk.Label(root, text="Loading Wait Time:", bg="black", fg="white")
label_loadingtime.pack()
entry_loadingtime = tk.Entry(root, textvariable=LoadingWaitTime, bg="black", fg="white")
entry_loadingtime.pack()

label_webhooklink = tk.Label(root, text="Webhook Link:", bg="black", fg="white")
label_webhooklink.pack()
entry_webhooklink = tk.Entry(root, textvariable=webhooklink, bg="black", fg="white")
entry_webhooklink.pack()

label_clientid = tk.Label(root, text="Client ID:", bg="black", fg="white")
label_clientid.pack()
entry_clientid = tk.Entry(root, textvariable=client_id, bg="black", fg="white")
entry_clientid.pack()

label_mainunitslot = tk.Label(root, text="Main Unit Slot:", bg="black", fg="white")
label_mainunitslot.pack()
entry_mainunitslot = tk.Entry(root, textvariable=MainUnitSlot, bg="black", fg="white")
entry_mainunitslot.pack()

label_discordid = tk.Label(root, text="Discord ID:", bg="black", fg="white")
label_discordid.pack()
entry_discordid = tk.Entry(root, textvariable=discordid, bg="black", fg="white")
entry_discordid.pack()

# Function to get ability to move the window
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

# Bind the function to the title bar
root.overrideredirect(True)
root.title("Settings")
root.bind('<B1-Motion>', move_window)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit, bg="black", fg="white")
submit_button.pack()

root.mainloop()


'''
Other functions
'''

# Variables :hotfurrypic:
TotalRounds = 0
TotalGems = 0

RPC = Presence(client_id)
RPC.connect()


def StartingRPC():
    RPC.update(state="Hi this is Ada's AA Macro and it's currently starting")
    
def UpdateRPC():
    RPC.update(state=f"Ada's Marine Macro wave 25, total rounds : {TotalRounds} gems: {TotalGems}", details="Currently macroing Anime Adventures")


def Webhook(description):
    webhook = DiscordWebhook(url=webhooklink)
    embed = DiscordEmbed(description=description)
    webhook.add_embed(embed)
    webhook.execute()
    
def send_disconnected_message(webhooklink, discordid, description=str):
    webhook = DiscordWebhook(url=webhooklink)
    message = f"<@{discordid}>"
    webhook.content = message
    embed = DiscordEmbed(color=0xFF0000)  # Red color
    embed.description = description
    webhook.add_embed(embed)
    webhook.execute()

    
def UpdateTotal():
    global TotalRounds, TotalGems
    TotalRounds += 1
    TotalGems += 100
    
    
    
'''
Lobby Functions
'''
    
    
def JoinVip():
    StartingRPC()
    Webhook("Hello and thank you for using Ada's Marine w25 macro!")
    webbrowser.open(Viplink)
    playbutton = pyautogui.locateOnScreen('Play.png', confidence=0.5)
    while True:
        time.sleep(1)
        Webhook(description="Joining Vip Server")
        time.sleep(LoadingWaitTime)
        if playbutton is not None:
            print("I can see it")
            Webhook(description="Going to Portal")
            autoit.mouse_click("left", x=157, y=482) # Play
            time.sleep(1)
            key.press("w")
            key.press("d")
            key.press("space")
            time.sleep(10) # can do longer if ur internet slow
            key.release("w")
            key.release("d")
            key.release("space")
            break
        else: 
            send_disconnected_message(webhooklink=webhooklink, discordid=discordid, description="Yo bro before u go to sleep or outside check ur PC and restart macro, i think roblox failed starting lmao.")
            continue
        
    

def ChoosingMapAndStarting():
    Webhook("Choosing map and starting.")
    autoit.mouse_click("left", x=1738, y=754) # Marine
    time.sleep(1)
    autoit.mouse_click("left", x=1142, y=813) # Friends only
    time.sleep(1)
    autoit.mouse_click("left", x=960, y=813) # Select
    time.sleep(1)
    autoit.mouse_click("left", x=955, y=782) # Start
    Webhook("Joining game")
    
    
    
'''
Game Functions
'''
def CheckIfDisconnected():
    disconnectedimg = pyautogui.locateOnScreen('Disconnected.png', confidence=0.6)
    if disconnectedimg is not None:
        send_disconnected_message(webhooklink=webhooklink, discordid=discordid, description="Disconnected in game because of tp fail or internet, restarting.")
        LobbyMacro()
    
    
def CheckIfJoinedGame():
    votebutton = None
    while votebutton is None:
        CheckIfDisconnected()
        time.sleep(3)
        votebutton = pyautogui.locateOnScreen('Vote.png', confidence=0.7)
        print("I can see vote button.")
    autoit.mouse_click("left", x=921, y=174) # Start game (yes button)

'''
def CheckIfWave20OrHigher():
    Wave = None
    while Wave is None:               
        time.sleep(3)
        Wave = pyautogui.locateOnScreen("Wave24.png", confidence=0.7, region=(474, 36, 250, 85))                    hai!!! it's not needed!!!!
        print("I can see +-Wave 24")
'''

def Restart():
        autoit.mouse_click("left", x=765, y=720) # Next button
        autoit.mouse_click("left", x=769, y=720) # 1
        autoit.mouse_click("left", x=766, y=720) # -  Clicking 3 times to claim rewards (aka fruits idk)
        time.sleep(1)
        autoit.mouse_click("left", x=767, y=720) # 3
        autoit.mouse_click("left", x=1108, y=218) # Replay button

def CheckIfLostBecauseOfRng():  # Don't worry, it usually happens at wave 7 because of leak at start (low chance) so that's why i created it.
    NextButtton = pyautogui.locateOnScreen('Lost.png', confidence=0.7)
    if NextButtton is not None:
        Webhook("Died because of rng at start, restarting")
        Restart()
        GameMacro()
        
def CheckIfLost():
    NextButton = None
    while NextButton is None:
        time.sleep(3)
        NextButton = pyautogui.locateOnScreen("Lost.png", confidence=0.7)


    
def ClickOnSlot():
    key.press(MainUnitSlot)
    key.release(MainUnitSlot)
    
        
        
def PlaceFirstAndSecondTowers():
    Webhook("Placing first and second units - Poseidon")
    ClickOnSlot()
    autoit.mouse_click("left", x=1274, y=859)
    ClickOnSlot()
    autoit.mouse_click("left", x=1442, y=861)
    
    
def ClickOnFirst():
    autoit.mouse_click("left", x=1274, y=859)
def ClickOnSecond():
    autoit.mouse_click("left", x=1442, y=861)
def ClickOnThird():
    autoit.mouse_click("left", x=1595, y=856)
    
    
def UpgradeUnit():
    autoit.mouse_click("left", x=418, y=650) 
def SellUnit():
    autoit.mouse_click("left", x=209, y=657) 
    
    
'''
Main Macro starts here!!!!!
'''

def LobbyMacro():
    JoinVip()
    ChoosingMapAndStarting()
    GameMacro()
    
    
def GameMacro():
    while True:
        Webhook("Discord Rich Presence updated.")
        UpdateRPC()
        # autoit.mouse_click("left", x=921, y=174) # Start game (yes button)
        CheckIfJoinedGame()
        Webhook("Image detection(Vote button) pressed  yes.")
        time.sleep(15) 
        PlaceFirstAndSecondTowers()
        Webhook("Placing 2 Poseidons.")
        time.sleep(30)
        ClickOnSlot()
        autoit.mouse_click("left", x=1595, y=856) # third tower
        Webhook("Placing third Poseidon, max limit reached.")
        time.sleep(30)
        ClickOnFirst()
        UpgradeUnit()
        UpgradeUnit()
        UpgradeUnit()
        Webhook("Upgraded Pos #1 to lvl 3.")
        time.sleep(40)
        ClickOnSecond()
        UpgradeUnit()
        UpgradeUnit()
        Webhook("Upgraded Pos #2 to lvl 2.")
        time.sleep(30)
        UpgradeUnit()
        ClickOnThird()
        UpgradeUnit()
        UpgradeUnit()
        time.sleep(10)
        UpgradeUnit()
        Webhook("Upgraded Pos #2 to lvl 3, Pos #3 is lvl 3.")
        time.sleep(20)
        for i in range(1,540):
            seconds = 0
            if seconds < i: 
                seconds += 1
                CheckIfLostBecauseOfRng() # Don't worry, it usually happens at wave 7 because of leak at start (low chance) so that's why i created it.
        SellUnit()
        ClickOnSecond()
        SellUnit()
        ClickOnFirst()
        SellUnit()
        CheckIfLost()
        Webhook("Lose gui detected, restarting")
        UpdateTotal()
        Webhook(f"Round completed. Total Rounds: {TotalRounds}, gems: {TotalGems}")
        Restart()
        
        
# Start..
LobbyMacro()

# I probably should've used OOP but lazy to rewrite everything now. - ada, 21.10.2023 (DD.MM.YYYY) 
