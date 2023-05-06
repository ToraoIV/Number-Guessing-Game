import random
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk


window = ctk.CTk()
window.title("Number Guessing Game")
window.geometry("400x400")
window.resizable(False, False)
difficulty = ""
text1 = ctk.StringVar(value="Number Guessing Game")
chances = ""
guess = ctk.IntVar(value= "0")
answer = random.randint(0,100)
uyari = ctk.StringVar()

def first_page():
      global difficulty, label_dif, button_easy, button_normal, button_hard
      label_dif = ctk.CTkLabel(window, text="Difficulty", font=("arial", 30, "bold"))
      button_easy = ctk.CTkButton(window, text="Easy", font=("arial", 20), command= lambda : (globals().update(difficulty="easy"), main()))
      button_normal = ctk.CTkButton(window, text="Normal", font=("arial", 20), command= lambda : (globals().update(difficulty="normal"), main()))
      button_hard = ctk.CTkButton(window, text="Hard", font=("arial", 20), command= lambda : (globals().update(difficulty="hard"), main()))
      label_dif.pack(pady=20)
      button_easy.pack(ipadx=40, ipady=20, pady=(20, 15))
      button_normal.pack(ipadx=40, ipady=20, pady=15)
      button_hard.pack(ipadx=40, ipady=20, pady=15)

def main():
      global text1, color, chances, guess, label_info, check_button, number_box, hak_label, frame1, button_back,button_reset
      label_dif.pack_forget()
      button_easy.pack_forget()
      button_normal.pack_forget()
      button_hard.pack_forget()

      if difficulty == "easy":
            chances = 15
      elif difficulty == "normal":
            chances = 10
      elif difficulty == "hard":
            chances = 5

      uyari.set(f"Remaining {chances} guesses")

      label_info = ctk.CTkLabel(window, textvariable = text1,text_color= "#0492C2", font=("arial", 30, "bold"))
      label_info.pack(pady=(50, 10))

      number_box = ttk.Spinbox(window, from_=0, to=100,textvariable=guess,justify='center', wrap=True, font=("arial", 30, "bold"), width=2)
      number_box.pack(pady=15, ipady=15, ipadx=15)

      hak_label = ctk.CTkLabel(window, textvariable = uyari)
      hak_label.pack()

      check_button = ctk.CTkButton(window, text="Check",state="normal", command= check)
      check_button.pack(pady=15)

      frame1 = ctk.CTkFrame(window)
      frame1.pack(pady=20)

      button_back= ctk.CTkButton(frame1, text="back", command=back)
      button_back.pack(side = tk.LEFT, padx=5)
      button_reset= ctk.CTkButton(frame1, text="reset", command=reset)
      button_reset.pack(side = tk.LEFT,padx=5)

def check():
      global chances
      guess1 = guess.get()
      print(answer)
      chances -= 1

      uyari.set(f"Remaining {chances} guesses")
      if answer == guess1:
            print("Correct!")
            text1.set("Correct!")
            label_info.configure(text_color = "green")
            check_button.configure(state = "disabled")
      elif answer > guess1:
            print("too low!")
            text1.set("too low!")
            label_info.configure(text_color="yellow")
      elif answer < guess1:
            print("too high!")
            text1.set("too high!")
            label_info.configure(text_color="yellow")
      if chances == 0:
            print("You lost!")
            text1.set("You lost!")
            label_info.configure(text_color="red")
            check_button.configure(state="disabled")

def reset():
      global chances, answer, guess

      if difficulty == "easy":
            chances = 15
      elif difficulty == "normal":
            chances = 10
      elif difficulty == "hard":
            chances = 5

      uyari.set(f"Remaining {chances} guesses")
      answer = random.randint(0, 100)
      text1.set("Everything is reset!")
      label_info.configure(text_color="#0492C2")
      check_button.configure(state="normal")
      guess = ctk.IntVar(value="0")

def back():
      global guess, text1
      guess = ctk.IntVar(value= "0")
      label_info.pack_forget()
      number_box.pack_forget()
      hak_label.pack_forget()
      check_button.pack_forget()
      frame1.pack_forget()
      button_back.pack_forget()
      button_reset.pack_forget()
      first_page()
      reset()
      text1 = ctk.StringVar(value="Number Guessing Game")


first_page()

window.mainloop()
