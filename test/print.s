	.text
	.section	.rodata
	.comm	T0,4,4
	.comm	T1,4,4
	.comm	T2,4,4
.LC0:
	.string "%c"
.LC1:
	.string "\n\n这个例子展示了在printf语句中的参数，可以是一个表达式。\n例如b*2+(4+5)*3=%d"
.LC2:
	.string "\n\n这个例子展示了数组内下标的可用变量表示，并且可递归嵌套\nintc=arr[arr[b+1]]=%d\n\n"
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
	subq	$24, %rsp
	movl	$1, -17(%rbp)
	movl	$0, -21(%rbp)
	movl	$0, -8(%rbp)
	movb	$97, -9(%rbp)
	movl	-8(%rbp), %edx
	movl	$1, %eax
	addl	%edx, %eax
	movl	%eax, T0(%rip)
	movl	-21(%rbp), %eax
	cltq
	movl	-21(%rbp, %rax, 4), %ecx
	movl	%ecx, -13(%rbp)
	movsbl	-9(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$2, %eax
	imull	-8(%rbp), %eax
	movl	%eax, T1(%rip)
	movl	T1(%rip), %edx
	movl	$27, %eax
	addl	%edx, %eax
	movl	%eax, T2(%rip)
	movl	T2(%rip), %eax
	movl	%eax, %esi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	-13(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC2(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT

	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.ident	"C2S"
