''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 3. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10, el segundo $20, el tercero $40, el cuarto $80 y así sucesivamente (el pago se dobla cada mes). Escribe un programa que calcule cada pago mensual y el total de lo que pagó después de los 20 meses.
'''

pago = 10
total = 0

for i in range(20):
    print(f'pago del mes {i+1} es: {pago}')
    total += pago
    pago *=2

print(f'El total pagado es: {total}')