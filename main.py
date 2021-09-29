from parser import BasicParser
from lexer import BasicLexer
from execute import BasicExecute
if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    print('MikiScript Language')
    env = {}
      
    while True:
          
        try:
            text = input('MikiScript Language > ')

        except EOFError:
            break
          
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)