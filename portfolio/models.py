"""
Different models for the portfolio project
"""
from enum import Enum
from dataclasses import dataclass

# ======================================= #
#                 ENUMS                   #
# ======================================= #


class EducationalType(Enum):
    """Educational Type information for the model"""
    UNIVERSITY = "university"
    LANGUAGE = "language"
    CERTIFICATE = "certificate"
    PUBLICATION = "publication"


# ======================================= #
#              DATACLASSES                #
# ======================================= #

@dataclass
class WorkExperienceModel:
    """Include a dataclass model for the Work information"""
    worked_date: str
    position_job: str
    company_and_city: str
    description_job: str
    software_skills: tuple[str, ...]


@dataclass
class EducationalModel:
    """Include a dataclass model for the educational information"""
    education_type: EducationalType
    study_subject: str
    educational_entity: str
    range_years: str
    description: str


@dataclass
class ProjectModel:
    """Include a dataclass model for the Project information"""
    project_title: str
    description: str
    url_github: str
    url_project: str
    project_image: str
    software_skills: tuple[str, ...]
