# 🚦 Smart Traffic Route Optimizer

A simple Flask-based web application that visualizes and computes the shortest path between locations using **Dijkstra's Algorithm** or **A\*** search.  
The app renders an interactive map (via Leaflet.js) and lets users click two points to find the optimal route.

---

## 📌 Features

- **Graph-based city map** with nodes and edges.
- **Two pathfinding algorithms**:
  - Dijkstra's Algorithm
  - A\* Search (Euclidean heuristic)
- **Interactive UI** using Leaflet.js and OpenStreetMap tiles.
- **Path visualization** on the map with route cost.
- Simple and beginner-friendly Python implementation.

---

## 📂 Project Structure

```

.
├── app.py                  # Flask backend server
├── smart\_traffic\_core.py   # Graph structure & algorithms
├── templates/
│   └── index.html          # Frontend UI with Leaflet map
└── README.md               # Project documentation

````

---

## ⚙️ Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-traffic-optimizer.git
cd smart-traffic-optimizer
````

2️⃣ **Install dependencies**

```bash
pip install flask
```

3️⃣ **Run the application**

```bash
python app.py
```

4️⃣ **Open in browser**
Visit:

```
http://127.0.0.1:5000/
```

---

## 🖥️ Usage

1. Select the algorithm (**Dijkstra** or **A\***).
2. Click a **start node** on the map.
3. Click a **destination node**.
4. The optimal route will be drawn in **red**, and the total cost will be displayed.

---

## 🧠 Algorithms

* **Dijkstra's Algorithm**
  Finds the shortest path from a source to all nodes in a weighted graph.

* **A\*** Search
  Uses a heuristic (Euclidean distance) to guide the search, often faster for large maps.

Both algorithms use a **min-heap priority queue** (`heapq`) for efficiency.

---

## 📸 Screenshot

<img width="1920" height="1080" alt="Screenshot 2025-08-15 035455" src="https://github.com/user-attachments/assets/18bd810e-6350-47ab-841a-722473521556" />

---

## 📜 License

This project is licensed under the Apache License 2.0 — you are free to use, modify, and distribute it.

---

## 🤝 Contributing

Pull requests are welcome!
If you find a bug or want to add features, feel free to fork this repo and submit a PR.

---

## ✨ Credits

* **Flask** for backend framework
* **Leaflet.js** for interactive maps
* **OpenStreetMap** for map tiles
