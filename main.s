section .data
	BETA db 230
section .text
global _start
_start:
	movzx rdi, byte [BETA]
	mov rax, 60
	syscall
