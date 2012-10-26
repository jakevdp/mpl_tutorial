
convert_nb:
	rm -rf notebooks
	rm -rf notebooks_ex
	python strip_notebooks.py
	python nbconvert.py notebooks/*.ipynb
	python nbconvert.py notebooks_ex/*.ipynb