class Aluno:
    def __init__(self,nome,av1, av2,av3):
        self.nome = nome
        self.av1 = av1
        self.av2 = av2
        self.av3 = av3
    
    def apresentar(self):
        print('Nome: ', self.nome)
    

    
    def notas(self):
        media_f = (self.av1 + self.av2+ self.av3)/3
        
        if media_f > 7:
            print('Aluno aprovado!!')
        else:
            print('Aluno Reprovado!!')
media = Aluno('Carlos',7,8,7)
media.apresentar()
media.notas()