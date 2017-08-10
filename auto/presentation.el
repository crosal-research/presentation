(TeX-add-style-hook
 "presentation"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("beamer" "12pt" "presentation" "t")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("ccicons" "scale=2") ("standalone" "subpreambles=true") ("hyperref" "linktocpage=true") ("babel" "portuguese" "english")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "beamer"
    "beamer12"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "appendixnumberbeamer"
    "booktabs"
    "ccicons"
    "pgfplots"
    "xspace"
    "standalone"
    "import"
    "babel")
   (TeX-add-symbols
    "themename")
   (LaTeX-add-labels
    "sec:orgfc3fdba"
    "sec:org677ccf0"
    "sec:org4abc11a"
    "sec:orgd39fd48")
   (LaTeX-add-xcolor-definecolors
    "mSybilaRed"
    "myBarRed"))
 :latex)

