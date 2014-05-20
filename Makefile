exe: main.cpp Cubitos.o Rubik.o
	g++ -g -o exe main.cpp Cubitos.o Rubik.o

Cubitos.o: Cubitos.h Cubitos.cpp
	g++ -c Cubitos.cpp

Rubik.o: Rubik.h Rubik.cpp Cubitos.o
	g++ -c Rubik.cpp

clean:
	rm *.o
	rm *~
