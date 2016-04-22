.PHONY: compile clean

compile:
	protoc -I=galatea-ipc --python_out=. galatea-ipc/*.proto

clean:
	find . -name \*.pyc -delete

clean-mac: clean
	find . -name ".DS_Store" -print0 | xargs -0 rm
