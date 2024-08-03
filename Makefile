all: build/client build/server

build:
	mkdir -p build

build/client.o: client.c | build
	gcc -Wall -Wextra -Werror -c client.c -o build/client.o

build/server.o: server.c | build
	gcc -Wall -Wextra -Werror -c server.c -o build/server.o

build/client: build/client.o
	gcc build/client.o -o build/client

build/server: build/server.o
	gcc build/server.o -o build/server

clean:
	rm -rf build

.PHONY: all clean

