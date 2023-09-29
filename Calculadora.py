import flet as ft
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '+-', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '7', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '8', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '9', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '*', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '4', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '5', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '6', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '-', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '1', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '2', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '3', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '+', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '0', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '.', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '=', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
]

def main(page: ft.Page): #Criando janela
    page.bgcolor='black'
    page.window_resizable = False #Não permite que o usuário redimensione a tela
    page.window_width = 300
    page.window_height = 390
    page.title = 'Calculadora do Sinx'
    page.window_always_on_top = True

    resultados = ft.Text(value=0, color= ft.colors.WHITE, size=20)


    def calculo(operador, vatual):
        try:
            total = eval(vatual) #Eval realiza cálculos por exemplo se ele encontrar o sinal + ele fará ma dição
        
            if operador == '%':
                total = total/100
            elif operador == '+-':
                total = -total
        except:
            return 'ERRO!'
        digits = min(abs(Decimal(total).as_tuple().exponent), 5)
        return format(total, f'.{digits}f')
    
            
        

    def select(e):
        vatual = resultados.value if resultados.value not in (0, 'ERRO!') else ''
        valor = e.control.content.value

        if valor.isdigit():
            valor = vatual + valor
        elif valor == 'AC':
            valor = 0
        else:
            if vatual and vatual[-1] in ('/','*', '-', '+', '.'): #[-1] seria último valor digitado
                vatual = vatual[:-1]

            valor = vatual + valor

            if valor[-1] in ('=','%','+-'):
                valor = calculo(operador=valor[-1], vatual=vatual)
        resultados.value = valor
        resultados.update()

    display = ft.Row( #Cria uma linha onde ficará os resultados
        width=300, #Tamanho da linha
        controls=[resultados],
        alignment='end',
    )
    
    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100, #arredonda o botão
        alignment=ft.alignment.center,
        on_click=select

        ) for btn in botoes] #Para cada botão dentro da lista botoes irá recriar o mesmo padrão

    keyboard = ft.Row( #Jogando a lista para dentro de uma row para poder mostrar na tela
        width=250,
        wrap=True, #Quebra a linha quando chegar no final da linha (limite da tela na horizontal)
        controls=btn,
        alignment='end'

    )

    page.add(display, keyboard) #Adiciona os elementos criados na tela




ft.app(target= main)
