#############
#CONSTANTS
#############
DIGITS = '0123456789'
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#############
#ERRORS
#############

class Error:
    def __init__(self,error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)
#############
#TOKENS
#############

TT_STRING  = 'TT_STRING'
TT_INT     = 'TT_INT'
TT_LPAREN  = 'LPAREN'
TT_RPAREN  = 'RPAREN'
TT_EQUAL   = 'EQUAL'
TT_LINE    = 'LINE'
TT_DOTS    = 'TWO DOTS'

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

##############
#LEXER
##############

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos  = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos +=1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in ALPHABET:
                tokens.append(self.make_word())
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TT_EQUAL))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_LINE))
                self.advance()
            elif self.current_char == ':':
                tokens.append(Token(TT_DOTS))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'"+ char + "'")

        return tokens, None


    def make_number(self):
        num_str = ''

        while self.current_char != None and self.current_char in DIGITS:
            num_str += self.current_char
            self.advance()
        return Token(int(num_str))
    def make_word(self):
        word_str = ''

        while self.current_char != None and self.current_char in ALPHABET:
            word_str += self.current_char
            self.advance()
        return Token(word_str)

##############
#RUN
##############

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error