from tkinter import *
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# Create main window
root = Tk()
root.title("Quantum Gate Visualizer")
root.geometry("500x400")
qc = QuantumCircuit(1)

def apply_H():
    qc.h(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
    state = Statevector.from_instruction(qc)
    fig = plot_bloch_multivector(state)

def apply_x():
    qc.x(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())

def apply_y():
    qc.y(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())

def reset_circuit():
    global qc
    qc = QuantumCircuit(1)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
title = Label(root, text="Quantum Circuit Builder", font=("Arial", 16), background="white")
title.pack(pady=10)
button_frame = Frame(root)
button_frame.pack(pady=10)

h_button = Button(
    button_frame,
    text="H Gate",
    command=apply_H,
    width=12,
    height=2,
    background="blue"
)
h_button.pack(side=LEFT, padx=10)

x_button = Button(button_frame, text="X Gate", command=apply_x, width=12, height=2, background="blue")
x_button.pack(side=LEFT, padx=10)

reset_button = Button(
    button_frame,
    text="Reset",
    command=reset_circuit,
    width=12,
    height=2,
    background="blue"
)
reset_button.pack(side=LEFT, padx=10)

circuit_display = Text(root, height=15, width=50, font=("Courier", 10))
circuit_display.pack(pady=20)
circuit_display.insert(END, qc.draw())
root.configure(background="white")
root.mainloop()