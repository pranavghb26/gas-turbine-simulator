import tkinter as tk
from tkinter import ttk, filedialog
from main import run_simulation

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv


# -----------------------------
# SIMULATION UPDATE (REAL-TIME)
# -----------------------------
def update_simulation(event=None):
    T1 = 288
    P1 = 101325

    comp_eff = comp_slider.get()
    turb_eff = turb_slider.get()
    mode = mode_var.get()

    ratios = list(range(2, 25))
    thrust_values = []
    eff_values = []

    for r in ratios:
        result = run_simulation(T1, P1, r, comp_eff, turb_eff)

        thrust_values.append(result["thrust"])
        eff_values.append(result["efficiency"])

    # Plot update
    ax1.clear()
    ax2.clear()

    ax1.plot(ratios, thrust_values)
    ax1.set_title("Thrust vs Pressure Ratio")
    ax1.set_xlabel("Pressure Ratio")
    ax1.set_ylabel("Thrust (N)")
    ax1.grid()

    ax2.plot(ratios, eff_values)
    ax2.set_title("Efficiency vs Pressure Ratio")
    ax2.set_xlabel("Pressure Ratio")
    ax2.set_ylabel("Thermal Efficiency")
    ax2.grid()

    canvas.draw()

    # Nozzle condition indicator
    last = run_simulation(T1, P1, 10, comp_eff, turb_eff)
    if last["V_exit"] < 1:
        nozzle_status.set("Nozzle: No Expansion ⚠️")
    elif last["V_exit"] > 1000:
        nozzle_status.set("Nozzle: High Velocity (Choked-like)")
    else:
        nozzle_status.set("Nozzle: Normal Flow")


# -----------------------------
# EXPORT TO CSV
# -----------------------------
def export_csv():
    file = filedialog.asksaveasfilename(defaultextension=".csv")

    if not file:
        return

    T1 = 288
    P1 = 101325
    comp_eff = comp_slider.get()
    turb_eff = turb_slider.get()

    ratios = list(range(2, 25))

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Pressure Ratio", "Thrust", "Efficiency"])

        for r in ratios:
            res = run_simulation(T1, P1, r, comp_eff, turb_eff)
            writer.writerow([r, res["thrust"], res["efficiency"]])


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()
root.title("Gas Turbine Simulator PRO")
root.geometry("1000x600")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="Gas Turbine Simulator", font=("Arial", 18),
         fg="white", bg="#1e1e1e").pack(pady=10)

# Left Panel
control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack(side=tk.LEFT, padx=20)

# Mode Dropdown
tk.Label(control_frame, text="Cycle Type", fg="white", bg="#1e1e1e").pack()
mode_var = tk.StringVar(value="Ideal")
mode_menu = ttk.Combobox(control_frame, textvariable=mode_var,
                         values=["Ideal", "Real"])
mode_menu.pack(pady=5)
mode_menu.bind("<<ComboboxSelected>>", update_simulation)

# Fuel Dropdown (placeholder for future physics)
tk.Label(control_frame, text="Fuel Type", fg="white", bg="#1e1e1e").pack()
fuel_var = tk.StringVar(value="Jet-A")
fuel_menu = ttk.Combobox(control_frame, textvariable=fuel_var,
                         values=["Jet-A", "Hydrogen", "Kerosene"])
fuel_menu.pack(pady=5)

# Compressor slider
tk.Label(control_frame, text="Compressor Efficiency", fg="white", bg="#1e1e1e").pack()
comp_slider = tk.Scale(control_frame, from_=0.6, to=1.0, resolution=0.01,
                       orient=tk.HORIZONTAL, length=200,
                       command=update_simulation)
comp_slider.set(0.85)
comp_slider.pack(pady=10)

# Turbine slider
tk.Label(control_frame, text="Turbine Efficiency", fg="white", bg="#1e1e1e").pack()
turb_slider = tk.Scale(control_frame, from_=0.6, to=1.0, resolution=0.01,
                       orient=tk.HORIZONTAL, length=200,
                       command=update_simulation)
turb_slider.set(0.9)
turb_slider.pack(pady=10)

# Export button
tk.Button(control_frame, text="Export CSV",
          command=export_csv,
          bg="#2196F3", fg="white", width=20).pack(pady=10)

# Nozzle status
nozzle_status = tk.StringVar()
tk.Label(control_frame, textvariable=nozzle_status,
         fg="yellow", bg="#1e1e1e").pack(pady=10)

# -----------------------------
# GRAPH AREA
# -----------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Initial run
update_simulation()

root.mainloop()
