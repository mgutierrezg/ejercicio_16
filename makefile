grafica.pdf: album.txt grafica.py
	python grafica.py
album.txt: album
	./album > album.txt
album: album.cpp
	c++ album.cpp -o album
