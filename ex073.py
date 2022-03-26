times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceara SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Gremio', 'Juventude',
         'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(times)
print('=-' * 80)
print(f'os 5 primeiros são {times[0:6]}')
print('=-' * 80)
print(f'Os 4 ultimos são {times[-5:-1]}')
print('=-' * 80)
print(f'Os times em ordem alfabética{sorted(times)}')
print('=-' * 80)
print(f'O chapecoense esta na {times.index("Chapecoense")+1} posição')
