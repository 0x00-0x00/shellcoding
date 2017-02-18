
	jmp ender

starter:
	xor rax, rax
	mov al, 4
	mov bl, 1
	pop rcx
	mov dl, 5
	int 0x80

	xor rax, rax
	mov al, 1
	mov bl, 0
	int 0x80
	

ender:
	call starter
	db 'Test'
