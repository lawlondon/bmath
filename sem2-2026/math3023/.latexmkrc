# Use pdflatex with shell-escape for tikz externalization
$pdflatex = 'pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Use biber (switch to bibtex if you're using natbib/plain bibtex instead)
$bibtex_use = 0;
$biber = 'biber %O %B';

# Always produce PDF via pdflatex
$pdf_mode = 1;

# Clean these extra files with latexmk -c
$clean_ext = 'synctex.gz run.xml bbl bcf fdb_latexmk';