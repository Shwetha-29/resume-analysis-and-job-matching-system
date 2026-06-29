SKILL_DISPLAY_NAMES = {

    "python": "Python",
    "java": "Java",
    "c": "C",
    "c++": "C++",
    "c#": "C#",

    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "typescript": "TypeScript",

    "react": "React",
    "angular": "Angular",
    "vue": "Vue",

    "node": "Node.js",
    "express": "Express",

    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",

    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",

    "docker": "Docker",
    "kubernetes": "Kubernetes",

    "tensorflow": "TensorFlow",
    "keras": "Keras",
    "pytorch": "PyTorch",

    "numpy": "NumPy",
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",

    "scikit-learn": "Scikit-learn",

    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "data science": "Data Science",

    "computer vision": "Computer Vision",
    "nlp": "NLP",

    "streamlit": "Streamlit",
    "streamlit cloud": "Streamlit Cloud",

    "langchain": "LangChain",
    "langgraph": "LangGraph",

    "openai": "OpenAI",

    "prompt engineering": "Prompt Engineering",

    "rag": "RAG",

    "vector database": "Vector Database",

    "embeddings": "Embeddings",

    "transformers": "Transformers",

    "lstm": "LSTM",

    "random forest": "Random Forest",

    "gen ai": "GenAI",

    "generative ai": "Generative AI",

    "llm": "LLM",

    "rest api": "REST API",

    "php": "PHP",

    "xampp": "XAMPP",

    "git": "Git",

    "github": "GitHub",

    "oracle": "Oracle"
}


def format_skill(skill):
    """
    Return a professional display name for a skill.
    """

    return SKILL_DISPLAY_NAMES.get(
        skill.lower(),
        skill.title()
    )