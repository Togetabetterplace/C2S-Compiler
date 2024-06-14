	.text
	.section	.rodata
	.comm	T0,4,4
	.comm	T1,4,4
	.comm	T2,4,4
	.comm	T3,4,4
	.comm	T4,4,4
	.comm	T5,4,4
	.comm	T6,4,4
	.comm	T7,4,4
	.comm	T8,4,4
	.comm	T9,4,4
	.comm	T10,4,4
	.comm	T11,4,4
	.comm	T12,4,4
	.comm	T13,4,4
	.comm	T14,4,4
	.comm	T15,4,4
	.comm	T16,4,4
	.text
	.globl	main
	.type	main, @function
main:

	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$8028, %rsp
	movl	$0, -4(%rbp)
	movl	$0, -8(%rbp)
	movl	$1, -12(%rbp)
	movb	$82, -17(%rbp)
	movl	$112, -12(%rbp)
.W4:
	movl	-12(%rbp), %eax
	cmpl	$1000, %eax
	jle	.block9
	movl	-12(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T0(%rip)
	movl	T0(%rip), %ecx
	movl	%ecx, -12(%rbp)
	movl	-8(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T1(%rip)
	movl	T1(%rip), %ecx
	movl	%ecx, -8(%rbp)
	movl	-12(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T2(%rip)
	movl	T2(%rip), %ecx
	movl	%ecx, -12(%rbp)
	movl	-12(%rbp), %eax
	cltq
	movl	$1, -8021(%rbp, %rax, 4)
	jmp	.W4
.block9:
	movl	-8(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T3(%rip)
	movl	T3(%rip), %ecx
	movl	%ecx, -8(%rbp)
	movl	-12(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T4(%rip)
	movl	T4(%rip), %ecx
	movl	%ecx, -12(%rbp)
	movl	-12(%rbp), %eax
	cltq
	movl	$1, -8021(%rbp, %rax, 4)
	movl	-12(%rbp), %edx
	movl	$900, %eax
	subl	%edx, %eax
	movl	%eax, T5(%rip)
	movl	T5(%rip), %ecx
	movl	%ecx, -12(%rbp)
	movl	$1, -12(%rbp)
.W23:
	movl	-12(%rbp), %eax
	cmpl	$100, %eax
	jle	.block28
	movl	-12(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T6(%rip)
	movl	T6(%rip), %ecx
	movl	%ecx, -12(%rbp)
	movl	-8(%rbp), %edx
	movl	$1, %eax
	subl	%edx, %eax
	movl	%eax, T7(%rip)
	movl	T7(%rip), %ecx
	movl	%ecx, -8(%rbp)
	movl	-12(%rbp), %eax
	cltq
	movl	-8021(%rbp, %rax, 4), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T8(%rip)
	movl	-12(%rbp), %eax
	cltq
	movl	T8(%rip), %ecx
	movl	%ecx, -8021(%rbp, %rax, 4)
	jmp	.W23
.block28:
	movl	-8(%rbp), %edx
	movl	$1, %eax
	subl	%edx, %eax
	movl	%eax, T9(%rip)
	movl	T9(%rip), %ecx
	movl	%ecx, -8(%rbp)
	movl	-12(%rbp), %eax
	cltq
	movl	-8021(%rbp, %rax, 4), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T10(%rip)
	movl	-12(%rbp), %eax
	cltq
	movl	T10(%rip), %ecx
	movl	%ecx, -8021(%rbp, %rax, 4)
	movl	$0, -21(%rbp)
.W39:
	movl	-8(%rbp), %eax
	cmpl	-21(%rbp), %eax
	jle	.code41
	jmp	.block41
.code41:
	movl	-8(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T11(%rip)
	movl	T11(%rip), %ecx
	movl	%ecx, -8(%rbp)
.W45:
	movl	-4(%rbp), %eax
	cmpl	$10240, %eax
	jle	.code47
	jmp	.block47
.code47:
	movl	-4(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T12(%rip)
	movl	T12(%rip), %ecx
	movl	%ecx, -4(%rbp)
	movl	-4(%rbp), %eax
	cmpl	$100, %eax
	jg	.code52
	jmp	.block52
.code52:
	movl	-4(%rbp), %edx
	movl	$9, %eax
	addl	%edx, %eax
	movl	%eax, T13(%rip)
	movl	T13(%rip), %ecx
	movl	%ecx, -4(%rbp)
	movl	-8(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T14(%rip)
	movl	T14(%rip), %ecx
	movl	%ecx, -8(%rbp)
.block52:
	movl	-4(%rbp), %eax
	cltq
	movl	-4(%rbp), %ecx
	movl	%ecx, -8021(%rbp, %rax, 4)
	jmp	.W45
.block47:
	jmp	.W39
.block41:
.W64:
	movl	-4(%rbp), %eax
	cmpl	$0, %eax
	jg	.code66
	jmp	.block66
.code66:
	movl	-4(%rbp), %edx
	movl	$1, %eax
	subl	%edx, %eax
	movl	%eax, T15(%rip)
	movl	T15(%rip), %ecx
	movl	%ecx, -4(%rbp)
.W70:
	movl	-8(%rbp), %eax
	cmpl	$0, %eax
	jg	.code72
	jmp	.block72
.code72:
	movl	-8(%rbp), %edx
	movl	$1, %eax
	subl	%edx, %eax
	movl	%eax, T16(%rip)
	movl	T16(%rip), %ecx
	movl	%ecx, -8(%rbp)
	jmp	.W70
.block72:
	jmp	.W64
.block66:

	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.ident	"C2S"
