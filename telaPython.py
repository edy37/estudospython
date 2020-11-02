import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.theme('dark grey 5')
        # layout
        layout = [
            [sg.Text('Nome: ',size=(5,0)), sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade: ',size=(5,0)), sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos? ')],
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Outlook',key='outlook'), sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim','cartões', key='simcartao'), sg.Radio('Não','cartões',key='naocartao')],
            [sg.Slider(range=(0,225),default_value=0,orientation='h',size=(15,20),key='sv')],
            [sg.Button('Enviar Dados: ')
            ],
            [sg.Output(size=(30,20))]
            ] 

        # janela
        self.janela = sg.Window('Dados do Usúario: ').layout(layout)
        # Extrair dados


    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            ac_gmail = self.values['gmail']
            ac_outlook = self.values['outlook']
            ac_yahoo = self.values['yahoo']
            sim_cartao = self.values['simcartao']
            nao_cartao = self.values['naocartao']
            s_v = self.values['sv']

            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {ac_gmail}')
            print(f'Aceita Outlook: {ac_outlook}')
            print(F'Aceita Yahoo: {ac_yahoo}')
            print(f'Aceita cartão: {sim_cartao}')
            print(f'Não aceita cartão: {nao_cartao}')
            print(f'Velocidade script {s_v}')

            
tela = TelaPython()
tela.Iniciar()

