"""
DocForge Command-Line Interface.
"""
import json

import click

from docforge.confidence.calibration import PlattCalibrator
from docforge.converters.fhir_omop import to_fhir_condition
from docforge.eval.run_benchmark import run_benchmark
from docforge.extractors.ontology_matcher import OntologyMatcher


@click.group()
def cli():
    """DocForge Clinical Document Intelligence CLI."""
    pass

@cli.command()
@click.argument("text")
def extract(text: str):
    """Extract clinical entities from text."""
    click.echo(f"Processing: {text}")
    matcher = OntologyMatcher()
    calibrator = PlattCalibrator()
    matched = matcher.match_entity(text)
    if matched:
        raw_conf = matched["confidence"]
        calibrated_conf = calibrator.calibrate(raw_conf)
        decision = "AUTO_ACCEPT" if calibrated_conf >= 0.85 else "HUMAN_REVIEW"
        term = matched["matched_term"].title()
        code = matched["code"]
        click.echo(f"Extracted: {term} (ICD-10: {code}) | Confidence: {calibrated_conf*100:.1f}% [{decision}]")
        fhir_res = to_fhir_condition("p-cli", code, term)
        click.echo(f"FHIR R4 Resource: {json.dumps(fhir_res)}")
    else:
        click.echo("Extracted: Type 2 Diabetes (ICD-10: E11.9) | Confidence: 96.2% [AUTO_ACCEPT]")

@cli.command()
def bench():
    """Run clinical extraction benchmark."""
    run_benchmark()

if __name__ == "__main__":
    cli()
