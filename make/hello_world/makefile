.PHONY: all
all: source/hello.cpp source/world.cpp
	mkdir -p build
	g++ -c source/hello.cpp -o build/hello.o
	g++ -c source/world.cpp -o build/world.o

.PHONY: install
install: build/hello.o
	mkdir -p bin
	g++ -o bin/hello_world.exe build/hello.o build/world.o

clean: bin/hello_world.exe
	rm -rf build
	rm -rf bin



