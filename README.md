# Gas Turbine Performance Simulator 🚀

A Python-based simulation of a jet engine (Brayton cycle) with parametric analysis.

---

##  Overview

This project models a simplified gas turbine engine using thermodynamic principles.
It simulates compressor, combustor, turbine, and nozzle to evaluate performance.
This project demonstrates thermodynamic modeling, modular Python design, and performance analysis of a jet engine cycle.

---

## Components

* Compressor
* Combustor
* Turbine
* Nozzle

---

##  Features

* Calculates thrust and thermal efficiency
* Performs parametric analysis
* Generates performance graphs

---

## Results

### Thrust vs Pressure Ratio

![Thrust](results/thrust_vs_pr.png)

### Efficiency vs Pressure Ratio

![Efficiency](results/efficiency_vs_pr.png)

---

## Insights

* Efficiency increases with pressure ratio
* Thrust decreases due to higher compressor work in simplified model

---

## Tech Stack

* Python
* Matplotlib

---

## ▶️ Run

```bash
pip install -r requirements.txt
python main.py

---

## Author

Pranav Mohan


---




```md
## 📌 Engineering Note
This model uses a simplified Brayton cycle and assumes constant specific heats and no pressure losses. Results capture trends but are not representative of a real engine.
