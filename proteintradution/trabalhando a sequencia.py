import copy


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

        mRNA = self.seq.replace('T', 'U')

        return mRNA

    def juntar_exons(self, exons):
        "Método que irá excluir os introns da sequencia de DNA para não ocerrer erros futuros na tradução da proteína."

        seq = list(self.seq)
        seq_semintrons = []

        for num in range(0,len(exons),2):
            intervalo = "".join(seq[exons[num]: exons[num+1]])
            seq_semintrons.append(intervalo)

        return "".join(seq_semintrons)


seq_dada = input().upper()
modifyseq = seq_dada.split(" ")
count = 0
newseq = []
while count < len(modifyseq):
    if not modifyseq[count].isnumeric() or modifyseq[count] == " " or modifyseq[count] == "":
        print(modifyseq[count])
        newseq.append(modifyseq[count])

    count += 1

newseq = "".join(newseq)

print(newseq)

qtd_exons = int(input("quantos exons tem nessa seq? "))
exons = []

for i in range(qtd_exons):
    print(f"coloque o intervalo do {i + 1}º exon")
    intervalo1 = int(input("Coloque o inicio do intervalo: "))
    exons.append(intervalo1)

    intervalo2 = int(input("Coloque o final do intervalo: "))
    exons.append(intervalo2)

dna = DNA(newseq)
print(dna.verify())
dnacod = dna.juntar_exons(exons)
print(dnacod)