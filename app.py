import streamlit as st
import pandas as pd
from utils import load_resources, generate_recommendations, export_to_pdf

# ---- Page Configuration ----
st.set_page_config(
    page_title="Personalized Learning Path Generator for AI & Data Science",
    page_icon="📚",
    layout="wide"
)

# ---- Title and Description ----
st.title("📚 Personalized Learning Path Generator for AI & Data Science")
st.markdown("""
This tool helps you create a **comprehensive** and **customizable** learning path tailored to your skills and goals in AI, Data Science, and beyond.
""")

# ---- Input Section: User Information ----
st.header("📝 Step 1: Tell Us About Yourself")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name:", placeholder="e.g., Reza")
    skill_level = st.selectbox("Select your skill level:", ["Beginner", "Intermediate", "Advanced"])

with col2:
    current_skills = st.multiselect(
        "Select your current skills:",
        [
            "Python", "R", "SQL", "Statistics", "Machine Learning", 
            "Deep Learning", "Data Visualization", "Natural Language Processing", 
            "Computer Vision", "Generative AI", "Big Data", "Cloud Computing", 
            "Time Series Analysis", "Anomaly Detection", "AutoML", "MLOps",
            "Natural Language Understanding", "Speech Recognition", "Reinforcement Learning",
            "Knowledge Representation and Reasoning", "Expert Systems", "Swarm Intelligence",
            "Evolutionary Algorithms", "Cognitive Computing", "Explainable AI",
            "AI Ethics and Fairness", "Edge AI", "Augmented Intelligence",
            "Human-Robot Interaction", "Multi-Agent Systems"
        ]
    )
    learning_goals = st.multiselect(
        "What do you want to learn?",
        [
            "Python", "Data Cleaning", "Data Visualization", "Machine Learning", 
            "Deep Learning", "Natural Language Processing", "Computer Vision", 
            "Generative AI", "Big Data", "Cloud Computing", "Time Series Analysis", 
            "Anomaly Detection", "AutoML", "MLOps",
            "Natural Language Understanding", "Speech Recognition", "Reinforcement Learning",
            "Knowledge Representation and Reasoning", "Expert Systems", "Swarm Intelligence",
            "Evolutionary Algorithms", "Cognitive Computing", "Explainable AI",
            "AI Ethics and Fairness", "Edge AI", "Augmented Intelligence",
            "Human-Robot Interaction", "Multi-Agent Systems"
        ]
    )

# ---- Generate Learning Path ----
if st.button("🚀 Generate Learning Path"):
    if not name:
        st.error("Please enter your name.")
    elif not current_skills:
        st.error("Please select your current skills.")
    elif not learning_goals:
        st.error("Please select your learning goals.")
    else:
        st.success(f"Generating a personalized learning path for {name}...")
        
        # Generate recommendations
        recommendations = generate_recommendations(current_skills, learning_goals)
        
        # Display recommendations
        st.subheader("🎯 Your Personalized Learning Path:")
        if recommendations:
            df = pd.DataFrame(recommendations)
            st.dataframe(df, use_container_width=True)
            
            # Export to PDF
            if st.button("📄 Export as PDF"):
                export_to_pdf(name, recommendations)
                st.success("Learning path exported as 'learning_path.pdf'!")
        else:
            st.info("You already have the required skills! Consider exploring advanced topics.")

# ---- Footer ----
st.markdown("""
---
🌟 Created with ❤️ by Hossein Ahmadi
""")