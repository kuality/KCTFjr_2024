main : main.o
	gcc -o main main.o -no-pie -m32

main.o : main.c
	gcc -c -o main.o main.c -no-pie -m32

clean :
	rm *.o main