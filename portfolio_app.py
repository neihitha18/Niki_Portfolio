
# ----- Page Config -----
st.set_page_config(page_title="Niki's Portfolio", page_icon="✨", layout="wide")

# ----- Custom CSS for color and style -----
st.markdown("""
    <style>
    .main {
        background: linear-gradient(120deg, #f6f9fc, #e0f7fa);
        color: #333;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .project-card {
        background-color: #ffffffdd;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Hero Section -----
st.title("Hi, I'm Niki 👋")
st.subheader("Data Scientist | AI Specialist | Generative AI Enthusiast")
st.write("""
Welcome to my portfolio! I specialize in building intelligent systems, extracting insights from data,
and creating explainable AI solutions. My passion lies in solving real-world problems using data, machine learning,
and cutting-edge AI techniques.
""")

# ----- Social Links -----
st.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com) 
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com) 
[![Hugging Face](https://img.shields.io/badge/HuggingFace-yellow?logo=huggingface)](https://huggingface.co)
""")

st.markdown("---")

# ----- Projects Section -----
st.header("📁 Featured Projects")

projects = [
    {
        "title": "Explainable AI for Breast Cancer Diagnosis",
        "description": "Built a CNN-based classifier for breast cancer cell image diagnosis. Integrated LIME for explainability.",
        "github": "https://github.com/your-repo",
    },
    {
        "title": "Generative AI with RAG",
        "description": "Used LangChain with Hugging Face and OpenAI APIs to create a retrieval-augmented generation chatbot.",
        "github": "https://github.com/your-repo",
    },
    {
        "title": "Simulated Hydrogen Sensor Data",
        "description": "Generated synthetic green hydrogen plant data to analyze anomalies and apply ML for predictive monitoring.",
        "github": "https://github.com/your-repo",
    },
]

for project in projects:
    with st.container():
        st.markdown(f"<div class='project-card'><h3>{project['title']}</h3><p>{project['description']}</p>"
                    f"<a href='{project['github']}' target='_blank'>🔗 GitHub Repo</a></div>", unsafe_allow_html=True)

st.markdown("---")

# ----- About Me Section -----
st.header("🙋‍♀️ About Me")
st.write("""
I'm Niki, a data science professional passionate about combining technical depth with creativity.
I’ve worked with structured and unstructured data, built interpretable ML pipelines, and explored the frontiers of Generative AI.
My toolkit includes Python, SQL, Power BI, TensorFlow, LangChain, and more.
""")

st.markdown("---")

# ----- Footer / Contact -----
st.header("📫 Let's Connect")
st.write("Feel free to reach out or explore my work on the platforms above.")