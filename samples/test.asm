section .data:
    msg db 'Hello World!', 0

section .text:
    global _start

_start:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, 0xc
    int 0x80

exit:
    xor eax, eax
    mov eax, 1
    mov ebx, 0
    int 0x80