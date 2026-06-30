from models.candidate import Skill


KNOWN_SKILLS = {

    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "react",
    "nodejs",
    "express",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "github",
    "linux",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "tensorflow",
    "keras",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "flask",
    "django"

}


class SkillExtractor:

    @staticmethod
    def extract(text):

        skills = []

        lower = text.lower()

        for skill in sorted(KNOWN_SKILLS):

            if skill in lower:

                skills.append(

                    Skill(

                        name=skill.title(),

                        confidence=0.95

                    )

                )

        return skills