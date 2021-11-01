from tkinter import *
from tkinter.messagebox import *


class DNA:
    """Uma string que representa um pedaço de uma das fitas de DNA com apenas 4 letras, 'A', 'T', 'C', 'G'."""

    def __init__(self, seq):
        self.seq = seq

    def verify(self):
        """É um método que vai verificar se o a sequência realmente representa um DNA"""

        validDNA = True

        for amino in self.seq:

            if amino != 'A' and amino != 'C' and amino != 'G' and amino != 'T':
                validDNA = False

        return validDNA

    def transcription(self):
        """Método que irá transcrever o DNA em RNA mensageiro"""

        mRNA = list(self.seq)

        for i in range(len(mRNA)):

            if mRNA[i] == "A":
                mRNA[i] = "U"

            elif mRNA[i] == "T":
                mRNA[i] = "A"

            elif mRNA[i] == "C":
                mRNA[i] = "G"

            elif mRNA[i] == "G":
                mRNA[i] = "C"

        return "".join(mRNA)


class RNAm(DNA):
    """Uma classe que representa um RNA mensageiro, que foi criado a partir de um DNA, representado pelas letras 'U', 'A', 'C' e 'G'."""

    def verify(self):
        """É um método que vai verificar se o a sequência realmente representa um RNA"""

        validRNA = True

        for nucleotide in self.seq:

            if nucleotide != 'A' and nucleotide != 'C' and nucleotide != 'G' and nucleotide != 'U':
                validRNA = False

        return validRNA

    def transcription(self):
        """Método que fará a sintese do mDNA a partir do RNA mensageiro (trancrição reversa)."""

        mDNA = list(self.seq)

        for i in range(len(mDNA)):

            if mDNA[i] == "A":
                mDNA[i] = "T"

            elif mDNA[i] == "U":
                mDNA[i] = "A"

            elif mDNA[i] == "C":
                mDNA[i] = "G"

            elif mDNA[i] == "G":
                mDNA[i] = "C"

        return "".join(mDNA)

    def tradution(self):
        """Método que criará a representação da proteína criada a partir do RNA mensageiro."""

        codon = {
            'F': ['UUU', 'UUC'],
            'M': ['AUG'],
            'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'I': ['AUU', 'AUC', 'AUA'],
            'V': ['GUU', 'GUC', 'GUA', 'GUG'],
            'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
            'P': ['CCU', 'CCC', 'CCA', 'CCG'],
            'T': ['ACU', 'ACC', 'ACA', 'ACG'],
            'A': ['GCU', 'GCC', 'GCA', 'GCG'],
            'Y': ['UAU', 'UAC'],
            'Stop': ['UAA', 'UAG', 'UGA', 'UGG'],
            'H': ['CAU', 'CAC'],
            'Q': ['CAA', 'CAG'],
            'N': ['AAU', 'AAC'],
            'K': ['AAA', 'AAG'],
            'D': ['GAU', 'GAC'],
            'E': ['GAA', 'GAG'],
            'C': ['UGU', 'UGC'],
            'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'G': ['GGU', 'GGC', 'GGA', 'GGG']
        }

        mRNA = self.seq
        print(mRNA)
        protein = []

        for n in range(0, len(mRNA) + 1, 3):
            for key in codon:
                if mRNA[n: n + 3] in codon[key]:
                    if key == 'Stop':
                        break
                    else:
                        protein.append(key)

        return ''.join(protein)


seq = input("digite uma sequencia: ")
dna1 = DNA(seq)

print(dna1.verify())
seq2 = dna1.transcription()
print(seq2)
rna1 = RNAm(seq2)
print(rna1.verify())
dnam = rna1.transcription()
print(dnam)
protein = rna1.tradution()
print(protein)

"""class Myapp:
  '''Cria a classe Myapp que comporta a janela do programa.'''
  def __init__(self, master):
    self.__master = master

    menucima = Menu(self.__master)
    self.__master.configure(menu = menucima)

    menu_acoes = Menu(menucima, tearoff=0)
    menucima.add_cascade(label='Ações', menu = menu_acoes)

    menu_acoes.add_command(label='Sair', command = self.aoClicarsair)

    menu_genoma = Menu(menucima, tearoff=0)
    menucima.add_cascade(label='Genoma', menu = menu_genoma)

    menu_genoma.add_command(label = 'Transcrever', command = self.aoClicartransc())
    menu_genoma.add_command(label = 'Traduzir', command = self.aoClicartraduzir())

    self.__framesup = Frame(self.__master)
    self.__framesup.grid(row=0, column=0)

    self.__frameinf = Frame(self.__master)
    self.__frameinf.grid(row=1, column=0)

    self.labdna = Label(self.__framesup, text='Informe o DNA:')
    self.labdna.grid(row=0, column=0)


    self.__dna = Entry(self.__framesup)
    self.__dna.grid(row=0, column=1)

    transc = Button(self.__framesup, text='Transcrever',command=self.aoClicartransc)
    transc.grid(row=1, column=1)

  def aoClicartransc(self):
     pass

  def aoClicartraduzir(self):
      pass

  def aoClicarsair(self):
      pass


root = Tk()
root.geometry('400x400')
root.title('Manipulação do genoma')
app = Myapp(root)
root.mainloop()"""
