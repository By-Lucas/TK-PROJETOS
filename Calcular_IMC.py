from tkinter import *
import tkinter as tk
from tkinter.font import Font



def calcular(): #criar uma opcao para o botao chamar'''
    peso1 = float(peso.get())
    altura1 = float(altura.get())

    imc = peso1/altura1**2
    resultado ['text'] = imc

janela = Tk()  #criar uma janela MAE
janela.title('CALCULAR IMC'.center(80)) # Titulo do programa e adcionado o titulo no centro
janela.geometry('380x500+600+250') # Largura e altura 
janela.resizable(False, False) # Aqui ninguem pode alterar a largura e nem a altura
BACKCOLOR1 = "#002436" #ESSA OPCAO E ADCIONA UMA COR
janela['background'] = BACKCOLOR1 #ESSA OPCAO EU SELECIONO A JANELA E ADCIONA UMA COR NELA

#CRIAR LABEL NUM FORMATO MAIS ORGANIZADO
label1 = Label(janela,text='Insira seu peso',font='arialblack 15', bg='#002436',fg='white',).grid(row=0, column=0)
label2 = Label(janela,text='Insira sua altura',font='arialblack 15', bg='#002436',fg='white').grid(row=1, column=0)

peso = Entry(janela)
peso.grid(row=0, column=1)

altura = Entry(janela)
altura.grid(row=1, column=1)

calcular1 = Button(janela, text='Calcular IMC',command=calcular,font='10',cursor='hand2').grid(row=3, column=0)

resultado = Label(janela, text='Resultado', font='arial 13', background=BACKCOLOR1, foreground='white')
resultado.grid(row=2, column=1)



janela.mainloop()