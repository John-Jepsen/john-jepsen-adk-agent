"""Function tools the agent uses to answer hiring-team questions.

Each tool returns structured data from profile.py so every factual claim
the agent makes is grounded in the resume and recommendation letter rather
than generated from model memory.
"""

from . import profile


def get_contact_info() -> dict:
    """Returns John's name, title, location, email, and GitHub profile."""
    return profile.CONTACT


def get_background() -> dict:
    """Returns John's professional summary, education, and career arc.

    Use this for questions like "tell me about yourself", "what is your
    background", or anything about education and career history at a glance.
    """
    return profile.BACKGROUND


def get_experience() -> dict:
    """Returns John's work history with detailed accomplishments per role.

    Use this for questions about his AI and software engineering experience,
    what he did at Qwasar, production systems he has run, or metrics and
    impact (users served, error reduction, applicants evaluated).
    """
    return {"experience": profile.EXPERIENCE}


def get_projects(project_name: str = "") -> dict:
    """Returns John's selected ML and software projects.

    Args:
        project_name: Optional. If provided, returns only projects whose
            name contains this string (case-insensitive). Leave empty to
            get all projects.
    """
    projects = profile.PROJECTS
    if project_name:
        needle = project_name.lower()
        matched = [p for p in projects if needle in p["name"].lower()]
        if matched:
            return {"projects": matched}
        return {
            "projects": [],
            "note": f"No project matching '{project_name}'. "
                    f"Available: {', '.join(p['name'] for p in projects)}",
        }
    return {"projects": projects}


def get_technical_skills(category: str = "") -> dict:
    """Returns John's technical skills, grouped by category.

    Args:
        category: Optional. One of: languages, machine_learning,
            ai_agents_and_llms, backend_and_systems, data_and_infrastructure,
            frontend, specialized, leadership. Leave empty for all categories.
    """
    skills = profile.SKILLS
    if category:
        key = category.lower().strip()
        if key in skills:
            return {key: skills[key]}
        return {
            "error": f"Unknown category '{category}'.",
            "available_categories": list(skills.keys()),
        }
    return skills


def get_role_fit() -> dict:
    """Returns why John is a strong fit for an AI/agent engineering role.

    Use this for questions like "why should we hire you", "why are you a
    good fit", or "what makes you different from other candidates".
    """
    return profile.ROLE_FIT


def get_recommendation() -> dict:
    """Returns quotes and context from John's letter of recommendation,
    written by the COO of Qwasar Silicon Valley.

    Use this for questions about references, what it is like to work with
    John, why he left his last role, or third-party validation of his work.
    """
    return profile.RECOMMENDATION


ALL_TOOLS = [
    get_contact_info,
    get_background,
    get_experience,
    get_projects,
    get_technical_skills,
    get_role_fit,
    get_recommendation,
]
