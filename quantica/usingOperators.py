# operadores de uso ou using operators é um objeto matemático usado para representar uma ação ou processo que altera um estado quântico
# criando variaveis observaveis

observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# o operador ZZ é Z⊗Z ou Z1Z0 (o entrelaçamento o qubit 1 e 0)
