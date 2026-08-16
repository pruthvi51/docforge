"""
Pydantic v2 Models for DocForge Extraction Pipelines.
"""
from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class StepType(str, Enum):
    REGEX_EXTRACTOR = "REGEX_EXTRACTOR"
    ONTOLOGY_MATCHER = "ONTOLOGY_MATCHER"
    LLM_EXTRACTOR = "LLM_EXTRACTOR"
    CONFIDENCE_CALIBRATOR = "CONFIDENCE_CALIBRATOR"

class PipelineStep(BaseModel):
    step_id: str
    step_type: StepType
    depends_on: List[str] = Field(default_factory=list)
    config: Dict[str, Any] = Field(default_factory=dict)

class ExtractionPipelineSpec(BaseModel):
    pipeline_id: str
    target_entities: List[str]
    confidence_threshold: float = 0.85
    steps: List[PipelineStep]
