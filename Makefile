all: public/index.html

public/index.html: .github/workflows/index.yml tools/branch-from-ref.py tools/nfkc.py Makefile
	black **/*.py && \
	pylama **/*.py && \
	python3 ./tools/nfkc.py --fix && \
	npm install && \
	npm run build
