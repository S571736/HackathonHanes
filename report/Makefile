#
# General purpose Makefile for LaTeX
# 
# The Makefile is licensed under MIT
# and is part of the Pinit project.
#
# Author: Preben Vangberg
# Since: 23.02.2019 
#
# A Makefile for Latex Compiles all files containing \begin{document}
# The resulting PDF got the same name, and will be in the same folder
# in out as in src.
#
# It will always trippel compile a document in case bibtex or
# makeindex is called.
#
# Also contains conditional compiling for:
#
# - Bibtex if bibliography{ is found in the file.
# - Makeindex if makeglossiaries is found in the file.
#
# A change in one tex file will result in that file being
# recompiled, unless it is a file found in img, lib, or is
# a tex file without \begin{document} as then all pdfs will
# be recompiled.
#

# Latex -> PDF compiler
COMPILER := pdflatex

# Additional compiler parameters
PARAM := -halt-on-error 

# Where to push the wall of text produced by Pdflatex
# Uncomment to push most text to /dev/null
AFTER := # > /dev/null 2>&1 #| grep '^!.*' -A200 --color=always

# Folders used
SRCDIR := src
OBJDIR := obj
OUTDIR := out
LIBDIR := lib
IMGDIR := img

# List of all .tex files
SEARCH_TERM := "begin{document}"

# Documents that are to be compiled
TEXS := $(shell grep -rl --include \*.tex $(SEARCH_TERM) $(SRCDIR))

# Other tex files which might be included by other tex files.
OTHER_TEXS := $(shell grep -rL --include \*.tex $(SEARCH_TERM) $(SRCDIR))

# Everything in the lib folder / img folder
LIBS := $(shell find $(LIBDIR) $(IMGDIR) -name "*")

# List of all the pdfs we want, created by subst
# the extension of the .tex files and changing the
# path
PDFS := $(subst $(SRCDIR),$(OUTDIR),$(TEXS:.tex=.pdf))

# Create all the pdfs.
target: $(PDFS) 

$(OUTDIR)/%.pdf: $(OBJDIR)/%.pdf 
	@mkdir -p $(@D)
	@cp $< $@

# Compile one .tex file
$(OBJDIR)/%.pdf: $(SRCDIR)/%.tex $(LIBS) $(OTHER_TEXS)
	@mkdir -p $(@D)
	@$(info Compiling: $< -> $@)
	@$(COMPILER) $(PARAM) -output-directory=$(@D) $< $(AFTER)
# Run bibtex if bibliography is found on an uncommented line.
	@if [ $(shell grep -c "^[^%]*bibliography{" $<) -gt 0 ]; then\
		echo "Compiling Bibtex";\
		bibtex $(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)) $(AFTER);\
	fi
# Compile glossaries and abbriviations using makeindex
# if makeglossaries is on a uncommented line.
	@if [ $(shell grep -c "^[^%]*makeglossaries" $<) -gt 0 ]; then\
		echo "Compiling Glossaries and Abbriviations";\
		makeindex -s $(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).ist -t\
	   		$(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).glg\
			-o $(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).gls\
			$(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).glo;\
		makeindex -s $(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).ist -t\
	   		$(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).alg\
			-o $(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).acr\
			$(subst $(SRCDIR),$(OBJDIR),$(subst .tex,,$<)).acn;\
	fi
	@$(COMPILER) $(PARAM) -output-directory=$(@D) $< $(AFTER)
	@$(COMPILER) $(PARAM) -output-directory=$(@D) $< $(AFTER)
	@echo ""

	
# Some phony bois
.PHONY: clean all

# Cleans all the aux files and pfds and rebuild
# everything
all: clean target

# removes all the aux and pdf files
clean: 
	@rm -rf $(OUTDIR) $(OBJDIR) 2>/dev/null || true
	@$(info Cleaning auxilerary and output files)
	@$(info )


