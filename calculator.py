def calc(a, op, b):
    if op == '+': return a + b
    if op == '*': return a * b
    if op == '-': return a - b
    
    if op == '/': return a / b if b != 0 else 'Sıfıra bölme hatası'
    return 'Geçersiz işlem'

a = float(input('Birinci sayı: '))
op = input('İşlem (+ - * /): ')
b = float(input('İkinci sayı: '))
print('Sonuç:', calc(a, op, b))

