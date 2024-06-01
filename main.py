import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import sympy as sp


def show_main_window():
    start_window.destroy()

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Calculateur de racines quadratiques")

    # Création des widgets
    label_a = tk.Label(root, text="a :")
    label_a.grid(row=0, column=0, padx=10, pady=10)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    label_b = tk.Label(root, text="b :")
    label_b.grid(row=1, column=0, padx=10, pady=10)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=10, pady=10)

    label_c = tk.Label(root, text="c :")
    label_c.grid(row=2, column=0, padx=10, pady=10)
    entry_c = tk.Entry(root)
    entry_c.grid(row=2, column=1, padx=10, pady=10)

    # Fonction de calcul
    import sympy as sp

    def calculate_roots():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            det = b ** 2 - 4 * a * c

            if det > 0:
                sqrt_det = math.sqrt(det)
                X1 = (-b + sqrt_det) / (2 * a)
                X2 = (-b - sqrt_det) / (2 * a)
                result = f"Les solutions sont X1 = {-b} + √{det} / {2 * a} et X2 = {-b} - √{det} / {2 * a}."
                messagebox.showinfo("Résultat", result)
            elif det == 0:
                X0 = -b / (2 * a)
                result = f"La solution unique est X0 = {X0}."
                messagebox.showinfo("Résultat", result)
            else:
                sqrt_det = math.sqrt(-det)
                X1_real = -b / (2 * a)
                X1_imag = sqrt_det / (2 * a)
                X2_real = -b / (2 * a)
                X2_imag = -sqrt_det / (2 * a)
                result = f"Les solutions sont X1 = {X1_real} + {X1_imag}i et X2 = {X2_real} + {X2_imag}i."
                messagebox.showinfo("Résultat", result)

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

            # Afficher le bouton "Reprendre"
        button_resume.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Fonction pour réinitialiser les entrées et cacher le bouton "Reprendre"

    def reset_inputs():
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        button_resume.grid_forget()

        # Création du bouton "Reprendre"

    button_resume = tk.Button(root, text="Reprendre", command=reset_inputs)

    button_calculate = tk.Button(root, text="Calculer", command=calculate_roots)
    button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Boucle principale
    root.mainloop()


# Création de la fenêtre de démarrage
start_window = tk.Tk()
start_window.title("Bienvenue")
start_window.geometry("600x400")
start_window.resizable(False, False)

# Chargement de l'image d'arrière-plan
image_path = "kunji_logo.png"  # Remplacer par le chemin de votre image
image = Image.open(image_path)
image = image.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionnement de l'image
background_image = ImageTk.PhotoImage(image)

# Création du canvas pour afficher l'image
canvas = tk.Canvas(start_window, width=600, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Ajout du label sur le canvas
start_label = tk.Label(start_window, text="Cliquez sur Lancer pour démarrer le programme", bg="white",
                       font=("Helvetica", 16))
canvas.create_window(300, 100, window=start_label)

# Ajout du bouton "Lancer" sur le canvas
start_button = tk.Button(start_window, text="Lancer", command=show_main_window, font=("Helvetica", 14))
canvas.create_window(300, 350, window=start_button)

# Boucle principale de la fenêtre de démarrage
start_window.mainloop()
