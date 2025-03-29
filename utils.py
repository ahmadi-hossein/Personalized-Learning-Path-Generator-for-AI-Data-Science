import pandas as pd
from fpdf import FPDF

# Load resources dataset
def load_resources():
    return pd.read_csv("data/resources.csv")

# Generate personalized recommendations
def generate_recommendations(current_skills, learning_goals):
    resources = load_resources()
    recommendations = []
    
    for goal in learning_goals:
        filtered = resources[
            (resources["Skill"] == goal) &
            (~resources["Prerequisite"].isin(current_skills))
        ]
        recommendations.extend(filtered.to_dict(orient="records"))
    
    return recommendations

# Export learning path to PDF
def export_to_pdf(name, recommendations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Personalized Learning Path for {name}", ln=True, align="C")
    pdf.ln(10)
    
    for i, rec in enumerate(recommendations, 1):
        pdf.cell(200, 10, txt=f"{i}. {rec['Title']} - {rec['Type']}", ln=True)
        pdf.cell(200, 10, txt=f"   Link: {rec['Link']}", ln=True)
        pdf.ln(5)
    
    pdf.output("learning_path.pdf")