global _start

_start:
jmp short str

code:
pop rsi
xor rax, rax
mov al, 1
mov rdi, rax
mov rdx, rdi
add rdx, 12
syscall

xor rax, rax
add rax, 60
xor rdi, rdi
syscall

str:
call code
db 'This Rocks!'
