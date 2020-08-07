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
    print(int(r[i]))
    c += 2



# Instruction Set Class

class InstructionSet():
    def __init__(self, bin_or_int='int'):
        super().__init__()

        instructions_set = (
                ('10000010', ldi), # LDI R0,8
                ('01000111', prn), # PRN R0
                ('00000001', halt), # HLT
        )

        self.bin_or_int = bin_or_int
        self.instructions = self._build_instructions(instructions_set)

        
    def _sbin_to_int(self, line):
        return int(line, 2)


    def _convert_to_binary(self, line):
        return bin(int(f'0b{line}', 2))


    def _build_instructions(self, iset):
        instructions = {}
        if self.bin_or_int == 'int':
            fn = self._sbin_to_int
        else:
            fn = self._convert_to_binary
        
        for ins in iset:
            n = fn(ins[0])
            instructions[n] = ins[1]
        return instructions


    def _parse_op(self, code):
        return self._sbin_to_int(code) >> 6



    def __call__(self, code):
        try:
            return self.instructions[code]
        except KeyError:
            raise NotImplementedError(f'Code {c} not defined')
        except:
            raise
            