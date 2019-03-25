""" Package constants """

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


# Compute-related
DEFAULT_COMPUTE_RESOURCES_NAME = "default"
SAMPLE_NAME_COLNAME = "sample_name"
COMPUTE_CONSTANTS = ["DEFAULT_COMPUTE_RESOURCES_NAME", "SAMPLE_NAME_COLNAME"]

# Project-related
DATA_SOURCES_SECTION = "data_sources"
DERIVATIONS_DECLARATION = "derived_attributes"
IMPLICATIONS_DECLARATION = "implied_attributes"
METADATA_KEY = "metadata"
SAMPLE_INDEPENDENT_PROJECT_SECTIONS = \
        [METADATA_KEY, DERIVATIONS_DECLARATION, IMPLICATIONS_DECLARATION, "trackhubs"]
PROJECT_CONSTANTS = ["DATA_SOURCES_SECTION", "IMPLICATIONS_DECLARATION",
                     "SAMPLE_INDEPENDENT_PROJECT_SECTIONS"]

# Sample-related
ASSAY_KEY = "protocol"
DATA_SOURCE_COLNAME = "data_source"
SAMPLE_ANNOTATIONS_KEY = "sample_annotation"
SAMPLE_SUBANNOTATIONS_KEY = "sample_subannotation"
SAMPLE_EXECUTION_TOGGLE = "toggle"
VALID_READ_TYPES = ["single", "paired"]
REQUIRED_INPUTS_ATTR_NAME = "required_inputs_attr"
ALL_INPUTS_ATTR_NAME = "all_inputs_attr"
SAMPLE_CONSTANTS = ["ALL_INPUTS_ATTR_NAME", "ASSAY_KEY", "DATA_SOURCE_COLNAME",
                    "REQUIRED_INPUTS_ATTR_NAME", "SAMPLE_ANNOTATIONS_KEY",
                    "SAMPLE_EXECUTION_TOGGLE", "VALID_READ_TYPES"]

# Other
FLAGS = ["completed", "running", "failed", "waiting", "partial"]
GENERIC_PROTOCOL_KEY = "*"
OTHER_CONSTANTS = ["FLAGS", "GENERIC_PROTOCOL_KEY"]


__all__ = COMPUTE_CONSTANTS + PROJECT_CONSTANTS + \
          SAMPLE_CONSTANTS + OTHER_CONSTANTS
