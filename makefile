#
# Makefile for SDES assignment
#

build:
	cd ./source && make all

clean:
	rm -rf output
	rm -rf source/__pycache__
	rm -f source/*.pyc source/*.aux source/*.log source/*.pdf


