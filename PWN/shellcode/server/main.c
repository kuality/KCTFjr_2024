#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>
#include <string.h>

void initalize() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stderr, 0, _IONBF, 0);
}

int main() {
    initalize();
    void* region = mmap(NULL, 0x1000, PROT_WRITE | PROT_READ | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    if(region == MAP_FAILED) {
        perror("mmap");
        return 1;
    }
    write(1, "input shellcode > ", 18);
    read(0, region, 0x100); 
    ((void(*)())region)();
    munmap(region, 0x1000);
}