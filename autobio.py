import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# Page Config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💻",
    layout="wide"
)


# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    h1, h2, h3 {
        color: #1f4e79;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About Me", "Skills", "Projects", "Contact"])

st.sidebar.markdown("---")
st.sidebar.info("Built using Streamlit 🚀")

# HOME PAGE
if page == "Home":
    # Use 2 columns: left for text, right for image
    col1, col2 = st.columns([3, 1])  # 3:1 ratio (text wider than image)

    with col1:
        st.title("👋 Welcome to My Portfolio")
        st.subheader("Hello! I'm Lyndon Luke Morre")
        st.write("An aspiring IT professional passionate about Cyber Security and Web Development.")
        
        st.metric("Projects Completed", 12)
        st.metric("Technologies Learned", 15)
        
        st.progress(80)
        st.caption("Learning Progress Towards Full-Stack Developer")

    with col2:
        from PIL import Image
        img = Image.open("images/profile.jpg")  
        st.image(img, width=300, caption="That's me 😎")

# ABOUT ME
elif page == "About Me":
    st.title("📖 About Me")

    st.write("""
    I am an IT student with experience in:
    - Web Development
    - Backend Systems
    - Database Management
    - Data Analytics
    """)
    st.write("I love cooking and playing video games., and I am a big fan of anime and manga.")

    with st.expander("🎯 My Goals"):
        st.write("To become a skilled Cyber Security Specialist and Game Developer.")
        st.write("To BEOME RICH.")
        st.write("To live life without having to worry about being bald once in my 40's.")

    st.success("I enjoy building practical systems that solve real-world problems.")

    st.title("Cooking With me 🍳")
    images = [
    "images/dynamite.jpg",
    "images/sisig.jpg",
    "images/omelette.jpg",
    "images/wings.jpg",
]
    
    if 'img_index' not in st.session_state:
        st.session_state.img_index = 0
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                st.session_state.img_index = max(st.session_state.img_index - 1, 0)
                with col2:
                     if st.button("Next"):
                        st.session_state.img_index = min(st.session_state.img_index + 1, len(images)-1)

    # Display image
    img_choice = st.selectbox("Select Image", images)
    img = Image.open(f"{img_choice}")
    
    st.image(img, width=500, caption=img_choice)
    
    st.write("I live in Cebu City, Philippines. I am currently a student at the University of Cebu - Main Campus, pursuing a degree in Information Technology.")
    if 'map_data' not in st.session_state:
        st.session_state.map_data = pd.DataFrame({
                'lat': [10.3157],
                'lon': [123.8854]
                })
    
    st.map(st.session_state.map_data)

    


# SKILLS
elif page == "Skills":
    st.title("🛠 Skills & Technologies")

    skills = {
        "Frontend": ["HTML", "CSS", "JavaScript", "React"],
        "Backend": ["Python", "Django", "Spring Boot", "PHP"],
        "Database": ["MySQL", "Firebase"],
        "Programming": ["Java", "C++", "Python"]
    }

    tabs = st.tabs(list(skills.keys()))

    for tab, category in zip(tabs, skills.keys()):
        with tab:
            for i, skill in enumerate(skills[category]):
                st.checkbox(
                    skill,
                    value=True,
                    key=f"{category}_{skill}_{i}"
                )





    st.subheader("Skill Proficiency (Sample Chart)")

    data = pd.DataFrame({
        "Skill": ["Python", "Java", "React", "SQL"],
        "Level": [85, 75, 80, 70]
    })

    st.bar_chart(data.set_index("Skill"))

# PROJECTS
elif page == "Projects":
    st.title("📂 My Projects")

    project_option = st.selectbox(
        "Choose a project:",
        ["Attendance System", "Online Shoe Store", "PetTrack", "Accessify", "Library Management System", "Submisstion Tracker System"]
    )

    st.write(f"### {project_option}")

    st.write("Project description goes here...")

    uploaded_file = st.file_uploader("Upload project screenshot", type=["png", "jpg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Project Preview", use_column_width=True)

    st.download_button(
        label="Download Project Documentation",
        data="Sample documentation content.",
        file_name="project_doc.txt"
    )

# CONTACT PAGE
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success(f"Thank you {name}! I will get back to you soon.")

    st.markdown("### 🌐 Connect with Me")
    st.write("LinkedIn | GitHub | Portfolio Website | Email ")

# Footer
st.markdown("---")
st.caption("© 2026 Lyndon Luke Morre | Built with Streamlit")
