texto = input('Digite algo: ')

print(f'O texto é alfanumérico?', texto.isalnum())
print(f'O texto é alfabético?', texto.isalpha())
print(f'O texto está capitalizado?', texto.istitle())
print(f'Os valores são decimais?', texto.isdecimal())
print(f'As letras estão em maiúsculas?', texto.isupper())
print(f'As letras estão em minúsculas?', texto.islower())
