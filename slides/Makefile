# slides/Makefile
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build

revealjs:
	@$(SPHINXBUILD) -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" $(SPHINXOPTS)

livehtml:
	@sphinx-autobuild -b revealjs "$(SOURCEDIR)" "$(BUILDDIR)/revealjs" \
		--re-ignore "custom\.css" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
