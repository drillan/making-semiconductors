# slides/Makefile
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build

revealjs:
	@$(SPHINXBUILD) -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" $(SPHINXOPTS)

livehtml:
	@sphinx-autobuild -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" \
		--ignore "*/_static/custom.css" --ignore "*/_static/custom.css.map" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
