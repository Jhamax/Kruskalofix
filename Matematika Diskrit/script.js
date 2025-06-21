// script.js
let edges = [];

function tambahSisi() {
  const from = document.getElementById("from").value.toUpperCase();
  const to = document.getElementById("to").value.toUpperCase();
  const length = parseInt(document.getElementById("length").value);
  if (from && to && !isNaN(length)) {
    edges.push([from, to, length]);
    updateDaftarSisi();
  }
}

function updateDaftarSisi() {
  const ul = document.getElementById("daftarSisi");
  ul.innerHTML = "";
  edges.forEach((e) => {
    const li = document.createElement("li");
    li.textContent = `${e[0]} -- ${e[1]} == ${e[2]} meter`;
    ul.appendChild(li);
  });
}

function hitungMST() {
  const nodes = new Set();
  edges.forEach(([u, v]) => {
    nodes.add(u);
    nodes.add(v);
  });
  const nodeList = Array.from(nodes);
  const map = {};
  nodeList.forEach((n, i) => map[n] = i);

  const parent = Array(nodeList.length).fill(0).map((_, i) => i);
  const rank = Array(nodeList.length).fill(0);

  function find(i) {
    if (parent[i] !== i) parent[i] = find(parent[i]);
    return parent[i];
  }

  function union(x, y) {
    const xroot = find(x);
    const yroot = find(y);
    if (rank[xroot] < rank[yroot]) {
      parent[xroot] = yroot;
    } else if (rank[xroot] > rank[yroot]) {
      parent[yroot] = xroot;
    } else {
      parent[yroot] = xroot;
      rank[xroot]++;
    }
  }

  const sortedEdges = [...edges].sort((a, b) => a[2] - b[2]);
  const mst = [];
  let total = 0;
  sortedEdges.forEach(([u, v, w]) => {
    const x = find(map[u]);
    const y = find(map[v]);
    if (x !== y) {
      mst.push([u, v, w]);
      total += w;
      union(x, y);
    }
  });

  const tbody = document.querySelector("#hasilTabel tbody");
  tbody.innerHTML = "";
  mst.forEach(([u, v, w]) => {
    const row = `<tr><td>${u}</td><td>${v}</td><td>${w}</td></tr>`;
    tbody.innerHTML += row;
  });

  const pricePerMeter = parseInt(document.getElementById("pricePerMeter").value);
  const totalCost = total * pricePerMeter;

  document.getElementById("totalBobot").textContent = `Total bobot MST: ${total} meter`;
  document.getElementById("totalBiaya").textContent = `Total biaya kabel: Rp ${totalCost}`;
}
