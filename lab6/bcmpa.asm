%include "io.mac"
.CODE
	global main
	extern old_main

main:
      push	ebp
      mov	ebp, esp
      mov	ecx, DWORD[ebp+12]  ;save the argv[1] addres
      mov	edx, DWORD[ebp+8]	; save the argv[2] addres
	  call	open				;open both files and save the contant to ecx
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
	
write: ; i think it;s not in use
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
	inc		placeOfChar
	movzx	AX, BYTE [ecx]		; take one byte each time to AX	
	movzx	BX, BYTE [edx]		; take one byte each time to BX
	cmp	AX, 0 		; if ( str1[i] == 0 ) break;
	je	end
	cmp	BX, 0 		; if ( str2[i] == 0 ) break;
	je	end
	cmp AX,BX		;if not equal write the line
	jne printline
	je	continue
	
continue:	
	inc	ecx
	inc edx
	jmp diffloop

printline:
	PutStr msgSec1
	PutInt placeOfChar
	PutStr msgSec2
	PutInt AX
	PutStr msgSec3
	PutInt BX
	nwln
	jmp continue

	
end:	
	mov esp, ebp
	pop ebp
	ret
	
.DATA
		placeOfChar Dw 0
		msgSec1		Db 'byte ','\0'
		msgSec2		Db ' -','\0'
		msgSec3		Db ' +','\0'
		
		
