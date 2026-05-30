from typing import Dict

from kedro.pipeline import Pipeline
from si_image_processing.pipelines.image_processing.pipeline import (
    create_pipeline,
)


def register_pipelines() -> Dict[str, Pipeline]:
    img_pipeline = create_pipeline()
    return {"__default__": img_pipeline, "image_processing": img_pipeline}