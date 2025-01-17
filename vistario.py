import psutil
import tkinter as tk
from tkinter import ttk
import time
import threading

class Vistario:
    def __init__(self, root):
        self.root = root
        self.root.title("Vistario - System Monitor")
        self.root.geometry("300x200")

        self.cpu_label = ttk.Label(root, text="CPU Usage: 0%")
        self.cpu_label.pack(pady=10)

        self.memory_label = ttk.Label(root, text="Memory Usage: 0%")
        self.memory_label.pack(pady=10)

        self.progress_cpu = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progress_cpu.pack(pady=5)

        self.progress_memory = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progress_memory.pack(pady=5)

        self.update_stats()

    def update_stats(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

        self.progress_cpu['value'] = cpu_usage
        self.progress_memory['value'] = memory_usage

        # Update the stats every second
        self.root.after(1000, self.update_stats)

def main():
    root = tk.Tk()
    app = Vistario(root)
    root.mainloop()

if __name__ == "__main__":
    main()