from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.visualization import matplotlib
import matplotlib.pyplot as ptl

# para executar programas quanticos de seguir 4 passos
# 1 mapear o problema para quântico
# 2 criar os circuitos e operadores
# 3 executar usando uma função primitiva quântica
# 4 analizar o resultado

# criando um novo circuito de qubits
qc = QuantumCircuit(2)

# adiciona uma porta hadamard?
qc.h(0)

# faz o entrelaçamento (CNOT) do qubit 0 com o qubit 1 
qc.cx(0, 1)

# desenha o resultado (no caso como funciona o entrelaçamento)
qc.draw("mpl")
ptl.show()

# basicamente esse circuito entrelaça os 2 qubits, é um "estado de bell",os dois se entrelaçam, como é mostrado no retorno
