main:
	push    rbp
    mov     eax, 8064
    call    ___chkstk_ms
    sub     rsp, rax
    lea     rbp, 128[rsp]
    call    __main
	subq	rsp, 8028
	mov	DWORD PTR 4[rbp], 0
	mov	DWORD PTR 8[rbp], 0
	mov	DWORD PTR 12[rbp], 1
	mov	DWORD PTR 17[rbp], 82
	mov	DWORD PTR 12[rbp], 112
.W4:
	mov	eax, DWORD PTR 12[rbp]
	cmp	eax, 1000
	je	.block9
	mov	edx, DWORD PTR 12[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T0[rip], eax
	mov	ecx, T0[rip]
	mov	DWORD PTR 12[rbp], ecx
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T1[rip], eax
	mov	ecx, T1[rip]
	mov	DWORD PTR 8[rbp], ecx
	mov	edx, DWORD PTR 12[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T2[rip], eax
	mov	ecx, T2[rip]
	mov	DWORD PTR 12[rbp], ecx
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	DWORD PTR 8021[rbp+rax*4], 1
	jmp	.W4
.block9:
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T3[rip], eax
	mov	ecx, T3[rip]
	mov	DWORD PTR 8[rbp], ecx
	mov	edx, DWORD PTR 12[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T4[rip], eax
	mov	ecx, T4[rip]
	mov	DWORD PTR 12[rbp], ecx
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	DWORD PTR 8021[rbp+rax*4], 1
	mov	edx, DWORD PTR 12[rbp]
	mov	eax, 900
	sub	eax, edx
	mov	T5[rip], eax
	mov	ecx, T5[rip]
	mov	DWORD PTR 12[rbp], ecx
	mov	DWORD PTR 12[rbp], 1
.W23:
	mov	eax, DWORD PTR 12[rbp]
	cmp	eax, 100
	je	.block28
	mov	edx, DWORD PTR 12[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T6[rip], eax
	mov	ecx, T6[rip]
	mov	DWORD PTR 12[rbp], ecx
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	sub	eax, edx
	mov	T7[rip], eax
	mov	ecx, T7[rip]
	mov	DWORD PTR 8[rbp], ecx
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	edx, DWORD PTR 8021[rbp+rax*4]
	mov	eax, 1
	add	eax, edx
	mov	T8[rip], eax
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	ecx, T8[rip]
	mov	DWORD PTR 8021[rbp+rax*4], ecx
	jmp	.W23
.block28:
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	sub	eax, edx
	mov	T9[rip], eax
	mov	ecx, T9[rip]
	mov	DWORD PTR 8[rbp], ecx
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	edx, DWORD PTR 8021[rbp+rax*4]
	mov	eax, 1
	add	eax, edx
	mov	T10[rip], eax
	mov	DWORD PTR 12[rbp], eax
	cltq
	mov	ecx, T10[rip]
	mov	DWORD PTR 8021[rbp+rax*4], ecx
	mov	DWORD PTR 21[rbp], 0
.W39:
	mov	eax, DWORD PTR 8[rbp]
	cmp	eax, DWORD PTR 21[rbp]
	je	.code41
	jmp	.block41
.code41:
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T11[rip], eax
	mov	ecx, T11[rip]
	mov	DWORD PTR 8[rbp], ecx
.W45:
	mov	eax, DWORD PTR 4[rbp]
	cmp	eax, 10240
	je	.code47
	jmp	.block47
.code47:
	mov	edx, DWORD PTR 4[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T12[rip], eax
	mov	ecx, T12[rip]
	mov	DWORD PTR 4[rbp], ecx
	mov	eax, DWORD PTR 4[rbp]
	cmp	eax, 100
	jg	.code52
	jmp	.block52
.code52:
	mov	edx, DWORD PTR 4[rbp]
	mov	eax, 9
	add	eax, edx
	mov	T13[rip], eax
	mov	ecx, T13[rip]
	mov	DWORD PTR 4[rbp], ecx
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	add	eax, edx
	mov	T14[rip], eax
	mov	ecx, T14[rip]
	mov	DWORD PTR 8[rbp], ecx
.block52:
	mov	DWORD PTR 4[rbp], eax
	cltq
	mov	ecx, DWORD PTR 4[rbp]
	mov	DWORD PTR 8021[rbp+rax*4], ecx
	jmp	.W45
.block47:
	jmp	.W39
.block41:
.W64:
	mov	eax, DWORD PTR 4[rbp]
	cmp	eax, 0
	jg	.code66
	jmp	.block66
.code66:
	mov	edx, DWORD PTR 4[rbp]
	mov	eax, 1
	sub	eax, edx
	mov	T15[rip], eax
	mov	ecx, T15[rip]
	mov	DWORD PTR 4[rbp], ecx
.W70:
	mov	eax, DWORD PTR 8[rbp]
	cmp	eax, 0
	jg	.code72
	jmp	.block72
.code72:
	mov	edx, DWORD PTR 8[rbp]
	mov	eax, 1
	sub	eax, edx
	mov	T16[rip], eax
	mov	ecx, T16[rip]
	mov	DWORD PTR 8[rbp], ecx
	jmp	.W70
.block72:
	jmp	.W64
.block66:

	mov	eax,0
	add	rsp, 8064
	pop	rbp
	ret
