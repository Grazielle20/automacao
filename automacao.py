import openpyxl
import pyperclip
import pyautogui
from time import sleep

#acesso a tabela
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

#acessando o conteúdo de cada linha na tabela
for linha in sheet_produtos.iter_rows(min_row=2):
    
    #nome do produto
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1060,154, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #descrição
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1051,220, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #categoria
    categoria = linha[2].value
    pyautogui.click(1162,287, duration=1)
    if categoria == "Calçados":
        pyautogui.click(1075,313, duration=1)
    elif categoria == "Roupas":
        pyautogui.click(1072,346, duration=1)
    else:
        pyautogui.click(1063,373, duration=1)
    
    #código do produto
    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1060,352, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #peso
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1045,417, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #botão de próximo
    pyautogui.click(1251,467, duration=1)
    sleep(2)
    
    #dimensões
    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1055,154, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #preço
    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1054,218, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #quantidade em estoque
    qtd_estoque = linha[7].value
    pyperclip.copy(qtd_estoque)
    pyautogui.click(1058,287, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #data de validade
    data_validade = linha[8].value
    pyperclip.copy(data_validade)
    pyautogui.click(1055,351, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #botão de próximo
    pyautogui.click(1256,434, duration=1)
    sleep(2)
    
    #cor
    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1046,153, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #tamanho
    tamanho = linha[10].value
    pyautogui.click(1164,219, duration=1)
    if tamanho == "Pequeno":
        pyautogui.click(1056,253, duration=1)
    elif tamanho == "Médio":
        pyautogui.click(1051,283, duration=1)
    else:
        pyautogui.click(1055,301, duration=1)
    
    #material  
    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1048,288, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #fabricante
    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1049,354, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #botão de próximo
    pyautogui.click(1257,433,duration=1)
    sleep(2)
    
    #país de origem
    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1047,156, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #observações
    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1048,221, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #código de barras
    codigo_barras = linha[15].value
    pyperclip.copy(codigo_barras)
    pyautogui.click(1049,288, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #localização no armazém
    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(1051,353, duration=1)
    pyautogui.hotkey("ctrl", "v")
    
    #botão de próximo
    pyautogui.click(1246,432,duration=1)
    sleep(2)
    
    #botão de finalizar
    pyautogui.click(1104,163,duration=1)
    sleep(2)