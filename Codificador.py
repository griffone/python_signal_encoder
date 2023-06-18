def nrz(secuencia_bits):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '1':
            resultado += '+'
        else:
            resultado += '0'
    return resultado

def nrz_l(secuencia_bits):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '1':
            resultado += '-'
        else:
            resultado += '+'
    return resultado

def nrz_i(secuencia_bits, bit_previo):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '1':
            bit_previo = '1' if bit_previo == '0' else '0'
            # valor_verdadero if condicion else valor_falso <-- Operador ternario
        resultado += '+' if bit_previo == '1' else '-'
    return resultado

def rz(secuencia_bits):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '1':
            resultado += '+0'
        else:
            resultado += '-0'
    return resultado

def manchester(secuencia_bits):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '1':
            resultado += '-+'
        else:
            resultado += '+-'
    return resultado

def manchester_diferencial(secuencia_bits, bit_previo):
    resultado = ''
    for bit in secuencia_bits:
        if bit == '0':
            resultado += '+-' if bit_previo == '1' else '-+'
        else:
            bit_previo = '1' if bit_previo == '0' else '0'
            resultado += '+-' if bit_previo == '1' else '-+'
    return resultado

def ami(secuencia_bits, bit_previo):
    resultado = ''
    polaridad = 1 if bit_previo == '0' else -1
    for bit in secuencia_bits:
        if bit == '1':
            resultado += '+' if polaridad == 1 else '-'
            polaridad = -polaridad
        else:
            resultado += '0'
    return resultado

def pseudoternary(secuencia_bits, bit_previo):
    resultado = ''
    polaridad = 1 if bit_previo == '0' else -1
    for bit in secuencia_bits:
        if bit == '0':
            resultado += '+' if polaridad == 1 else '-'
            polaridad = -polaridad
        else:
            resultado += '0'
    return resultado

def hdb3(secuencia, pulso):
    
    pulso = "-" if pulso == "+" else "+"

    contador_pulsos = 0
    ceros_seguidos = 0
    resultado = ''

    for bit in secuencia:
        if bit == "1":
            contador_pulsos += 1
            ceros_seguidos = 0
            if contador_pulsos != 1:
                pulso = "+" if pulso == "-" else "-"
            resultado += pulso
        else:
            ceros_seguidos += 1
            if ceros_seguidos == 4:
                ceros_seguidos = 0
                if contador_pulsos % 2 == 0:
                    pulso = "+" if pulso == "-" else "-"
                    resultado = resultado[:-3]
                    contador_pulsos += 2
                    resultado += pulso + "00" + pulso
                else:
                    resultado = resultado[:-3]
                    contador_pulsos += 1
                    resultado += "000" + pulso
            else:
                resultado += "0"
    return resultado

def b8zs(secuencia, pulso):
    
    pulso = "-" if pulso == "+" else "+"
    
    ceros_seguidos = 0
    resultado = ''

    for bit in secuencia:
        if bit == "1":
            ceros_seguidos = 0
            if resultado:  # Verifica si hay algún bit previo en el resultado
                pulso = "+" if pulso == "-" else "-"
            resultado += pulso
        else:
            ceros_seguidos += 1
            if ceros_seguidos == 8:
                ceros_seguidos = 0
                pattern = "000" + pulso
                pulso = "+" if pulso == "-" else "-"
                pattern += pulso + "0" + pulso
                pulso = "+" if pulso == "-" else "-"
                pattern += pulso
                resultado = resultado[:-7]
                resultado += pattern
            else:
                resultado += "0"
    return resultado

secuencia_bits = input("Ingresa la secuencia de bits: ")

while not all(bit in ('0', '1') for bit in secuencia_bits):
    print("Error: La secuencia debe contener solo bits (0 o 1).")
    secuencia_bits = input("Ingresa la secuencia de bits nuevamente: ")

esquema_codificacion = input("Ingresa el esquema de codificación (1. NRZ, 2. NRZ-L, 3. NRZ-I, 4. RZ, 5. Manchester, 6. Manchester Diferencial, 7. AMI, 8. Pseudo-ternario, 9. HDB3, 10. B8ZS): ")

if esquema_codificacion == '1':
    resultado_final = nrz(secuencia_bits)
elif esquema_codificacion == '2':
    resultado_final = nrz_l(secuencia_bits)
elif esquema_codificacion == '3':
    bit_previo = input("Ingresa el bit anterior: ")
    resultado_final = nrz_i(secuencia_bits, bit_previo)
elif esquema_codificacion == '4':
    resultado_final = rz(secuencia_bits)
    print("Advertencia: Tener en cuenta la bibliografía, es posible que la secuencia este al revés")
elif esquema_codificacion == '5':
    resultado_final = manchester(secuencia_bits)
elif esquema_codificacion == '6':
    bit_previo = input("Ingresa el bit anterior: ")
    resultado_final = manchester_diferencial(secuencia_bits, bit_previo)
elif esquema_codificacion == '7':
    bit_previo = input("Ingresa el bit anterior: ")
    resultado_final = ami(secuencia_bits, bit_previo)
elif esquema_codificacion == '8':
    bit_previo = input("Ingresa el bit anterior: ")
    resultado_final = pseudoternary(secuencia_bits, bit_previo)
elif esquema_codificacion == '9':
    pulso = input("Ingresa el pulso anterior (+/-): ")
    resultado_final = hdb3(secuencia_bits, pulso)
elif esquema_codificacion == '10':
    pulso = input("Ingresa el pulso anterior (+/-): ")
    resultado_final = b8zs(secuencia_bits, pulso)

print(f"La secuencia codificada es: {resultado_final}")
input()
