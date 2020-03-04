lib:
	go build -o lib.so -buildmode=c-shared lib.go
	cc main.c ./lib.so

clean:
	rm -f lib.so a.out

.PHONY: lib clean
