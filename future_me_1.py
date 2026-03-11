import streamlit as st
import random
import pandas as pd


st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color:white;
}

h1,h2,h3,h4 {
    color:#00ffe5;
}

div[data-testid="stMetric"] {
    background-color:#111;
    border-radius:10px;
    padding:15px;
}

.block-container {
    padding-top:2rem;
}

.stButton>button {
    background: linear-gradient(90deg,#00ffe5,#007cf0);
    color:black;
    border:none;
    border-radius:8px;
    font-weight:bold;
    padding:10px 20px;
}

.stButton>button:hover {
    transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)
# ---------------- UI ---------------- #

st.title("🔮 FutureMe AI")
st.subheader("Explore Your Career in 2035")

st.write("Enter your profile to see your possible future career.")

name = st.text_input("Name")
age = st.number_input("Age", 16, 60)

skills = st.text_area("Current Skills")
interests = st.text_area("Interests")
goal = st.text_input("Future Goal")

predict = st.button("Predict My Future")

# ---------------- Career Knowledge Base ---------------- #

career_domains = {

    "AI & Data": {
    "keywords":[
    "python","machine learning","ai","data","deep learning",
    "statistics","analytics","automation","nlp","computer vision"
    ],
    "careers":[
    "AI Engineer","Machine Learning Engineer","Data Scientist",
    "AI Researcher","AI Product Manager","Deep Learning Engineer"
    ]
    },

    "Software Engineering": {
    "keywords":[
    "programming","coding","software","development",
    "backend","frontend","algorithms","systems","debugging"
    ],
    "careers":[
    "Software Engineer","Backend Developer","Frontend Developer",
    "Full Stack Developer","Systems Engineer"
    ]
    },

    "Finance": {
    "keywords":[
    "finance","investment","economics","markets","trading",
    "portfolio","risk","banking","financial modeling"
    ],
    "careers":[
    "Investment Banker","Portfolio Manager",
    "Financial Analyst","Risk Analyst","Asset Manager"
    ]
    },

    "FinTech": {
    "keywords":[
    "fintech","blockchain","crypto","digital payments",
    "financial technology","decentralized","smart contracts"
    ],
    "careers":[
    "FinTech Specialist","Blockchain Developer",
    "Crypto Analyst","Digital Banking Strategist"
    ]
    },

    "Cybersecurity": {
    "keywords":[
    "security","cyber","network","encryption",
    "hacking","penetration testing","threat analysis"
    ],
    "careers":[
    "Cybersecurity Analyst","Security Engineer",
    "Ethical Hacker","Penetration Tester"
    ]
    },

    "Cloud & DevOps": {
    "keywords":[
    "cloud","aws","devops","docker","kubernetes",
    "infrastructure","deployment","automation"
    ],
    "careers":[
    "Cloud Engineer","DevOps Engineer",
    "Site Reliability Engineer","Cloud Architect"
    ]
    },

    "Business & Entrepreneurship": {
    "keywords":[
    "business","startup","entrepreneur",
    "strategy","leadership","innovation","product"
    ],
    "careers":[
    "Startup Founder","Product Manager",
    "Business Strategist","Innovation Consultant"
    ]
    },

    "Marketing & Growth": {
    "keywords":[
    "marketing","branding","advertising",
    "digital marketing","seo","content","growth"
    ],
    "careers":[
    "Marketing Manager","Growth Strategist",
    "Brand Manager","Digital Marketing Specialist"
    ]
    },

    "Healthcare & BioTech": {
    "keywords":[
    "medicine","biology","healthcare",
    "biotech","genetics","clinical","pharmaceutical"
    ],
    "careers":[
    "Biomedical Scientist","Healthcare Analyst",
    "BioTech Researcher","Medical Data Analyst"
    ]
    },

    "Design & Creativity": {
    "keywords":[
    "design","ui","ux","creative","visual",
    "graphics","product design","illustration"
    ],
    "careers":[
    "UX Designer","Product Designer",
    "Graphic Designer","Creative Director"
    ]
    },

    "Education & Research": {
    "keywords":[
    "teaching","education","research",
    "academia","learning","curriculum"
    ],
    "careers":[
    "Professor","Research Scientist",
    "Education Specialist","Academic Researcher"
    ]
    }
}

# ---------------- Reality Check Data ---------------- #

reality_checks = {

"AI & Data":[
"Rapid technology changes require constant upskilling.",
"High global competition in AI-related jobs.",
"AI tools may automate some routine data tasks."
],

"Software Engineering":[
"Technology stacks evolve quickly requiring continuous learning.",
"Competition from global remote developers.",
"Automation tools may reduce demand for basic coding tasks."
],

"Finance":[
"Economic downturns can affect hiring and bonuses.",
"High-pressure environment with performance expectations.",
"Automation and AI may replace some financial analysis roles."
],

"FinTech":[
"Regulatory changes could disrupt fintech innovations.",
"Crypto and blockchain markets are highly volatile.",
"Security risks in digital financial systems."
],

"Cybersecurity":[
"Cyber threats evolve rapidly requiring constant skill upgrades.",
"High responsibility during security breaches.",
"Need for certifications and specialized expertise."
],

"Cloud & DevOps":[
"Frequent system updates and infrastructure changes.",
"Pressure to maintain uptime during outages.",
"Continuous certification requirements."
],

"Business & Entrepreneurship":[
"High startup failure rates.",
"Difficulty securing funding in early stages.",
"Market competition from established companies."
],

"Marketing & Growth":[
"Constant pressure to meet marketing performance targets.",
"Rapid changes in digital marketing algorithms.",
"High competition in brand positioning."
],

"Healthcare & BioTech":[
"Strict regulatory approval processes.",
"Long research and development timelines.",
"High responsibility impacting public health."
],

"Design & Creativity":[
"Creative burnout due to constant demand for new ideas.",
"Client revisions and tight deadlines.",
"Freelance instability in some roles."
],

"Education & Research":[
"Long academic career paths before stability.",
"Limited funding for research in some fields.",
"Competitive academic job markets."
]

}

# ---------------- Personal Life Impact ---------------- #

personal_life_impacts = {

"AI & Data":[
"Long hours working on complex models or research deadlines.",
"Continuous learning reducing personal free time.",
"Extended screen exposure leading to fatigue."
],

"Software Engineering":[
"Long debugging sessions close to product deadlines.",
"Occasional overtime during product releases.",
"Extended screen exposure affecting health."
],

"Finance":[
"Very long working hours especially in investment banking.",
"High stress due to financial pressure.",
"Limited personal time during peak financial periods."
],

"FinTech":[
"Fast-paced startup environments can increase stress.",
"Unpredictable workloads due to rapid innovation.",
"Balancing finance and tech knowledge requires constant effort."
],

"Cybersecurity":[
"On-call responsibilities during cyber incidents.",
"High stress during security breaches.",
"Irregular working hours in critical situations."
],

"Cloud & DevOps":[
"Late-night deployments and system monitoring.",
"Responsibility during outages affecting personal time.",
"High pressure to maintain system reliability."
],

"Business & Entrepreneurship":[
"Long working hours especially in early startup stages.",
"Financial uncertainty affecting personal stability.",
"Difficulty separating work from personal life."
],

"Marketing & Growth":[
"Constant pressure to meet campaign targets.",
"Fast-paced work cycles with tight deadlines.",
"Need to stay connected to trends and social platforms."
],

"Healthcare & BioTech":[
"Emotionally demanding work environments.",
"Long hours in research or healthcare settings.",
"High responsibility affecting stress levels."
],

"Design & Creativity":[
"Creative pressure to constantly produce new ideas.",
"Tight deadlines for design projects.",
"Client feedback cycles affecting personal schedules."
],

"Education & Research":[
"Long hours preparing lessons or research publications.",
"Balancing teaching responsibilities with research work.",
"Academic pressure to publish frequently."
]

}


# ---------------- Prediction Logic ---------------- #

if predict:

    # Combine all user inputs
    user_profile = (skills + " " + interests + " " + goal).lower()

    domain_scores = {}

    for domain, data in career_domains.items():

        score = 0

        for word in data["keywords"]:
            if word in user_profile:
                score += 1

        domain_scores[domain] = score

    st.markdown("### 📊 Career Compatibility Analysis")

    chart_data = pd.DataFrame({
        "Career Domain": list(domain_scores.keys()),
        "Score": list(domain_scores.values())
    })

    st.bar_chart(chart_data.set_index("Career Domain"))

    best_domain = max(domain_scores, key=domain_scores.get)

    predicted_career = random.choice(career_domains[best_domain]["careers"])

    confidence = min(domain_scores[best_domain] * 20, 100)

    
    st.divider()
    st.success("Future prediction complete")

    # ---------------- Output ---------------- #

    st.markdown("### 🚀 Predicted Career")
    st.write(predicted_career)

    st.markdown("### 📊 Prediction Confidence")
    st.write(f"{confidence}%")

    # ---------------- Skill Gap Analysis ---------------- #

    required_skills = career_domains[best_domain]["keywords"]

    missing_skills = []

    for skill in required_skills:
        if skill not in user_profile:
            missing_skills.append(skill)

    st.markdown("### 🧠 Skills You Should Learn")

    if len(missing_skills) == 0:
        st.write("You already have many relevant skills!")
    else:
        for skill in missing_skills:
            st.write(f"• {skill}")

    # ---------------- Roadmap ---------------- #

    st.markdown("### 🗺 Roadmap to 2035")

    st.write("""
    2025–2026: Strengthen foundational knowledge and technical skills  

    2027–2028: Work on real-world projects and internships  

    2029–2031: Gain industry experience and specialization  

    2032–2035: Move into advanced or leadership roles
    """)

    # ---------------- Future Self Message ---------------- #
    st.markdown("### 📈 2035 Industry Outlook")

    st.write("""
    AI & Data → Rapid Growth 🚀  
    FinTech → High Growth 📈  
    Cybersecurity → Critical Demand 🔐  
    Technology → Strong Growth 💻  
    Traditional Banking → Moderate Growth
    """)


    st.markdown("### 💬 Message From Your 2035 Self")

    st.write(f"""
    Hello {name},

    By focusing on {goal}, you successfully built a career as a {predicted_career} in the {best_domain} industry.

    Your strongest advantage was combining your skills in {skills} with your passion for {interests}.

    Keep learning and adapting — the future belongs to those who continuously evolve.
    """)
    st.markdown("### 🌟 Other Possible Career Paths")

    top_domains = sorted(domain_scores, key=domain_scores.get, reverse=True)[:3]

    for domain in top_domains:
        career = random.choice(career_domains[domain]["careers"])
        st.write(f"• {career} ({domain})")

# ---------------- Reality Check ---------------- #

    st.warning("Reality Check: Challenges You Should Be Prepared For")

    st.markdown("### ⚠️ Industry Risks")

    risks = reality_checks.get(best_domain, [])

    if risks:
        for risk in risks:
            st.write("•", risk)

    st.markdown("### 🧠 Personal Life Impact")

    life_impacts = personal_life_impacts.get(best_domain, [])

    if life_impacts:
        for impact in life_impacts:
            st.write("•", impact)

    st.markdown("### 🛠 How to Prepare")

    st.write("""
    • Continuously update your skills and industry knowledge  
    • Build strong real-world project experience  
    • Develop stress management and time management skills  
    • Maintain a healthy work-life balance where possible  
    """)