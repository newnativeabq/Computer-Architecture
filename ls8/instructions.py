# instructions.py


# Common instructions

def halt(*args):
    return True


def ldi(*args):
    m, r, c = args
    cp = c.value
    i = int(m[cp+1])
    r[i] = m[cp+2]
    c += 3


def prn(*args):
    m, r, c = args
    cp = c.value
    i = int(m[cp+1])
    print(r[i])
    c += 2



# Instruction Set Class

class InstructionSet():
    instructions = {
            0b10000010: ldi, # LDI R0,8
            0b01000111: prn, # PRN R0
            0b00000001: halt, # HLT
    }

    def __call__(self, code):
        try:
            return self.instructions[code]
        except:
            raise NotImplementedError(f'Code {code} not defined')





