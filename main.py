from tkinter import *
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Quantum Gate Visualizer")
root.geometry("500x400")
qc = QuantumCircuit(1)

bloch_canvas = None

def update_visuals():
    global bloch_canvas

    # Update circuit text
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())

    # Generate statevector
    state = Statevector.from_instruction(qc)

    # Create Bloch sphere figure
    fig = plot_bloch_multivector(state)

    # Remove old Bloch sphere
    if bloch_canvas is not None:
        bloch_canvas.get_tk_widget().destroy()

    # Embed figure into Tkinter
    bloch_canvas = FigureCanvasTkAgg(fig, master=root)
    bloch_canvas.draw()

    bloch_canvas.get_tk_widget().pack()

def apply_H():
    qc.h(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
    update_visuals()
def apply_x():
    qc.x(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
    update_visuals()
def apply_y():
    qc.y(0)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
    update_visuals()
def reset_circuit():
    global qc
    qc = QuantumCircuit(1)
    circuit_display.delete("1.0", END)
    circuit_display.insert(END, qc.draw())
title = Label(root, text="Quantum Circuit Builder", font=("Arial", 16), background="grey")
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
y_button = Button(button_frame, text="Y Gate", command=apply_y, width=12, height=2, background="blue")
y_button.pack(side=LEFT, padx=10)
reset_button = Button(
    button_frame,
    text="Reset",
    command=reset_circuit,
    width=12,
    height=2,
    background="blue"
)
reset_button.pack(side=LEFT, padx=10)
circuit_display = Text(root, height=15, width=50, font=("Courier", 10), fg = "white", bg = "grey")
circuit_display.pack(pady=20)
circuit_display.insert(END, qc.draw())
root.configure(background="grey")
root.mainloop()