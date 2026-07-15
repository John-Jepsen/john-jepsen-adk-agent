# John Jepsen — Career Agent (Google ADK)

An interactive AI agent, built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/), that lets a hiring team learn about me: my background, AI and software engineering experience, projects, technical skills, and why I fit the role.

**Live agent:** _deployment link goes here_
**Repository:** https://github.com/John-Jepsen/john-jepsen-adk-agent

Ask it things like:

- "Tell me about John's background."
- "What production AI systems has he built?"
- "Show me his machine learning projects."
- "What are his skills with agents and LLMs?"
- "Why is he a good fit for this role?"
- "What does his recommendation letter say?"

## Architecture

```
┌─────────────────────────────────────────────────┐
│  ADK Web UI / API  (Cloud Run)                  │
│  ┌───────────────────────────────────────────┐  │
│  │  root_agent  (gemini-2.5-flash)           │  │
│  │  grounded via function tools:             │  │
│  │   get_background      get_experience      │  │
│  │   get_projects        get_technical_skills│  │
│  │   get_role_fit        get_recommendation  │  │
│  │   get_contact_info                        │  │
│  └───────────────┬───────────────────────────┘  │
│                  │                               │
│         career_agent/profile.py                  │
│         (structured resume + recommendation      │
│          letter data — single source of truth)   │
└─────────────────────────────────────────────────┘
```

Design choices:

- **Every factual claim is tool-grounded.** The model is instructed to call a tool before answering, so it cites real numbers from my resume instead of hallucinating. Facts live in one place (`profile.py`); the tools in `tools.py` expose them with filtering (by project name, by skill category).
- **Honest about its limits.** Questions outside the profile (salary, availability) get a "not on file — email John" response instead of a guess.
- **Tested.** `pytest` covers every tool's contract and the agent wiring; CI runs on every push.

## Run it locally

```bash
git clone https://github.com/John-Jepsen/john-jepsen-adk-agent.git
cd john-jepsen-adk-agent
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your Gemini API key (free at https://aistudio.google.com/apikey)
adk web                # chat UI at http://localhost:8000
```

Or talk to it in the terminal with `adk run career_agent`.

## Tests

```bash
pip install pytest
pytest tests/ -q
```

## Deploy (Google Cloud Run)

```bash
gcloud auth login
adk deploy cloud_run \
  --project <YOUR_PROJECT> \
  --region us-central1 \
  --service_name john-jepsen-career-agent \
  --with_ui \
  ./career_agent
```

Set `GOOGLE_GENAI_USE_VERTEXAI=TRUE` on the service to use Vertex AI with the project's service account (no API key needed), or provide `GOOGLE_API_KEY` as a secret.

## Project structure

```
career_agent/
├── __init__.py     # exposes the agent to the ADK CLI
├── agent.py        # root_agent definition + system instruction
├── tools.py        # function tools (the agent's only source of facts)
└── profile.py      # structured resume + recommendation letter data
tests/
└── test_tools.py   # tool contracts + agent wiring
```

## Contact

**John Jepsen** — johnjepsen808@gmail.com — San Antonio, TX
GitHub: [@John-Jepsen](https://github.com/John-Jepsen)
