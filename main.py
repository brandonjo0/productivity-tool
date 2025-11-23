import tkinter as tk
from tkinter import filedialog, messagebox

from tools.pdf_reader import read_pdf
from ai.client import GeminiClient
import ai.prompts as prompts

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

def select_pdf(root):
    file_path = filedialog.askopenfilename(
        parent=root,
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        messagebox.showinfo("Cancelled", "No file selected.")
        return None

    return file_path

def get_user_choice():
    print("\nWhat would you like to do?")
    print("1. Summarize the PDF")
    print("2. Create Notes")
    print("3. Generate Study Schedule")
    print("4. Generate Flashcards")
    print("-. Select a different PDF")
    print("=. Exit")

    return input("\nEnter your choice: ")

def main():
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)

    print("\nSelect a PDF file...")
    pdf_path = select_pdf(root)

    print("\nSelected file:", pdf_path)

    print("\nExtracting text...")
    text = read_pdf(pdf_path)

    ai = GeminiClient()

    while True:
        choice = get_user_choice()

        if choice == "1":
            print("\n--- SUMMARY ---\n")
            print(ai.request(prompts.summary_prompt(text)))

        elif choice == "2":
            print("\n--- NOTES ---\n")
            print(ai.request(prompts.notes_prompt(text)))

        elif choice == "3":
            days = input("\nEnter the number of days required for the study schedule: ")

            print("\n--- STUDY SCHEDULE ---\n")
            print(ai.request(prompts.study_schedule_prompt(text, days)))

        elif choice == "4":
            print("\n--- FLASHCARDS ---\n")
            print(ai.request(prompts.flashcards_prompt(text)))

        elif choice == "-":
            print("\nSelect a new PDF file...")
            pdf_path = select_pdf(root)

            print("\nSelected file:", pdf_path)

            print("\nExtracting text...")
            text = read_pdf(pdf_path)

        elif choice == "=":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
