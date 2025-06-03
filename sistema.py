import customtkinter as ctk

#sistema com customtkinter 
class Sistema(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dados")
        self.geometry("500x400")
        
        self.pagina_atual = 0
        
        self.paginas = [self.pagina1(), self.pagina2(), self.pagina3(), self.pagina4(), self.pagina5()]
        
        self.mostrar_pagina(self.pagina_atual)
    
    #função de criar a página 1    
    def pagina1(self):
        frame = ctk.CTkFrame(self)
        
        #nome do produto    
        label_nome = ctk.CTkLabel(frame, text="Nome do Produto")
        label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(frame)
        self.entry_nome.pack()
        
        #descrição do produto 
        label_descricao = ctk.CTkLabel(frame, text="Descrição")
        label_descricao.pack(pady=5)
        self.entry_descricao = ctk.CTkEntry(frame)
        self.entry_descricao.pack()
        
        #categoria do produto
        label_categoria = ctk.CTkLabel(frame, text="Categoria")
        label_categoria.pack(pady=5)
        self.combobox_categoria = ctk.CTkComboBox(frame, values=["Calçados", "Roupas", "Acessórios"])
        self.combobox_categoria.pack()
        
        #codigo do produto  
        label_codigo = ctk.CTkLabel(frame, text="Código do Produto")
        label_codigo.pack(pady=5)
        self.entry_codigo = ctk.CTkEntry(frame)
        self.entry_codigo.pack()
        
        #peso do produto    
        label_peso = ctk.CTkLabel(frame, text="Peso(em kg)")
        label_peso.pack(pady=5)
        self.entry_peso = ctk.CTkEntry(frame)
        self.entry_peso.pack()
        
        #botão de próximo   
        botao_proximo = ctk.CTkButton(frame, text="Próximo", command=self.proxima_pagina)
        botao_proximo.pack(side="right", pady=5, padx=30)
           
        return frame
    
    #função de criar a página 2    
    def pagina2(self):
        frame = ctk.CTkFrame(self)
        
        #dimensões do produto   
        label_dimensoes = ctk.CTkLabel(frame, text="Dimensões(L x A x P)")
        label_dimensoes.pack(pady=5)
        self.entry_dimensoes = ctk.CTkEntry(frame)
        self.entry_dimensoes.pack()
        
        #preço do produto    
        label_preco = ctk.CTkLabel(frame, text="Preço")
        label_preco.pack(pady=5)
        self.entry_preco = ctk.CTkEntry(frame)
        self.entry_preco.pack()
        
        #quantidade em estoque do produto  
        label_qtd_estoque = ctk.CTkLabel(frame, text="Quantidade em Estoque")
        label_qtd_estoque.pack(pady=5)
        self.entry_qtd_estoque = ctk.CTkEntry(frame)
        self.entry_qtd_estoque.pack()
        
        #data de validade do produto   
        label_data_validade = ctk.CTkLabel(frame, text="Data de Validade")
        label_data_validade.pack(pady=5)
        self.entry_data_validade = ctk.CTkEntry(frame)
        self.entry_data_validade.pack()
        
        #botão de voltar    
        botao_voltar= ctk.CTkButton(frame, text="Voltar", command=self.voltar_pagina)
        botao_voltar.pack(side="left", pady=5, padx=30)
        
        #botão de próximo    
        botao_proximo = ctk.CTkButton(frame, text="Próximo", command=self.proxima_pagina)
        botao_proximo.pack(side="right", pady=5, padx=30)
            
        return frame
    
    #função de criar a página 3    
    def pagina3(self):
        frame = ctk.CTkFrame(self)
        
        #cor do produto    
        label_cor = ctk.CTkLabel(frame, text="Cor")
        label_cor.pack(pady=5)
        self.entry_cor = ctk.CTkEntry(frame)
        self.entry_cor.pack()
        
        #tamanho do produto    
        label_tamanho = ctk.CTkLabel(frame, text="Tamanho")
        label_tamanho.pack(pady=5)
        self.combobox_tamanho = ctk.CTkComboBox(frame, values=["Pequeno", "Médio", "Grande"])
        self.combobox_tamanho.pack()
        
        #material do produto    
        label_material = ctk.CTkLabel(frame, text="Material")
        label_material.pack(pady=5)
        self.entry_material = ctk.CTkEntry(frame)
        self.entry_material.pack()
        
        #fabricante do produto   
        label_fabricante = ctk.CTkLabel(frame, text="Fabricante")
        label_fabricante.pack(pady=5)
        self.entry_fabricante = ctk.CTkEntry(frame)
        self.entry_fabricante.pack()
        
        #botão de voltar   
        botao_voltar= ctk.CTkButton(frame, text="Voltar", command=self.voltar_pagina)
        botao_voltar.pack(side="left", pady=5, padx=30)
        
        #botão de próximo   
        botao_proximo = ctk.CTkButton(frame, text="Próximo", command=self.proxima_pagina)
        botao_proximo.pack(side="right", pady=5, padx=30)
            
        return frame
    
    #função de criar a página 4    
    def pagina4(self):
        frame = ctk.CTkFrame(self)
        
        #país de origem do produto   
        label_pais_origem = ctk.CTkLabel(frame, text="País de Origem")
        label_pais_origem.pack(pady=5)
        self.entry_pais_origem = ctk.CTkEntry(frame)
        self.entry_pais_origem.pack()
        
        #observações do produto    
        label_observacoes = ctk.CTkLabel(frame, text="Observações")
        label_observacoes.pack(pady=5)
        self.entry_observacoes = ctk.CTkEntry(frame)
        self.entry_observacoes.pack()
        
        #código de barras do produto    
        label_codigo_barras = ctk.CTkLabel(frame, text="Código de Barras")
        label_codigo_barras.pack(pady=5)
        self.entry_codigo_barras = ctk.CTkEntry(frame)
        self.entry_codigo_barras.pack()
        
        #localização do produto no armazém    
        label_loc_armazem = ctk.CTkLabel(frame, text="Localização no Armazém")
        label_loc_armazem.pack(pady=5)
        self.entry_loc_armazem = ctk.CTkEntry(frame)
        self.entry_loc_armazem.pack()
        
        #botão de voltar    
        botao_voltar= ctk.CTkButton(frame, text="Voltar", command=self.voltar_pagina)
        botao_voltar.pack(side="left", pady=5, padx=30)
        
        #botão de próximo   
        botao_proximo = ctk.CTkButton(frame, text="Próximo", command=self.proxima_pagina)
        botao_proximo.pack(side="right", pady=5, padx=30)
            
        return frame
    
    #função de criar a página 5    
    def pagina5(self):
        frame = ctk.CTkFrame(self)
        
        #mensagem    
        label_mensagem = ctk.CTkLabel(frame, text="Dados salvos com sucesso!")
        label_mensagem.pack(pady=10)
        
        #botão de finalizar    
        botao_finalizar= ctk.CTkButton(frame, text="Finalizar", command=self.finalizar)
        botao_finalizar.pack()
            
        return frame
    
    #função de mostrar a página    
    def mostrar_pagina(self, indice):
        for pagina in self.paginas:
            pagina.pack_forget()
                
            self.paginas[indice].pack(fill="both", expand=True)
    
    #função de ir para a próxima página 
    def proxima_pagina(self):
        if self.pagina_atual < len(self.paginas) - 1:
            self.pagina_atual += 1
            self.mostrar_pagina(self.pagina_atual)
    
    #função de voltar para a página anterior        
    def voltar_pagina(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            self.mostrar_pagina(self.pagina_atual)  
    
    #função de finalizar        
    def finalizar(self):
        self.entry_nome.delete(0, ctk.END)
        self.entry_descricao.delete(0, ctk.END)
        self.entry_codigo.delete(0, ctk.END)
        self.entry_peso.delete(0, ctk.END)
        self.entry_dimensoes.delete(0, ctk.END)
        self.entry_preco.delete(0, ctk.END)
        self.entry_qtd_estoque.delete(0, ctk.END)
        self.entry_data_validade.delete(0, ctk.END)
        self.entry_cor.delete(0, ctk.END)
        self.entry_material.delete(0, ctk.END)
        self.entry_fabricante.delete(0, ctk.END)
        self.entry_pais_origem.delete(0, ctk.END)
        self.entry_observacoes.delete(0, ctk.END)
        self.entry_codigo_barras.delete(0, ctk.END)
        self.entry_loc_armazem.delete(0, ctk.END)
        
        self.pagina_atual = 0
        self.mostrar_pagina(self.pagina_atual) 
        

if __name__ == "__main__":
    app = Sistema()
    app.mainloop()
    