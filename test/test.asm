main:
	push    rbp
    mov     eax, 8064
    call    ___chkstk_ms
    sub     rsp, rax
    lea     rbp, 128[rsp]
    call    __main
	subq	rsp, 120
	mov	DWORD PTR 8[rbp], 0
	mov	DWORD PTR 112[rbp], 1
	mov	DWORD PTR 108[rbp], 2
	mov	DWORD PTR 104[rbp], 3
.W4:
	mov	eax, DWORD PTR 8[rbp]
	cmp	eax, 20
	je	.code6
	jmp	.block6
.code6:
	mov	DWORD PTR 8[rbp], eax
	cltq
	mov	ecx, DWORD PTR 112[rbp+rax*4]
	mov	DWORD PTR 12[rbp], ecx
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T0[rip], eax
	mov	T0[rip], eax
	cltq
	mov	edx, DWORD PTR 112[rbp+rax*4]
	mov	eax, DWORD PTR 12[rbp]
	add	eax, edx
	mov	T1[rip], eax
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 2
	add	eax, edx
	mov	T2[rip], eax
	mov	T2[rip], eax
	cltq
	mov	ecx, T1[rip]
	mov	DWORD PTR 112[rbp+rax*4], ecx
	mov	eax, DWORD PTR 8[rbp]
	movl	edx, DWORD PTR 12[rbp]
	mov	esi, eax
	leaq	.LC0[rip], rdi
	mov	01h, eax
	call	printf@PLT
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T3[rip], eax
	mov	ecx, T3[rip]
	mov	DWORD PTR 8[rbp], ecx
	jmp	.W4
.block6:
	mov	esi, eax
	leaq	.LC1[rip], rdi
	mov	01h, eax
	call	printf@PLT

	mov	eax,0
	add	rsp, 8064
	pop	rbp
	ret
