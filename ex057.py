sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0:9]
while sexo not in 'MASCULINOFEMININO':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0:9]
print('sexo \33[31m{}\33[m registrado com sucesso '.format(sexo[0]))
