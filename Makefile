.PHONY: compile clean

compile:
	protoc -I=galatea-ipc --python_out=. galatea-ipc/*.proto

clean-mac:
	find . -name ".DS_Store" -print0 | xargs -0 rm
