class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios_cuenta, balance_cuenta):
        self.numero_cuenta=numero_cuenta
        self.propietarios_cuenta=propietarios_cuenta
        self.balance_cuenta=balance_cuenta

cuenta= CuentaBancaria("1000508684", ["Meruem", "Netero"], 20000.896)

print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios_cuenta)
print("Balance:", cuenta.balance_cuenta)