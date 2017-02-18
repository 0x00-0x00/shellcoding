global _start

_start:
	; rax = 1, rdi = 1, rsi = string, rdx = len(string)
	xor rax, rax 
	mov rax, 0x21646c7241414141
	shr rax, 0x20
	push rax	
	mov rax, 0x6f57206f6c6c6548
	push rax
	push rsp
	pop rsi ; joga o endereco da string no rsi

	xor rax, rax ;zera o rax
	add rax, 0x1 ;rax = 1

	xor rdi, rdi
	add rdi, 0x1 ;rdi = 1

	xor rdx, rdx
	add rdx, 0xd
	syscall

	;sys_exit syscall => rax=60, rdi=error_code(0)
	xor rax, rax
	add rax, 0x3c ;rax=60

	xor rdi, rdi
	syscall
