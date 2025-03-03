let tablero = [
  [7, 1, 3],
  [4, 0, 5],
  [6, 2, 8],
];

function actualizarTablero() {
  const tableroDiv = document.getElementById("tablero");
  tableroDiv.innerHTML = "";
  tablero.flat().forEach((num) => {
    const cell = document.createElement("div");
    cell.className = "cell";
    cell.textContent = num !== 0 ? num : "";
    tableroDiv.appendChild(cell);
  });
  console.log("Estado actual del tablero:", tablero);
}

function generarAleatorio() {
  let nums = [0, 1, 2, 3, 4, 5, 6, 7, 8].sort(() => Math.random() - 0.5);
  tablero = [
    [nums[0], nums[1], nums[2]],
    [nums[3], nums[4], nums[5]],
    [nums[6], nums[7], nums[8]],
  ];
  actualizarTablero();
  console.log("Nuevo estado generado aleatoriamente:", tablero);
}

function encontrarPosicionVacia(tablero) {
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (tablero[i][j] === 0) return [i, j];
    }
  }
}

function copiarTablero(tablero) {
  return tablero.map((fila) => [...fila]);
}

function intercambiar(tablero, x1, y1, x2, y2) {
  let nuevoTablero = copiarTablero(tablero);
  [nuevoTablero[x1][y1], nuevoTablero[x2][y2]] = [
    nuevoTablero[x2][y2],
    nuevoTablero[x1][y1],
  ];
  return nuevoTablero;
}

function sonIguales(tablero1, tablero2) {
  return JSON.stringify(tablero1) === JSON.stringify(tablero2);
}

async function resolver() {
  let tablero_meta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
  ];
  let movimientos = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let cola = [{ tablero: tablero, camino: [] }];
  let visitados = new Set();
  let intentos = 0;
  let inicio = performance.now();

  document.getElementById("resultados").innerHTML = "";
  console.log("Estado inicial:", tablero);
  while (cola.length > 0) {
    let { tablero, camino } = cola.shift();
    let clave = JSON.stringify(tablero);
    if (visitados.has(clave)) continue;
    visitados.add(clave);
    intentos++;

    if (sonIguales(tablero, tablero_meta)) {
      let totalTiempo = (performance.now() - inicio) / 1000;
      document.getElementById(
        "resultados"
      ).innerHTML += `Solución encontrada en ${intentos} intentos en ${totalTiempo.toFixed(
        2
      )} segundos.<br><br>`;
      console.log(
        "Solución encontrada en",
        intentos,
        "intentos en",
        totalTiempo.toFixed(2),
        "segundos."
      );
      return;
    }

    let [x, y] = encontrarPosicionVacia(tablero);
    for (let [dx, dy] of movimientos) {
      let nx = x + dx,
        ny = y + dy;
      if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
        let nuevoTablero = intercambiar(tablero, x, y, nx, ny);
        cola.push({ tablero: nuevoTablero, camino: [...camino, nuevoTablero] });
        console.log("Paso", intentos, "\n", nuevoTablero);
        actualizarTablero();
      }
    }
  }
  document.getElementById("resultados").innerHTML = "No se encontró solución.";
  console.log("No se encontró solución después de", intentos, "intentos.");
}

actualizarTablero();
