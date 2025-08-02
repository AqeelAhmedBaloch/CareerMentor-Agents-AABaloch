# 🎓 Career Mentor Agents

**Career Mentor Agents** is a multi-agent AI system that helps users explore, plan, and pursue their ideal career paths. It intelligently guides users from discovering their strengths and interests to generating personalized career roadmaps using LLM agents and tool-based reasoning.

Built using **Chainlit**, **OpenAI Agent SDK**, and modular agent handoffs.

---

## 🚀 Key Features

- 🧭 **CareerAgent**: Analyzes user interests, goals, and recommends career fields.
- 📘 **SkillAgent**: Suggests the skills, certifications, and learning paths required.
- 🧳 **JobAgent**: Provides job roles, demand trends, and average salaries.
- 🔧 Integrated tools:
  - `get_career_roadmap()`
  - `get_learning_resources()`
  - `get_job_opportunities()`
- 🤖 Uses agent handoff architecture for seamless knowledge flow.

---

## 🧠 How It Works

```plaintext
User Input
   ↓
CareerAgent → SkillAgent → JobAgent
   ↓                 ↘︎
 Roadmap      Tools + Data Sources
