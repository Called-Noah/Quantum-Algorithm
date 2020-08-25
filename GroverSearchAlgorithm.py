import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
%config InlineBackend.figure_format = 'svg' #Makes image nice
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.visualization import plot_histogram

#Set new QuantumCircuit, two Qubits
n = 2
grover_circuit = QuantumCircuit(n)

#Draw Hadamard 
for qubit in range(n): # if n = 1, only q0 will be created
    grover_circuit.h(qubit) #h = Hadamard Gate which puts into a superposition state
grover_circuit.draw('mpl') #mpl = matplotlib

#Draw X and cZ Gate
for qubit in range(n):
    grover_circuit.x(qubit) # Create X gate

grover_circuit.cz(0, 1) # cz gate which seems like a line, the connection between q0 and q1

#Draw X gate
for qubit in range(n):
    grover_circuit.x(qubit)

grover_circuit.draw('mpl')

#Draw Hadamard Gate
for qubit in range(n):
    grover_circuit.h(qubit)
grover_circuit.draw('mpl')

#Draw Z and cZ Gate
for qubit in range(n):
    grover_circuit.z(qubit)
grover_circuit.cz(0, 1)

grover_circuit.draw('mpl')

#Draw Hadamard Gate
for qubit in range(n):
    grover_circuit.h(qubit)

grover_circuit.draw('mpl')
