from docforge.models.spec import ExtractionPipelineSpec, PipelineStep, StepType
from docforge.compiler.dag_compiler import compile_execution_order

def test_topological_sort():
    spec = ExtractionPipelineSpec(
        pipeline_id="clinical_note_v1",
        target_entities=["DIAGNOSIS", "MEDICATION"],
        steps=[
            PipelineStep(step_id="step1", step_type=StepType.REGEX_EXTRACTOR),
            PipelineStep(step_id="step2", step_type=StepType.ONTOLOGY_MATCHER, depends_on=["step1"]),
            PipelineStep(step_id="step3", step_type=StepType.CONFIDENCE_CALIBRATOR, depends_on=["step2"]),
        ]
    )
    order = compile_execution_order(spec)
    assert order == ["step1", "step2", "step3"]
