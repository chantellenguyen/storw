import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.title("chantelle's sanrio store")
root.geometry("350x350")
total = 0
money = 99999

def update_total(cost):
  global total, money
  cost_int = int(cost.strip("$"))
  if money >= cost_int:
      total += cost_int
      money -= cost_int
      cost_output.config(text=f"Total cost: ${total}")
      wallet_balance.config(text=f"Wallet balance: ${money}")
  else:
      cost_output.config(text="Not enough money!")

# Images and costs
items = [{"image": "chantelle1.png", "cost": "$3500 "},
         {"image": "chantelle2.png", "cost": "$20758"},
         {"image": "chantelle3.png", "cost": "$8000"}]
title_label= tk.Label(root, text= "chantelle sanrio store",font=("Helvitica, 17"))
title_label.pack(pady=5)

#Create a frame to put the pictures of items in
frame = tk.Frame(root)
frame.pack()

for item in items:
  item_frame = tk.Frame(frame)
  item_frame.pack(side=tk.LEFT)

  # Open and resize the image
  img = Image.open(item["image"])
  img = img.resize((100, 100))
  img = ImageTk.PhotoImage(img)
  img_label = tk.Label(item_frame, image=img)
  img_label.image = img
  img_label.pack()

  # Add cost below each image
  cost_label = tk.Label(item_frame, text="Cost: " + item["cost"])
  cost_label.pack()

  # Add a Buy button
  buy_button = tk.Button(item_frame, text="Buy This Now", command=lambda cost=item["cost"]: update_total(cost))
  buy_button.pack()


cost_output = tk.Label(root, text="")
cost_output.pack(pady=40)

wallet_balance = tk.Label(root, text=f"Wallet balance: ${money}")
wallet_balance.pack()







#Run application
root.mainloop()
