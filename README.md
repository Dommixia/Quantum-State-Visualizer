# Quantum State Visualizer

An interactive desktop application built with Python and Tkinter that lets you build quantum circuits by applying gates one at a time and instantly visualizes the qubit state on a Bloch sphere.

## What it does

- Apply quantum gates (H, X, Y) to a single qubit using buttons
- Instantly see the qubit state update on the Bloch sphere after each gate
- View the quantum circuit diagram updating in real time
- Reset the circuit back to |0⟩ at any time

## How it works

Each button applies a gate to the quantum circuit. After every gate the app computes the new state vector and re-renders the Bloch sphere, showing exactly how the qubit's state changes with each operation. The circuit diagram updates simultaneously so you can follow the full sequence of gates applied.

## Gates supported

| Gate | Effect |
|---|---|
| H | Creates superposition — moves arrow from north pole to equator |
| X | Flips the qubit — moves arrow from north pole to south pole |
| Y | Flips the qubit with a phase factor |
| Reset | Clears all gates and returns qubit to \|0⟩ |

## Tech stack

- Python
- Qiskit (quantum circuit and state vector)
- Tkinter (GUI)
- Matplotlib (Bloch sphere rendering)

## Setup

```bash
pip install qiskit matplotlib
python main.py
```

## Key learnings

- How to embed Matplotlib figures inside a Tkinter GUI
- How quantum gate sequences build up a circuit incrementally
- How each gate physically moves the qubit state on the Bloch sphere
- Connecting quantum computing concepts to a real interactive interface