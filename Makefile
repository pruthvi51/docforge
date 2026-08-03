.PHONY: help setup test demo bench paper clean

help:
	@echo "DocForge Document Intelligence Commands:"
	@echo "  make setup     Install dependencies with uv"
	@echo "  make test      Run unit and pipeline test suite"
	@echo "  make demo      Launch Streamlit HITL clinician review queue"
	@echo "  make bench     Run extraction accuracy & Platt calibration benchmark"
	@echo "  make paper     Compile LaTeX research technical report with tectonic"

setup:
	uv pip install -e ".[dev]"

test:
	pytest -v tests/

demo:
	streamlit run ui/app.py

bench:
	python3 -m docforge.eval.run_benchmark

paper:
	cd paper && tectonic docforge_architecture_paper.tex

clean:
	rm -rf .pytest_cache manifests/ output/ target/
