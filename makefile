run:main
	./main
main: main.o
	ld main.o -o main
main.o: main.s
	nasm -f elf64 main.s -o main.o
main.s: main.py test.sic
	python3 main.py test.sic