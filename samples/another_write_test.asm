global _start

_start:
	;write syscall

	;rax = 1
	;rdi = 1
	;rsi = string address
	;rdi = string length

	xor rax, rax
	mov rax, 0x61646e4141414141
	shr rax, 0x28
	push rax
	
	mov rax, 0x696c20796c656166
	push rax

	mov rax, 0x61722061206f6d41
	push rax

	push rsp
	pop rsi

	xor rax, rax
	add rax, 0x1

	xor rdi, rdi
	add rdi, 0x1

	xor rdx, rdx
	add rdx, 0x14
	syscall


	;exit syscall 
	;rax = 60
	;rdi = error code
	xor rax, rax
	add rax, 0x3c

	xor rdi, rdi
	syscall

	
