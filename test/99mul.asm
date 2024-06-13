main:
	push    rbp
    mov     eax, 8064
    call    ___chkstk_ms
    sub     rsp, rax
    lea     rbp, 128[rsp]
    call    __main
	subq	rsp, 12
	mov	DWORD PTR 4[rbp], 1
	mov	esi, eax
	leaq	.LC0[rip], rdi
	mov	01h, eax
	call	printf@PLT
.W2:
	mov	eax, DWORD PTR 4[rbp]
	cmp	eax, 10
	je	.code4
	jmp	.block4
.code4:
	mov	ecx, DWORD PTR 4[rbp]
	mov	DWORD PTR 8[rbp], ecx
.W7:
	mov	eax, DWORD PTR 8[rbp]
	cmp	eax, 10
	je	.code9
	jmp	.block9
.code9:
	mov	eax, DWORD PTR 8[rbp]
	imul	eax, DWORD PTR 4[rbp]
	mov	T0[rip], eax
	mov	eax, DWORD PTR 4[rbp]
	movl	edx, DWORD PTR 8[rbp]
	mov	ecx, T0[rip]
	mov	esi, eax
	leaq	.LC1[rip], rdi
	mov	01h, eax
	call	printf@PLT
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T1[rip], eax
	mov	ecx, T1[rip]
	mov	DWORD PTR 8[rbp], ecx
	jmp	.W7
.block9:
	mov	esi, eax
	leaq	.LC2[rip], rdi
	mov	01h, eax
	call	printf@PLT
	mov	edx, DWORD PTR 4[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T2[rip], eax
	mov	ecx, T2[rip]
	mov	DWORD PTR 4[rbp], ecx
	jmp	.W2
.block4:

	mov	eax,0
	add	rsp, 8064
	pop	rbp
	ret
