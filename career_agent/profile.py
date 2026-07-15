"""Structured career profile data for John Jepsen.

This module is the single source of truth the agent's tools draw from.
Content is sourced from John's resume and his letter of recommendation
from Qwasar's COO (June 2026).
"""

CONTACT = {
    "name": "John Jepsen",
    "title": "Machine Learning Engineer | Software Engineer | AI Product Engineer",
    "location": "San Antonio, TX",
    "email": "johnjepsen808@gmail.com",
    "github": "https://github.com/John-Jepsen",
}

BACKGROUND = {
    "summary": (
        "Software engineer and machine learning engineer with 5+ years of "
        "experience building production platforms, ML-powered features, AI "
        "agents, and SaaS systems serving more than 10,000 users across the "
        "United States, Europe, and Africa. At Qwasar Silicon Valley, served "
        "as Software Engineer and Director of Programming, leading engineering "
        "execution, platform development, AI initiatives, and educational "
        "program delivery across multiple live products."
    ),
    "education": {
        "degree": "M.S., Software Engineering & Machine Learning",
        "school": "Woolf University",
        "completion": "July 2026",
        "focus": (
            "machine learning systems, applied AI, distributed software "
            "architecture, deep reinforcement learning, production ML feature "
            "development, RAG, and AI application deployment"
        ),
    },
    "career_arc": (
        "Before software, John spent 10 years as a District Sales Manager at "
        "Johnson Brothers, managing 15 direct reports and a $2M territory — "
        "he brings people leadership and business judgment that most "
        "engineers don't have. He then transitioned into engineering and "
        "rose to Director of Programming at Qwasar within five years."
    ),
}

EXPERIENCE = [
    {
        "role": "Software Engineer & Director of Programming",
        "company": "Qwasar Silicon Valley",
        "period": "Jan 2021 - July 2026",
        "highlights": [
            "Led engineering and program delivery across a SaaS product "
            "portfolio for education and workforce upskilling customers; "
            "owned architecture, delivery, reliability, and roadmap execution.",
            "Maintained and extended Upskill, a SaaS learning platform "
            "serving 10,000+ active users: learner/admin dashboards, "
            "progress tracking, automated grading, cohort management, "
            "reporting, notifications, auth/permissions, and AI-assisted "
            "learning workflows.",
            "Reduced production errors by ~40% by strengthening background "
            "jobs, monitoring/logging, data pipelines, and database "
            "performance.",
            "Built a college application platform from 0 to 2,000+ users, "
            "owning architecture and ongoing scaling.",
            "Built an agentic learning companion (Python + Ruby) that chats "
            "with students and generates dynamic curriculum — in production "
            "handling 1,000+ sessions/messages per week.",
            "Developed an agentic program-manager system (Python/CrewAI) for "
            "weekly data aggregation, analytics reporting, and intervention "
            "identification for struggling students.",
            "Engineered an AI-powered code-validation interpreter (C++, "
            "Java, Python) for automated skill evaluation — used to assess "
            "3,000+ applicants.",
            "Created a comprehensive LLM and RAG curriculum taught across 7 "
            "campuses: prompt engineering, transformer math, vector search, "
            "cloud deployment, model evaluation, agent workflows, and "
            "production AI patterns.",
            "Architected GitHub-based CI/CD with Docker and Kubernetes; set "
            "technical direction and mentored engineers.",
        ],
    },
    {
        "role": "District Sales Manager",
        "company": "Johnson Brothers",
        "period": "10 years",
        "highlights": [
            "Managed a team of 15 direct reports and a sales territory "
            "grossing $2M annually — territory planning, coaching, revenue "
            "accountability, and operational execution.",
        ],
    },
]

PROJECTS = [
    {
        "name": "atari-games",
        "description": (
            "Deep RL agents using Double DQN with prioritized experience "
            "replay in PyTorch; trained and evaluated on CartPole, Space "
            "Invaders, and Pac-Man with configurable training pipelines and "
            "released checkpoints."
        ),
        "tech": ["PyTorch", "Deep RL", "Double DQN", "prioritized experience replay"],
    },
    {
        "name": "classically-punk",
        "description": (
            "End-to-end music genre classification on Spotify data; reached "
            "0.700 test accuracy and 0.695 macro F1 on a 10-genre task with "
            "reproducible experiment tracking and pipeline versioning."
        ),
        "tech": ["Python", "librosa", "scikit-learn", "XGBoost", "UMAP", "MLflow", "DVC", "PostgreSQL"],
    },
    {
        "name": "qkd-avantheir",
        "description": (
            "Adaptive ML defenses for Quantum Key Distribution; a co-evolving "
            "attacker/defender study showing how ML defenses degrade or hold "
            "under shifting adversarial strategies."
        ),
        "tech": ["Python", "adversarial ML", "quantum key distribution"],
    },
    {
        "name": "qkdsec",
        "description": (
            "Open-source Python library, installable via pip, for quantum key "
            "distribution security. Implements ETSI QKD 014 industry "
            "standards with tools for secure key workflows, protocol testing, "
            "quantum simulations, and mathematical security proofs."
        ),
        "tech": ["Python", "ETSI QKD 014", "security", "open source"],
    },
    {
        "name": "digital-freight-matching",
        "description": (
            "Production load-to-carrier matching on Ruby 3.3 / Rails 8 with "
            "Sidekiq, ActionCable, Kafka, geospatial optimization, real-time "
            "updates, REST APIs, and full test coverage."
        ),
        "tech": ["Ruby on Rails 8", "Sidekiq", "Kafka", "ActionCable", "geospatial"],
    },
    {
        "name": "striper-dex",
        "description": (
            "ML fishing-forecast service using XGBoost on 30+ years of NOAA "
            "oceanographic data; Dockerized inference pipeline predicting "
            "optimal fishing conditions in Monterey Bay."
        ),
        "tech": ["XGBoost", "Docker", "NOAA data", "forecasting"],
    },
    {
        "name": "this agent",
        "description": (
            "The agent you are talking to right now: built with the Google "
            "Agent Development Kit (ADK) in Python, powered by Gemini, with "
            "structured profile data exposed through function tools, and "
            "deployed to Google Cloud Run."
        ),
        "tech": ["Google ADK", "Gemini", "Python", "Cloud Run"],
    },
]

SKILLS = {
    "languages": ["Python", "Ruby", "TypeScript/JavaScript", "SQL", "HTML/CSS", "C/C++"],
    "machine_learning": [
        "PyTorch", "XGBoost", "scikit-learn", "librosa", "UMAP", "MLflow",
        "DVC", "model calibration", "deep reinforcement learning (DQN, "
        "Double DQN, prioritized experience replay)", "model evaluation",
        "adversarial ML",
    ],
    "ai_agents_and_llms": [
        "Google ADK", "CrewAI multi-agent orchestration", "RAG",
        "vector search", "prompt engineering", "OpenAI ChatKit",
        "Agent Builder", "curriculum-generating agents",
    ],
    "backend_and_systems": [
        "Ruby on Rails 8", "FastAPI", "Sidekiq", "ActionCable", "Kafka",
        "REST APIs", "microservices", "authentication/authorization",
        "geospatial systems",
    ],
    "data_and_infrastructure": [
        "PostgreSQL", "MongoDB", "vector databases", "Redis", "Docker",
        "Kubernetes", "GitHub Actions CI/CD", "GCP", "AWS", "monitoring and "
        "observability", "Selenium scraping", "encrypted data-lake workflows",
    ],
    "frontend": ["React", "Vite", "TypeScript", "dashboards and admin interfaces"],
    "specialized": [
        "Quantum Key Distribution (ETSI QKD 014)", "BB84 simulation",
        "numerical security proofs", "KME conformance testing",
    ],
    "leadership": [
        "technical direction", "mentoring", "roadmap and cross-product "
        "planning", "Agile/Scrum", "LLM/RAG curriculum design",
        "hackathon facilitation", "people management (15 direct reports)",
    ],
}

ROLE_FIT = {
    "pitch": (
        "John is the rare engineer who has already done the job most AI "
        "engineering roles describe: he has designed, built, shipped, and "
        "operated LLM-powered agents in production — not demos. His agentic "
        "learning companion handles 1,000+ real user sessions a week, his "
        "CrewAI program-manager agent runs weekly analytics for school "
        "teams, and his AI code-evaluation system has assessed 3,000+ "
        "applicants."
    ),
    "reasons": [
        "Production AI agents, not prototypes: multi-agent orchestration "
        "(CrewAI), RAG pipelines, vector search, and LLM integrations "
        "running in systems with 10,000+ users.",
        "Full-stack ownership: he takes features from architecture through "
        "CI/CD (Docker, Kubernetes, GitHub Actions) to monitoring in "
        "production, on GCP and AWS.",
        "Real ML depth beneath the LLM layer: deep RL in PyTorch, calibrated "
        "XGBoost forecasting, adversarial ML research, and rigorous "
        "evaluation practice (MLflow, DVC).",
        "He can teach what he builds: he wrote and taught an entire LLM/RAG "
        "curriculum across 7 campuses — a strong signal of communication "
        "skill and true depth of understanding.",
        "Leadership that scales: Director of Programming at Qwasar plus 10 "
        "years managing teams before engineering — he raises the bar for "
        "the people around him.",
        "This submission itself: he learned the Google ADK and shipped this "
        "working, deployed agent for the application — that is how he "
        "approaches new tools.",
    ],
}

RECOMMENDATION = {
    "author": "Jennifer Robertson, Chief Operating Officer, Qwasar Silicon Valley",
    "contact": "jennifer@qwasar.io",
    "date": "June 25, 2026",
    "quotes": [
        "It is with great pleasure and without reservation that I recommend "
        "John Jepsen.",
        "One of John's notable achievements at Qwasar was single-handedly "
        "developing a comprehensive curriculum for AI application "
        "development... covering RAG architectures, LLM integration, "
        "fine-tuning methodologies, and end-to-end AI application "
        "development. This curriculum became a cornerstone of our "
        "educational offering and is continually requested by our clients.",
        "He led and participated in a complete platform redevelopment, an "
        "extensive database migration involving re-architected object "
        "design, and the construction of an entirely new client application "
        "portal.",
        "John maintained a product-focused mindset that kept technical "
        "decisions grounded in real user needs — a balance that not all "
        "engineers strike naturally, but which John embodied consistently.",
        "He mentored numerous junior engineers in data science and machine "
        "learning — not because it was assigned to him, but because he "
        "cares deeply about both the people around him and the field itself.",
        "I would hire him again without hesitation, and I offer my strongest "
        "and most heartfelt recommendation to any organization fortunate "
        "enough to bring him on board.",
    ],
    "context": (
        "Qwasar wound down its North America programs in 2026, which is why "
        "John is on the market — not performance. His COO calls that "
        "parting 'a genuine sadness.'"
    ),
}
