run:main
	./main
main: main.o
	ld main.o -o main
main.o: main.s
	nasm -f elf64 main.s -o main.o
main.s: main.py main.sic
	python3 main.py main.sic


clean:
	rm -rf main.s main.o main