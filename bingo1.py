import tkinter as tk
import random

class BingoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ビンゴの司会システム")
        self.used_numbers = set()  # 引かれた数字を記憶
        self.history = []  # 引かれた数字の履歴

        # ラベルとボタンの作成
        self.display_label = tk.Label(master, text="", font=("Helvetica", 48), bg="lightblue")
        self.display_label.pack(pady=20)

        self.history_label = tk.Label(master, text="引かれた数字の履歴: ", font=("Helvetica", 14))
        self.history_label.pack(pady=20)

        tk.Button(master, text="数字を引く", command=self.draw_number, font=("Helvetica", 24)).pack(pady=20)

    def draw_number(self):
        if len(self.used_numbers) < 75:
            number = random.randint(1, 75)
            while number in self.used_numbers:
                number = random.randint(1, 75)

            self.used_numbers.add(number)
            self.history.append(number)
            self.display_label.config(text=str(number), bg=self.get_random_color())
            self.update_history()
        else:
            self.display_label.config(text="すべての数字が引かれました！", bg="red")

    def update_history(self):
        self.history_label.config(text="引かれた数字の履歴: " + ", ".join(map(str, self.history)))

    def get_random_color(self):
        return f'#{random.randint(0, 0xFFFFFF):06x}'

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
