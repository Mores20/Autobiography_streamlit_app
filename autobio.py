import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime
import time

# Page Configa
st.set_page_config(
    page_title="Lyndon Luke Morre | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
import os

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error("CSS file not found. Check your file path.")

load_css()


# Initialize session state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 0
if 'notification_shown' not in st.session_state:
    st.session_state.notification_shown = False
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Visitor counter
st.session_state.visitor_count += 1

# Sidebar with enhanced navigation
with st.sidebar:
    # Profile section
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h2 style='color: white; margin-bottom: 20px;'>Lyndon Luke Morre</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Try to load profile image
    try:
        profile_img = Image.open("images/profile.jpg")
        st.image(profile_img, width=200, output_format="auto")
    except:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                      width: 150px; height: 150px; border-radius: 50%; margin: 20px auto;
                      display: flex; align-items: center; justify-content: center;'>
                <span style='color: white; font-size: 48px;'>👤</span>
            </div>
        """, unsafe_allow_html=True)
    
    # Navigation with icons
    st.markdown("<br>", unsafe_allow_html=True)
    
    pages = {
        "🏠 Home": "Home",
        "👨‍💻 About Me": "About Me",
        "🛠 Skills": "Skills",
        "📂 Projects": "Projects", 
        "📬 Contact": "Contact"
    }
    
    page = st.radio("Navigation", list(pages.keys()))
    page = pages[page]
    
    # Dark mode toggle
    st.markdown("<br>", unsafe_allow_html=True)
    dark_mode = st.checkbox("🌙 Dark Mode", st.session_state.dark_mode)
    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode
        st.rerun()
    
    # Visitor counter
    st.markdown("---")
    st.markdown(f"""
        <div style='text-align: center; color: white; padding: 10px;'>
            <p>👥 Visitors: {st.session_state.visitor_count}</p>
            <p style='font-size: 12px; opacity: 0.8;'>Built with Streamlit 🚀</p>
        </div>
    """, unsafe_allow_html=True)

# Welcome notification
if not st.session_state.notification_shown:
    st.balloons()
    st.success("👋 Welcome to my portfolio! Feel free to explore!")
    st.session_state.notification_shown = True
    time.sleep(2)
    st.rerun()

# HOME PAGE
if page == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <h1 class='fade-in'>👋 Welcome to My Portfolio</h1>
            <h2 class='typing-animation' style='font-size: 24px; color: 62222;'>
                Hello! I'm Lyndon Luke Morre
            </h2>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
                      padding: 25px; border-radius: 20px; margin: 20px 0;'>
                <p style='font-size: 18px; line-height: 1.6;'>
                    An aspiring IT professional passionate about 
                    <span style='color: #667eea; font-weight: bold;'>Cyber Security</span> and 
                    <span style='color: #764ba2; font-weight: bold;'>Web Development</span>.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Metrics in a row
        col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
        with col_metrics1:
            st.metric("Projects Completed", "12", "+2 this month")
        with col_metrics2:
            st.metric("Technologies Learned", "15", "↑ 20%")
        with col_metrics3:
            st.metric("GitHub Contributions", "450", "↑ 35%")
        
        # Animated progress
        st.subheader("🎯 Full-Stack Developer Journey")
        progress_value = 80
        st.progress(progress_value/100)
        st.caption(f"Progress: {progress_value}% - Almost there! Keep going! 💪")
        
        # Quick actions
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            if st.button("📄 View Resume", use_container_width=True):
                st.info("Resume download will be available soon!")
        with col_btn2:
            if st.button("💼 See Projects", use_container_width=True):
                st.session_state.page = "Projects"
                st.rerun()
        with col_btn3:
            if st.button("📧 Contact Me", use_container_width=True):
                st.session_state.page = "Contact"
                st.rerun()
    
    with col2:
        try:
            img = Image.open("images/profile.jpg")
            st.image(img, width=350, caption="That's me! 😎")
        except:
            # Placeholder animation
            st.markdown("""
                <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                          width: 350px; height: 350px; border-radius: 30px; 
                          display: flex; align-items: center; justify-content: center;
                          animation: pulse 2s infinite;'>
                    <span style='color: white; font-size: 100px;'>👨‍💻</span>
                </div>
                <style>
                    @keyframes pulse {
                        0% { transform: scale(1); }
                        50% { transform: scale(1.05); }
                        100% { transform: scale(1); }
                    }
                </style>
            """, unsafe_allow_html=True)
    
    # Featured section
    st.markdown("---")
    st.subheader("🌟 Featured Highlights")
    
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    
    with col_feat1:
        st.markdown("""
            <div class='project-card' style='text-align: center;'>
                <h3>🏆 Recent Achievement</h3>
                <p style='font-size: 36px;'>🥇</p>
                <p>1st Place - University Hackathon 2025</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_feat2:
        st.markdown("""
            <div class='project-card' style='text-align: center;'>
                <h3>📚 Current Focus</h3>
                <p style='font-size: 36px;'>🔐</p>
                <p>Advanced Cybersecurity Certification</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_feat3:
        st.markdown("""
            <div class='project-card' style='text-align: center;'>
                <h3>🎮 Fun Fact</h3>
                <p style='font-size: 36px;'>🎯</p>
                <p>Speedrun enthusiast - 100+ games completed</p>
            </div>
        """, unsafe_allow_html=True)

# ABOUT ME
elif page == "About Me":
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.title("📖 About Me")
        
        # Interactive timeline
        st.markdown("""
                
                <div class="timeline-item">
                    <h3>🎓 Education</h3>
                    <p>
                        <strong>Cebu Institute of Technology - University</strong><br>
                        Bachelor of Science in Information Technology<br>
                        2022 - Present
                    </p>
                </div>
        """, unsafe_allow_html=True)
                

        st.markdown("""
            <div class="timeline-item">
                    <h3>💼 Experience</h3>
                    <p>
                        <strong>IT Intern</strong> - Tech Solutions Inc.<br>
                        Web Development & Database Management<br>
                        Summer 2024
                    </p>
                </div>
        """, unsafe_allow_html=True)
        st.markdown("""
                <div class="timeline-item">
                    <h3>🏆 Certifications</h3>
                    <p>
                        • Google IT Support Professional<br>
                        • Cisco Networking Basics<br>
                        • Python for Everybody (Coursera)
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)


        
        with st.expander("🎯 My Goals & Dreams", expanded=True):
            st.markdown("""
                <div style='padding: 10px;'>
                    <p>✨ <strong>Short-term:</strong> Become a skilled Cyber Security Specialist</p>
                    <p>🎮 <strong>Long-term:</strong> Develop my own indie game studio</p>
                    <p>💰 <strong>Financial:</strong> Achieve financial freedom and help my family</p>
                    <p>💇‍♂️ <strong>Humor:</strong> Keep my hairline intact through my 40s! 😂</p>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.title("🍳 Cooking Gallery")
        
        # Enhanced image gallery
        images = {
            "🍤 Dynamite": "images/dynamite.jpg",
            "🍖 Sisig": "images/sisig.jpg", 
            "🥚 Omelette": "images/omelette.jpg",
            "🍗 Wings": "images/wings.jpg"
        }
        
        # Image selector with preview
        img_choice = st.selectbox("Choose a dish to view:", list(images.keys()))
        
        try:
            img = Image.open(images[img_choice])
            st.image(img, width=500, caption=f"Homemade {img_choice}", output_format="auto")
            
            # Cooking stats
            st.markdown("""
                <div style='background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%);
                          padding: 20px; border-radius: 15px; margin-top: 20px;'>
                    <h4 style='margin-top: 0;'>👨‍🍳 Cooking Stats</h4>
                    <p>⭐ Rating: 4.8/5</p>
                    <p>⏱️ Prep Time: 25 mins</p>
                    <p>🔥 Difficulty: Medium</p>
                </div>
            """, unsafe_allow_html=True)
        except:
            st.info("📸 Cooking photos coming soon! Add your images to the 'images' folder.")
    
    # Location with map
    st.markdown("---")
    st.subheader("📍 Location")
    
    col_map1, col_map2 = st.columns([2, 1])
    
    with col_map1:
        map_data = pd.DataFrame({
            'lat': [10.3157],
            'lon': [123.8854]
        })
        st.map(map_data, zoom=12)
    
    with col_map2:
        st.markdown("""
            <div style='padding: 30px;'>
                <h3>Cebu City, Philippines</h3>
                <p>🏝️ Queen City of the South</p>
                <p>🌆 Where tradition meets innovation</p>
                <p>🎯 Timezone: GMT+8</p>
            </div>
        """, unsafe_allow_html=True)

# SKILLS
elif page == "Skills":
    st.title("🛠 Skills & Technologies")
    
    # Skills visualization
    skills_data = {
        "Frontend": ["HTML", "CSS", "JavaScript", "React", "Bootstrap"],
        "Backend": ["Python", "Django", "Spring Boot", "PHP", "Node.js"],
        "Database": ["MySQL", "Firebase", "MongoDB", "PostgreSQL"],
        "Programming": ["Java", "C++", "Python", "C#", "JavaScript"],
        "Tools": ["Git", "Docker", "VS Code", "Postman", "Figma"],
        "Soft Skills": ["Problem Solving", "Team Collaboration", "Communication", "Time Management"]
    }
    
    # Skill tags with categories
    for category, skills in skills_data.items():
        st.subheader(f"📌 {category}")
        
        # Create columns for better layout
        cols = st.columns(3)
        for i, skill in enumerate(skills):
            col_idx = i % 3
            with cols[col_idx]:
                st.markdown(f"""
                    <div class='skill-tag' style='width: 100%; text-align: center;'>
                        {skill}
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Skill proficiency with custom progress bars
    st.subheader("📊 Skill Proficiency")
    
    proficiency_data = {
        "Python": 85,
        "Java": 75,
        "React": 80,
        "SQL": 70,
        "JavaScript": 85,
        "Django": 65
    }
    
    for skill, level in proficiency_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"**{skill}**")
        with col2:
            st.markdown(f"""
                <div class='skill-progress'>
                    <div class='skill-progress-fill' style='width: {level}%;'></div>
                </div>
                <p style='text-align: right; margin-top: -5px;'>{level}%</p>
            """, unsafe_allow_html=True)
    
    # Learning path
    st.subheader("🎓 Learning Path")
    
    learning_topics = [
        "Advanced React & Next.js",
        "Cloud Computing (AWS)",
        "Ethical Hacking",
        "Mobile Development",
        "System Design"
    ]
    
    for i, topic in enumerate(learning_topics):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{topic}**")
        with col2:
            if i < 2:
                st.markdown("🟢 In Progress")
            else:
                st.markdown("⚪ Planned")

# PROJECTS
elif page == "Projects":
    st.title("📂 My Projects")
    
    # Project showcase
    projects = {
        "Attendance System": {
            "description": "A QR-code based attendance tracking system with real-time monitoring and automated reporting.",
            "tech": ["Python", "OpenCV", "SQLite", "Streamlit"],
            "status": "Completed",
            "year": "2024",
            "icon": "📱"
        },
        "Online Shoe Store": {
            "description": "Full-stack e-commerce platform for sneaker enthusiasts with payment integration.",
            "tech": ["Django", "PostgreSQL", "Stripe API", "Bootstrap"],
            "status": "Live",
            "year": "2024",
            "icon": "👟"
        },
        "PetTrack": {
            "description": "Pet health monitoring app with vaccination schedules and medical records.",
            "tech": ["React", "Firebase", "Node.js", "Material-UI"],
            "status": "In Development",
            "year": "2025",
            "icon": "🐾"
        },
        "Accessify": {
            "description": "Accessibility tools for visually impaired users with screen reading capabilities.",
            "tech": ["Python", "Tkinter", "TTS", "OpenCV"],
            "status": "Beta",
            "year": "2024",
            "icon": "♿"
        },
        "Library Management System": {
            "description": "Complete library automation system with inventory and member management.",
            "tech": ["Java", "Spring Boot", "MySQL", "Thymeleaf"],
            "status": "Completed",
            "year": "2023",
            "icon": "📚"
        },
        "Submission Tracker": {
            "description": "Academic submission tracking system for students and instructors.",
            "tech": ["PHP", "MySQL", "Bootstrap", "AJAX"],
            "status": "Completed",
            "year": "2023",
            "icon": "📋"
        }
    }
    
    # Project filter
    col_filter1, col_filter2 = st.columns(2)
    with col_filter1:
        status_filter = st.multiselect(
            "Filter by Status",
            ["Completed", "Live", "Beta", "In Development"],
            default=["Completed", "Live", "Beta", "In Development"]
        )
    with col_filter2:
        year_filter = st.selectbox(
            "Filter by Year",
            ["All", "2025", "2024", "2023"]
        )
    
    # Display projects in grid
    cols = st.columns(2)
    col_index = 0
    
    for project_name, project_info in projects.items():
        if project_info["status"] in status_filter:
            if year_filter == "All" or project_info["year"] == year_filter:
                with cols[col_index % 2]:
                    tech_tags = ''.join([f'<span class="skill-tag">{tech}</span>' for tech in project_info['tech']])
                    status_color = "#10b981" if project_info["status"] == "Completed" else "#f59e0b" if project_info["status"] == "Live" else "#6366f1"
                    
                    st.markdown(f"""
                        <div class='project-card'>
                            <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                                <span style='font-size: 40px; margin-right: 15px;'>{project_info['icon']}</span>
                                <h3 style='margin: 0;'>{project_name}</h3>
                            </div>
                            <p style='color: var(--gray);'>{project_info['description']}</p>
                            <div style='margin: 15px 0;'>
                                {tech_tags}
                            </div>
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 15px;'>
                                <span style='background: {status_color};
                                         padding: 5px 10px; border-radius: 50px; font-size: 12px;
                                         color: white;'>
                                    {project_info['status']}
                                </span>
                                <span style='color: var(--gray);'>{project_info['year']}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                col_index += 1
    
    # Project stats
    st.markdown("---")
    st.subheader("📈 Project Statistics")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.metric("Total Projects", len(projects), "6")
    with col_stat2:
        completed = sum(1 for p in projects.values() if p["status"] == "Completed")
        st.metric("Completed", completed, f"{completed}/{len(projects)}")
    with col_stat3:
        live = sum(1 for p in projects.values() if p["status"] == "Live")
        st.metric("Live", live, "+1 this month")
    with col_stat4:
        st.metric("Lines of Code", "~15K", "↑ 25%")

# CONTACT PAGE
elif page == "Contact":
    st.title("📬 Get In Touch")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                      padding: 40px; border-radius: 30px; color: white; height: 100%;'>
                <h2 style='color: white; margin-top: 0;'>Let's Connect!</h2>
                <p style='font-size: 18px; margin-bottom: 30px;'>
                    I'm always interested in hearing about new opportunities,
                    collaborations, or just having a chat about tech!
                </p>
                <div style='margin-top: 40px;'>
                    <p style='font-size: 16px;'>📧 lyndon.luke@example.com</p>
                    <p style='font-size: 16px;'>📱 +63 XXX XXX XXXX</p>
                    <p style='font-size: 16px;'>📍 Cebu City, Philippines</p>
                </div>
                <div style='margin-top: 40px;'>
                    <p style='font-size: 24px;'>
                        <a href='#' style='color: white; text-decoration: none; margin-right: 20px;'>🔗 LinkedIn</a>
                        <a href='#' style='color: white; text-decoration: none; margin-right: 20px;'>💻 GitHub</a>
                        <a href='#' style='color: white; text-decoration: none;'>📱 Twitter</a>
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_form", clear_on_submit=True):
            st.subheader("Send a Message")
            
            name = st.text_input("Full Name", placeholder="John Doe")
            email = st.text_input("Email", placeholder="john@example.com")
            subject = st.text_input("Subject", placeholder="Project Inquiry")
            message = st.text_area("Message", placeholder="Tell me about your project...", height=150)
            
            col_submit1, col_submit2 = st.columns(2)
            with col_submit1:
                submit = st.form_submit_button("📨 Send Message", use_container_width=True)
            with col_submit2:
                clear = st.form_submit_button("Clear", use_container_width=True)
            
            if submit:
                if name and email and message:
                    st.success(f"""
                        ✅ Thank you {name}! Your message has been sent.
                        I'll get back to you within 24 hours.
                    """)
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
    
    # FAQ Section
    st.markdown("---")
    st.subheader("❓ Frequently Asked Questions")
    
    with st.expander("What's your availability for freelance work?"):
        st.write("I'm currently available for part-time freelance projects. My typical response time is within 24 hours.")
    
    with st.expander("What's your preferred tech stack?"):
        st.write("I primarily work with Python (Django/Streamlit) and JavaScript (React), but I'm always learning new technologies!")
    
    with st.expander("Do you offer mentorship?"):
        st.write("Yes! I enjoy helping aspiring developers. Feel free to reach out if you need guidance in web development.")

# Footer with dynamic copyright
st.markdown("---")
current_year = datetime.now().year
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.caption(f"© {current_year} Lyndon Luke Morre | Built with Streamlit")

with col_footer2:
    st.caption("🔄 Last updated: February 2026")

with col_footer3:
    if st.button("🔝 Back to Top"):
        st.markdown("<script>window.scrollTo(0,0);</script>", unsafe_allow_html=True)