import tkinter as tk
from tkinter import ttk, messagebox
import heapq

# ===========================
# DATA GRAPH
# ===========================

graph = {
    "Tangerang": {"Jakarta": 20, "Serang": 30},
    "Jakarta": {"Tangerang": 20, "Bekasi": 15, "Depok": 18},
    "Bekasi": {"Jakarta": 15, "Cikarang": 20},
    "Depok": {"Jakarta": 18, "Bandung": 40},
    "Serang": {"Tangerang": 30, "Bandung": 35},
    "Bandung": {"Serang": 35, "Depok": 40, "Cikarang": 10},
    "Cikarang": {"Bekasi": 20, "Bandung": 10}
}

# ===========================
# ALGORITMA DIJKSTRA
# ===========================

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        jarak, kota, path = heapq.heappop(queue)

        if kota in visited:
            continue

        visited.add(kota)
        path = path + [kota]

        if kota == end:
            return jarak, path

        for tetangga, bobot in graph[kota].items():
            if tetangga not in visited:
                heapq.heappush(queue, (jarak + bobot, tetangga, path))

    return None

# ===========================
# FUNGSI GUI
# ===========================

def cari_rute():

    asal = combo_asal.get()
    tujuan = combo_tujuan.get()

    hasil = dijkstra(graph, asal, tujuan)

    if hasil:
        jarak = hasil[0]
        rute = hasil[1]
        biaya = jarak * 2500

        hasil_label.config(
            text=
            f"Rute : {' -> '.join(rute)}\n"
            f"Jarak : {jarak} KM\n"
            f"Biaya : Rp{biaya:,.0f}"
        )

    else:
        messagebox.showinfo("Info", "Rute tidak ditemukan")

# ===========================
# GUI
# ===========================

root = tk.Tk()
root.title("Sistem Rute Pengiriman")
root.geometry("500x350")

judul = tk.Label(
    root,
    text="SISTEM RUTE PENGIRIMAN BARANG",
    font=("Arial", 16, "bold")
)
judul.pack(pady=10)

tk.Label(root, text="Kota Asal").pack()

combo_asal = ttk.Combobox(root, values=list(graph.keys()))
combo_asal.pack()

tk.Label(root, text="Kota Tujuan").pack()

combo_tujuan = ttk.Combobox(root, values=list(graph.keys()))
combo_tujuan.pack()

btn = tk.Button(
    root,
    text="Cari Rute",
    command=cari_rute,
    bg="lightblue",
    font=("Arial", 11)
)
btn.pack(pady=10)

hasil_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="left"
)
hasil_label.pack()

root.mainloop()