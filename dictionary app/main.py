import tkinter as tk
from ttkbootstrap import ttk
import requests


def get_data(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        definitions = []
        for word_meaning in meanings:
            definitions.append(
                f"PartOfSpeech: {word_meaning['partOfSpeech']}\n"
                f"Meaning : {word_meaning['definitions'][0]['definition']}\n")
        return "\n".join(definitions)
    return "Word not found."


def search():
    word = text_input.get()
    definition = get_data(word)
    text_output.configure(state="normal")
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, definition)
    text_output.configure(state="disabled")


screen = tk.Tk()
screen.title("dIc aPp")
screen.geometry("600x400")

# output_frame
output_frame = ttk.Frame(screen)
output_frame.pack(padx=20, pady=20)

# text_output
text_output = tk.Text(output_frame, state="disabled", height=10, font=("lato", 15))
text_output.pack()

# search frame
search_frame = ttk.Frame(screen)
search_frame.pack(padx=20, pady=10)

# search_bar
search_bar = ttk.Label(search_frame, text="Search word", font=("lato", 20, "bold"))
search_bar.grid(row=0, column=0, padx=5)

# text_input
text_input = ttk.Entry(search_frame, width=20)
text_input.grid(row=0, column=1, padx=5)

# search button
search_button = ttk.Button(search_frame, text="Search", width=15, command=search)
search_button.bind(<>, search)
search_button.grid(rows=2, columnspan=2, pady=20)

screen.mainloop()
