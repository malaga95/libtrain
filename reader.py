#Napisz program "reader.py", który zmodyfikuje plik csv i wyświetli w terminalu jego zawartość, a następnie zapisze w wybranej lokalizacji.
#Wykonanie programu:
#
#reader.py <src> <dst> <change1> <change2> ..
#src to ścieżka pliku csv. Jeśli plik nie istnieje bądź podana ścieżka nie jest plikiem, wyświetl błąd i wskaż pliki w tym samym katalogu.
#dst to docelowa ścieżka, w której zapiszemy zmieniony plik csv.
#
#change1 ... changeN to ciągi znaków w posraci "Y,X,wartosc" Y to wiersz do zmodyfikowania (liczony od 0, X to kolumna (liczona od 0). Komórka pod wskazanym adresem powinna zmienić wartość na "wartosc
import sys

class CsvReader:
    def __init__(self):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
        self.task = []
        self.lines = self.read_file()
        for c in sys.argv[3:]:
            self.task.append(c.split(','))
    
    def read_file(self):
        lines = []
        with open(self.input_file, 'r') as file:
            for line in file.readlines():
                #
                tmp = line.split('\n')[0].split(',')
                lines.append(tmp)
                #line.split[-1] = line.split[-1].split('\n')[0]
        return lines
    
    def modify(self):
       # lines = self.read_file
        for change in self.task:
            self.lines[int(change[0])][int(change[1])] = change [2]
    
    def __str__(self):
        return f'Input file : {self.input_file}; output file : {self.output_file}; changes : {self.task}'

    def save_file(self):
        with open(self.output_file, 'w') as file:
            for line in self.lines:
                for element in line[:-1]:
                    file.write(str(element)+',')
                file.write(str(line[-1] + '\n'))
read = CsvReader()
read.modify()
read.save_file()
#print(read.input_file,read.output_file,read.task)