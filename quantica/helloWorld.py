from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1, 1)
qc.h(0)

# Medir o qubit e armazenar o resultado no bit clássico
qc.measure(0, 0)

# Executar o circuito em um simulador
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()

# Obter e exibir os resultados
counts = result.get_counts(qc)
print("Resultados:", counts)
