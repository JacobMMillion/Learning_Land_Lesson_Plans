import random
import time

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "magenta", "teal"]
pattern = []

print("Select gamemode: normal, endless")

gamemode = input()

if gamemode == "normal" or gamemode == "Normal" or gamemode == "NORMAL":
    print("Gamemode: Normal")
else:
    print("Gamemode: Endless")