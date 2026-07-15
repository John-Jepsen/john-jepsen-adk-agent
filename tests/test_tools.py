"""Unit tests for the career agent's tools and agent wiring."""

from career_agent import tools
from career_agent.agent import root_agent


def test_contact_info_has_required_fields():
    contact = tools.get_contact_info()
    for key in ("name", "email", "github", "location"):
        assert contact[key]


def test_background_covers_summary_and_education():
    background = tools.get_background()
    assert "10,000" in background["summary"]
    assert background["education"]["school"] == "Woolf University"


def test_experience_includes_qwasar_role():
    experience = tools.get_experience()["experience"]
    assert any("Qwasar" in role["company"] for role in experience)
    assert all(role["highlights"] for role in experience)


def test_projects_returns_all_by_default():
    projects = tools.get_projects()["projects"]
    assert len(projects) >= 6


def test_projects_filters_by_name_case_insensitive():
    result = tools.get_projects("QKD")
    names = [p["name"] for p in result["projects"]]
    assert "qkd-avantheir" in names and "qkdsec" in names


def test_projects_unknown_name_lists_available():
    result = tools.get_projects("does-not-exist")
    assert result["projects"] == []
    assert "atari-games" in result["note"]


def test_skills_all_categories_nonempty():
    skills = tools.get_technical_skills()
    assert skills
    assert all(items for items in skills.values())


def test_skills_filters_by_category():
    result = tools.get_technical_skills("machine_learning")
    assert list(result.keys()) == ["machine_learning"]


def test_skills_unknown_category_reports_available():
    result = tools.get_technical_skills("underwater basket weaving")
    assert "available_categories" in result


def test_role_fit_has_pitch_and_reasons():
    fit = tools.get_role_fit()
    assert fit["pitch"]
    assert len(fit["reasons"]) >= 4


def test_recommendation_quotes_present():
    rec = tools.get_recommendation()
    assert "Jennifer Robertson" in rec["author"]
    assert len(rec["quotes"]) >= 3


def test_root_agent_is_wired():
    assert root_agent.name == "john_jepsen_career_agent"
    assert len(root_agent.tools) == len(tools.ALL_TOOLS)
    assert root_agent.instruction
