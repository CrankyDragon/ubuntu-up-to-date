all: setup build

setup:
	python configure.py

build:
	packer build -var-file=./variables.json ubuntu.json

check:
	packer inspect ubuntu.json

debug:
	packer build --debug -var-file=./variables.json ubuntu.json
