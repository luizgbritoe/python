class Veiculo:
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def exibir_info(self):
        info_base = super().exibir_info()
        return f'{info_base}, Número de Portas: {self.num_portas}'
    
carro1 = Carro('Toyota', 'Corolla', 4)
print(carro1.exibir_info())

carro2 = Carro('Chevrolet', 'Onix', 4)
print(carro2.exibir_info())