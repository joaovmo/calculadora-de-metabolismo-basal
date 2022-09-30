from ast import Break
from lib2to3.pytree import convert
from msilib.schema import CheckBox
from multiprocessing import Event
from multiprocessing.resource_sharer import stop
from optparse import Values
from re import M
from subprocess import CREATE_NO_WINDOW
from turtle import clear
import typing
import PySimpleGUI as sg

sg.theme('Dark Brown')

class Telapython:
    def __init__(self):
        #layout
        layout = [
            [sg.Image(sg.EMOJI_BASE64_HAPPY_BIG_SMILE)],   
            [sg.Text('Digite seu nome: ',size=(18)),sg.Input(size=(30),key='nome')],
            [sg.Text('Digite sua idade: ',size=(18)),sg.Input(size=(30),key='idade')],
            [sg.Text('Digite seu peso: ',size=(18)),sg.Input(size=(30),key='peso')],
            [sg.Text('Digite sua altura em cm: ',size=(18)),sg.Input(size=(30),key='altura')],
            [sg.Text('Qual seu sexo?')],
            [sg.Checkbox('h',key='h'),sg.Checkbox('m',key='m')],
            [sg.Button('Enviar dados', expand_x = True)],
            [sg.Button('Limpar dados', expand_x = True)],
            [sg.Combo(["Sou sedentario (não faço atividades)", 'Faço pouca atividade (3x na semana)', 'Faço muita atividade (5x na semana)'],key='atividades', expand_x=True, s=(13))],
            [sg.Output(size=(55,18),key='saida', font = 'Franklin 12',)]
        ]
        #janela
        self.janela = sg.Window("Caluladora de metabolismo basal").layout(layout)
        #extrair oa dados da tela
        self.button, self.values, = self.janela.Read()
    
        while True:
            self.button, self.values, = self.janela.Read()
            self.janela.FindElement('saida').Update('')
            tmbh = 0
            nome = self.values['nome']
            idade = int(self.values['idade'])
            peso = int(self.values['peso'])
            altura = int(self.values['altura']) 
            h = self.values['h']
            m = self.values['m']
            atividades=(self.values['atividades'])
            if h == True:
                tmbh = 66 + (13.8*peso) + (5*altura) - (6.8*idade)
                print(f'{nome}, sua taxa de metabolismo é : {round(tmbh)} calorias')
                if atividades == 'Sou sedentario (não faço atividades)':
                    perder_20 = tmbh * 0.8
                    print(f'voce precisa comer {round(perder_20)} calorias para emagrecer' )
                    manter_10 = tmbh * 1
                    print(f'voce precisa comer {round(manter_10)} calorias para manter seu peso' )
                    engordar_30 = tmbh * 1.3
                    print(f'voce precisa comer {round(engordar_30)} calorias para aumentar seu peso' )
                elif atividades == 'Faço pouca atividade (3x na semana)':
                    perder_11 = tmbh * 0.95
                    print(f'voce precisa comer {round(perder_11)} calorias para emagrecer' )
                    manter_20 = tmbh * 1.2
                    print(f'voce precisa comer {round(manter_20)} calorias para manter seu peso' )
                    engordar_40 = tmbh * 1.4
                    print(f'voce precisa comer {round(engordar_40)} calorias para aumentar seu peso' )
                elif atividades == 'Faço muita atividade (5x na semana)':
                    perder_10 = tmbh * 1
                    print(f'voce precisa comer {round(perder_10)} calorias para emagrecer' )
                    manter_30 = tmbh * 1.3
                    print(f'voce precisa comer {round(manter_30)} calorias para manter seu peso' )
                    engordar_45 = tmbh * 1.45
                    print(f'voce precisa comer {round(engordar_45)} calorias para aumentar seu peso' )
            elif h == False:
               tmbm = 655 + (9.6*peso) + (1.8*altura) - (4.7*idade)
               print (f'{nome}, sua taxa de metabolismo é : {round(tmbm)} calorias')
               if atividades == 'Sou sedentario (não faço atividades)':
                    perder_20m = tmbm * 0.8
                    print(f'voce precisa comer {round(perder_20m)} calorias para emagrecer' )
                    manter_10m = tmbm * 1
                    print(f'voce precisa comer {round(manter_10m)} calorias para manter seu peso' )
                    engordar_30m = tmbm * 1.3
                    print(f'voce precisa comer {round(engordar_30m)} calorias para aumentar seu peso' )
               elif atividades == 'Faço pouca atividade (3x na semana)':
                    perder_11m = tmbm * 0.95
                    print(f'voce precisa comer {round(perder_11m)} calorias para emagrecer' )
                    manter_20m = tmbm * 1.2
                    print(f'voce precisa comer {round(manter_20m)} calorias para manter seu peso' )
                    engordar_40m = tmbm * 1.4
                    print(f'voce precisa comer {round(engordar_40m)} calorias para aumentar seu peso' )
               elif atividades == 'Faço muita atividade (5x na semana)':
                    perder_10m = tmbm * 1
                    print(f'voce precisa comer {round(perder_10m)} calorias para emagrecer' )
                    manter_30m = tmbm * 1.3
                    print(f'voce precisa comer {round(manter_30m)} calorias para manter seu peso' )
                    engordar_45m = tmbm * 1.45
                    print(f'voce precisa comer {round(engordar_45m)} calorias para aumentar seu peso' )
            if self.button == 'Limpar dados':
                current_num = []
                full_operation = []
                self.janela['saida'].Update("")
            
            

            
            
                    



tela = Telapython()
tela.Iniciar()