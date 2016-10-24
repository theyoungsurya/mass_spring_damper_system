
all: ../output/Disp&Vel_vs_time.png  ../output/140010049.pdf ../output/Mass-Spring-Animation.mp4

../output/Disp&Vel_vs_time.png: main.py mass_spring_damper_system.py input.csv
	python main.py

../output/Mass-Spring-Animation.mp4: main.py mass_spring_damper_system.py input.csv
	python main.py
.ONESHELL:
../output/140010049.pdf: ../output/Disp&Vel_vs_time.png 140010049.tex
	pdflatex --output-directory=../output 140010049.tex
	cp -t ../output/  140010049.tex Undamped_free_vibrations.png spring-mass.png Forced_damped.png Damped_free.png Animation.html
	cd ../output/
	pdflatex 140010049.tex
	pdflatex 140010049.tex
	rm 140010049.tex Undamped_free_vibrations.png spring-mass.png Forced_damped.png Damped_free.png  *.lof *.log *.aux *.toc
