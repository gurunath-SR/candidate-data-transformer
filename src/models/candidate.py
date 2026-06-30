from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str
    confidence: float = 0.0


class Experience(BaseModel):
    company: str
    role: str
    duration: Optional[str] = None


class Education(BaseModel):
    institution: str
    degree: str
    year: Optional[str] = None


class Candidate(BaseModel):

    candidate_id: Optional[str] = None

    full_name: Optional[str] = None

    emails: List[str] = Field(default_factory=list)

    phones: List[str] = Field(default_factory=list)

    location: Optional[str] = None

    headline: Optional[str] = None

    links: Dict[str, str] = Field(default_factory=dict)

    years_experience: float = 0.0

    skills: List[Skill] = Field(default_factory=list)

    experience: List[Experience] = Field(default_factory=list)

    education: List[Education] = Field(default_factory=list)

    provenance: Dict[str, str] = Field(default_factory=dict)

    # NEW
    field_confidence: Dict[str, float] = Field(default_factory=dict)

    overall_confidence: float = 0.0