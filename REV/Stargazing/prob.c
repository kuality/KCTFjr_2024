#include <stdio.h>
#include <string.h>

void werqerczxcv(char *str) {
    while (*str) {
        __asm__(
            "movb (%0), %%al;"       
            "xorb $0xAA, %%al;"     
            "addb $0x03, %%al;"     
            "movb %%al, (%0);"       
            :                       
            : "r"(str)             
            : "%al"          
        );
        str++;
    }
}

int main() {
    char adfasdfas[] = { 0xe4, 0xec, 0x101, 0xef, 0xf8, 0xe3, 0xdb, 0xd4, 0xf0, 0xa1, 0xd3, 0x9c, 0xf8, 0xa1, 0xc7, 0xd1, 0xf8, 0xdb, 0x9c, 0xff, 0x9c, 0xdb, 0xdc, 0x9c, 0xf8, 0x9d, 0xcb, 0xef, 0xe2, 0xdc, 0xec, 0xa1, 0xe1, 0x9e, 0x9d, 0xe7, 0xda };

    printf("DO NOT LOOK AT THE MOON. PLEASE FALL ASLEEP AND REFRAIN FROM LOOKING OUTSIDE.");
    return 0;
}
