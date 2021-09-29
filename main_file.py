from parser import BasicParser
from lexer import BasicLexer
from execute import BasicExecute
import sys
def main(argv):
    inputfile = argv
    print(argv)
    file1 = open(argv, 'r')
    lexer = BasicLexer()
    parser = BasicParser()
    print('MikiScript Language')
    env = {}
    while True:
        try:
            text = line = file1.readline()
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)


if __name__ == "__main__":
   main(sys.argv[1])