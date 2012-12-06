section .text
	global main
	extern old_main

main:
      push	ebp
      mov	ebp, esp
      mov	ecx, DWORD[ebp+12]  ;save the argv[1] addres
      mov	edx, DWORD[ebp+8]	; save the argv[2] addres
	  call	open
	  call	read
	  mov	ebx,0
	  jmp	diffloop
	 
	 ; push	ecx
	  ;push	edx
     ; call	old_main
    ;  mov	esp, ebp
     ; pop	ebp
      ;ret	
	  
read:
	mov eax,3 ; linux system call- read
    mov ecx,[esp+8]
    mov edx,[esp+12]
	int 0x80	;execute the system call 
	ret
	
write:
	mov eax,4 ; linux system call- write
    mov ecx,[esp+8]
    mov edx,[esp+12]
	int 0x80	;execute the system call 
	ret
	
open:
	mov eax,5; linux system call- open
    mov ecx,[esp+8]
    mov edx,[esp+12]
	int 0x80	;execute the system call 
	ret
	
close:
	mov eax,6; linux system call- close
	mov ecx,[esp+8]
	mov edx, [esp+12]
	int 0x80	;execute the system call 
	ret

	
diffloop:
	movzx	ecx, BYTE [ecx]
	movzx	edx, BYTE [edx]
	cmp	ecx, 0 		; if ( str1[i] == 0 ) break;
	je	end
	cmp	edx, 0 		; if ( str2[i] == 0 ) break;
	je	end
	cmp ecx,edx		;if not equal write the line
	jne printline
	je	continue
	
continue:	
	inc	bx
	jmp diffloop

printline:
	call write
	jmp continue

	
end:	
	mov esp, ebp
	pop ebp
	ret
	
section .data
		;placeOfChar Dw 1
		;chNew	DW ?
		;chOld	DW ?
