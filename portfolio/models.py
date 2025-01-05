"""
Different models for the portfolio project
"""
from typing import Optional
from enum import Enum
from dataclasses import dataclass

# ======================================= #
#                 ENUMS                   #
# ======================================= #


class EducationalType(Enum):
    """Educational Type information for the model"""
    UNIVERSITY = "university"
    LANGUAGE = "languages"
    CERTIFICATE = "file-badge"
    PUBLICATION = "test-tubes"


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
    url: Optional[str] = None


@dataclass
class ProjectModel:
    """Include a dataclass model for the Project information"""
    project_title: str
    project_image: str
    description: str
    software_skills: tuple[str, ...]
    url_project: Optional[str] = None
    url_github: Optional[str] = None


@dataclass
class OpenSourceModel:
    """Include a dataclass model for the OpenSource code"""
    project_title: str
    project_image: str
    description: str
    software_skills: tuple[str, ...]
    url_project: Optional[str] = None
    url_github: Optional[str] = None


@dataclass
class WorkVisaModel:  # pylint: disable=R0902
    """Include a dataclass model for the Visa information"""
    visa_name: str
    country: str
    description: str
    eligibility_conditions: str
    duration: str
    application_fee: float
    processing_time: str
    required_documents: list[str]
    application_link: str
