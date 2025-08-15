from flask import Flask, render_template, request, jsonify
from math import isfinite
from smart_traffic_core import Graph, sample_map, dijkstra, astar, reconstruct_path

app = Flask(__name__)
graph = sample_map()

@app.route("/")
def index():
    # Send nodes and edges to JS for drawing
    nodes = [{"id": n.id, "name": n.name, "x": n.x, "y": n.y} for n in graph.nodes]
    edges = [{"u": u, "v": e.to, "w": e.weight}
             for u in range(graph.size())
             for e in graph.neighbors(u) if u < e.to]  # avoid duplicates
    return render_template("index.html", nodes=nodes, edges=edges)

@app.route("/find_path", methods=["POST"])
def find_path():
    data = request.json
    src = int(data["src"])
    dst = int(data["dst"])
    algo = data["algo"]

    if algo == "dijkstra":
        dist, parent = dijkstra(graph, src)
        finald = dist[dst]
    else:
        dist, parent = astar(graph, src, dst)
        finald = dist[dst]

    if isfinite(finald):
        path = reconstruct_path(parent, src, dst)
        return jsonify({"path": path, "cost": finald})
    else:
        return jsonify({"error": "No path found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
