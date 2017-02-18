

SYSCALL_BLUEPRINT = """xor rax, rax
    mov rax, %s
    shr rax, %s
    push rax

    mov rax, %s
    push rax

    mov rax, %s
    push rax

    push rsp
    pop rsi

    xor rax, rax
    add rax, 0x1

    xor rdi, rdi
    add rdi, 0x1

    xor rdx, rdx
    add rdx, %s
    syscall
"""

class WriteCall(object):
    def __init__(self, data):
        self.data = data
        self.length = self._count_length()

    def _count_length(self):
        """
        Count byte size of hexadecimal data
        """
        n = 0
        for block in self.data:
            leng = (len(block) - 2) / 2
            n += leng
        return n

    def _shear_value(self, first_block):
        return hex(first_block.count("41"))

    def _insert_data(self, data):
        return "mov rax, %s\npush rax" % data

    def _construct(self):
        return SYSCALL_BLUEPRINT % ()

