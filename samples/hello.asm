[SECTION .text]
global _start

_start: 
	jmp short ender
	

	starter:
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx

	mov eax, 4
	mov ebx, 1
	pop ecx
	mov edx, 5 
	int 0x80

	xor eax, eax
	mov eax, 1
	xor ebx, ebx
	int 0x80

	ender:
	call starter
	db 'hello'
