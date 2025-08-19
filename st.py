import pandas as pd
import numpy as np
import streamlit as st
import json
import base64
st.set_page_config(layout="wide")

# Sidebar navigation
page = st.sidebar.radio(" ", ["🏠 Home", "👨‍💼 About Me", "📄 Resume", "📁 Projects", "📬 Contacts"])

# 🏠 HOME SECTION
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("Hi, I'm Akshat Jangid ")
        st.markdown("<h2 style='color: green;'>Data Scientist| ML & DL Enthusiast</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            I am an aspiring Data Scientist with a strong foundation in data analysis, machine learning, and statistical modeling.
            My technical skill set includes Python, Pandas, NumPy, Scikit-learn, TensorFlow, OpenCV, Flask and Streamlit. 
            I have hands-on experience working on end-to-end projects involving data cleaning, feature engineering, model training, 
            and deployment through interactive web applications.  
            <br><br>
            Currently, I am focused on developing robust machine learning models for domains such as customer satisfaction prediction and stock price forecasting, 
            with a strong emphasis on practical implementation and performance optimization.  
            <br><br>
            Driven by curiosity and continuous learning, I aim to contribute to impactful, data-driven solutions in business and technology.
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("casual photo2-black.jpg", width=350)
        st.markdown(
        """
        <div style='text-align: center; margin-top: 25px;'>
            <a href="https://www.linkedin.com/in/akshat-jangid/" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="35" style="margin-right: 20px;">
            </a>
            <a href="https://www.linkedin.com/in/akshat-jangid" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="margin-right: 20px;">
            </a>
            <a href="https://www.instagram.com/your_username" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="35">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
# 👨‍💼 ABOUT ME SECTION
elif page == "👨‍💼 About Me":
    try:
        with open("about_me.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        st.markdown("## 👨‍💼 About Me")
        st.markdown(f"**{data['name']}**")
        st.write(data['bio'])

        st.markdown("### 🔧 Skills")
        st.write(", ".join(data['skills']))

        st.markdown("### 📚 Currently Learning")
        for topic in data['learning']:
            st.write(f"- {topic}")


        st.markdown("### 🎯 Career Goal")
        st.write(data['goals'])

    except FileNotFoundError:
        st.error("❌ 'about_me.json' not found. Please make sure the file exists in the same folder.")


# Other pages (future placeholders)
elif page == "📄 Resume":
    st.header("My Resume")
    st.markdown("Click the button below to download my latest resume:")
    st.markdown("---")
    with open("AKSHAT JANGID NEW RESUME  .pdf", "rb") as file:
        resume_data=file.read()
    st.download_button(label="Download Resume",
                        data=resume_data,
                          file_name="AKSHAT JANGID NEW RESUME  .pdf",
                        mime="application/pdf"
                        ) 
    
    with open("resume.png", "rb") as image_file:
     encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f'<img src="data:image/png;base64,{encoded}" width="700"/>',
        unsafe_allow_html=True
    )
    

elif page == "📁 Projects":
    st.header("Projects")

    try:
        with open("about_me.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for project in data['projects']:
            st.subheader(f"🔹 {project['title']}")
            st.write(project['description'])
            st.markdown(f"[GitHub Repository]({project['github']})")
            st.markdown(f"[App Link]({project['app link']})")
            st.markdown("---")

    except FileNotFoundError:
        st.error("❌ 'about_me.json' not found.")


elif page == "📬 Contacts":
    st.header("Get in Touch")
    st.markdown("""you can reach out to me via the following platforms:
    - 📧 Email: [akshatjangid23@gmail.com](mailto:akshatjangid23@gmail.com)
    - 💼 LinkedIn: [linkedin.com/in/akshatjangid](https://linkedin.com/in/akshatjangid)
    - 🐙 GitHub: [github.com/akshatjangid](https://github.com/akshatjangid)
    - 📱 Phone: +91-8854004221   """)

    st.markdown("---")
    st.subheader("Send me a message")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
          st.success("✅ Thank you! Your message was received.")