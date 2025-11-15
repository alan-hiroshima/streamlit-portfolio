import streamlit as st
import pandas as pd
import os

def main():
    st.set_page_config(
        page_title="Autobiography & Portfolio",
        page_icon=":sparkles:",
        layout="wide",
    )

    # HEADER
    col1, col2 = st.columns([1, 3])
    with col1:
        local_profile = os.path.join("images", "cover.jpg")
        if os.path.exists(local_profile):
            st.image(local_profile, width=140, caption="Profile")
        else:
            st.image(
                "https://avatars.githubusercontent.com/u/9919?v=4",
                width=140,
                caption="Profile"
            )
    with col2:
        st.title("Alan Christian Neis")
        st.markdown("***")
        st.write(
            "Welcome to my digital space. I am currently in the process of discovering oneself and learning new things."
        )

    st.write("---")

    # TABS
    tabs = st.tabs(["About me", "Portfolio", "Contact", "Resume"])

    # ----------------- ABOUT ME -----------------
    with tabs[0]:
        st.header("About me")
        st.markdown(
            "I was a student who discovered how computers can turn ideas into reality and make a lot of money😂. "
            "Over time I learned to love coding, building projects, and collaborating with others."
        )

        st.subheader("Education")
        st.markdown(
            """
        - Bachelor of Science in Computer Science, Cebu Institute of Technology (2023 - Present)
        - Graduated with honors from STI College of Ormoc (2022 - 2023)
        """
        )

        st.subheader("Hobbies and Interests")
        st.markdown(
            """
        - Sports (Basketball, Pickleball, Badminton, Table Tennis)
        - Hiking
        - Travel
        - Playing video games
        """
        )

        with st.expander("Quick fun facts"):
            st.markdown(
                """
        - Wants to try golf  
        - I am a fan of F1 racing  
        - I don't really eat vegetables  
        - I haven't flown on an airplane  
        - I play video games but I suck at playing them  
        """
            )

        st.subheader("Skills & Tools")
        # Skills in 2 columns layout
        programming = [
            "Java", "C++", "C", "Python", "Kotlin",
            "JavaScript", "HTML", "CSS", "MySQL", "GitHub"
        ]
        productivity = ["Microsoft 365", "Google Workspace", "Zoom"]
        design = ["Canva", "Figma"]

        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("### Programming & Development")
            for item in programming:
                st.markdown(f"- {item}")

        with col_right:
            st.markdown("### Productivity & Collaboration")
            for item in productivity:
                st.markdown(f"- {item}")
            st.write("")
            st.markdown("### Design & Content Tools")
            for item in design:
                st.markdown(f"- {item}")

    # ----------------- PORTFOLIO -----------------
    with tabs[1]:
        st.header("My Portfolio")
        st.markdown("Below are a few snapshots of past and recent work. Click a project to expand details.")

        projects = [
            {
                "title": "Space Shooter",
                "short": "A classic arcade space shooter featuring pixel ships, endless waves of enemies, and powerful weapon boosts.",
                "image": "images/space.png",
                "link": "https://github.com/alan-hiroshima/Java_Capstne.git",
                "tags": ["Java"],
                "year": 2024,
                "details": "Built this game to deepen my knowledge of OOP Principles and also learn basics of project creation."
            },
            {
                "title": "Inmate Escape",
                "short": "A game where the prisoner runs from the police while avoiding obstacles",
                "image": "images/inmate.png",
                "link": "https://github.com/rrraine/Inmate_Escape.git",
                "tags": ["Java", "CSS"],
                "year": 2025,
                "details": "Inspired by games like Zombie Tsunami and Extreme Pamplona."
            },
            {
                "title": "Uplift",
                "short": "A mobile app that delivers inspirational quotes and promotes positivity through personalized, uplifting messages.",
                "image": "images/quote.png",
                "link": "https://github.com/alan-hiroshima/Mobile_Development___Uplift.git",
                "tags": ["Kotlin"],
                "year": 2024,
                "details": "Built to give users motivational quotes for posting and for mobile development practice."
            },
        ]

        PLACEHOLDER = "https://via.placeholder.com/480x320.png?text=No+Image"

        # Display projects in a grid
        cols_per_row = 3
        for i, p in enumerate(projects):
            if i % cols_per_row == 0:
                cols = st.columns(cols_per_row)
            col = cols[i % cols_per_row]
            with col:
                img_path = p.get("image", "")
                if img_path and os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.image(PLACEHOLDER, use_container_width=True)

                st.subheader(p["title"])
                st.write(p["short"])
                if p.get("tags"):
                    st.markdown("**Tags:** " + ", ".join(p["tags"]))
                st.caption(f"Year: {p.get('year', '')}")

                with st.expander("More details"):
                    st.write(p.get("details", ""))
                    if p.get("link"):
                        st.markdown(f"[View project →]({p['link']})", unsafe_allow_html=True)

        st.markdown("---")
        st.info("To add project images: upload them below and then reference them in the projects list (e.g., 'images/filename.png').")

        uploaded_files = st.file_uploader(
            "Upload project images (optional)",
            accept_multiple_files=True,
            type=["png", "jpg", "jpeg"]
        )
        if uploaded_files:
            os.makedirs("images", exist_ok=True)
            for up in uploaded_files:
                save_path = os.path.join("images", up.name)
                with open(save_path, "wb") as f:
                    f.write(up.getbuffer())
            st.success(f"Saved {len(uploaded_files)} file(s) to /images. Refresh the portfolio list to use them.")

    # ----------------- CONTACT -----------------
    with tabs[2]:
        st.header("Contact me")
        st.markdown("Feel free to reach out using the form below or via the provided links.")

        col_form, col_links = st.columns([2, 1])
        with col_form:
            with st.form("contact_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                message = st.text_area("Message")
                submitted = st.form_submit_button("Send")
                if submitted:
                    st.success("Thanks! Your message was submitted — I'll get back to you soon.")
                    st.write("(This demo doesn't actually send emails.)")

        with col_links:
            st.markdown("### Reach me")
            contact_email = "alanchristianneis@gmail.com"
            linkedin_url = "https://www.linkedin.com/in/yourprofile/"
            github_url = "https://github.com/alan-hiroshima"

            st.markdown(
                f"""
            <a href="mailto:{contact_email}">📧 Email</a><br>
            <a href="{linkedin_url}" target="_blank">🔗 LinkedIn</a><br>
            <a href="{github_url}" target="_blank">🐙 GitHub</a>
            """,
                unsafe_allow_html=True,
            )

    # ----------------- RESUME -----------------
    with tabs[3]:
        st.header("Resume / CV")
        resume_text = """
ALAN CHRISTIAN NEIS
27 Junquera Ext., Brgy. Santa Cruz, Cebu
Email: alanchristianneis@gmail.com
Phone: +63 9205667058

TECHNICAL SKILLS
Programming & Development:
- Java, C++, C, Python, Kotlin, JavaScript, HTML, CSS, MySQL, GitHub

Productivity & Collaboration:
- Microsoft 365, Google Workspace, Zoom

Design & Content Tools:
- Canva, Figma

LEADERSHIP & ACTIVITIES
Assistant VP External — Senior Plus Red Cross Youth (SPRCY) (2022–2023)
- Assisted in managing outreach programs and workshops.
- Helped secure resources from external partners.
- Coordinated with barangay officials and Ormoc City Red Cross Chapter.

Logistics Committee Member — CIT-U Computer Science (2023–2024)
- Coordinated logistics for smooth execution of events.
- Assisted in CSS Tutorials for exam preparation.
- Provided administrative and registration support.

EDUCATION
Cebu Institute of Technology – University (2023–Present)
- Bachelor of Science in Computer Science

STI College Ormoc (2022–2023)
- STEM Strand
- Graduated with 94% General Average — With Honors

ACLC College of Ormoc (2021–2022)
- STEM Strand
"""
        st.code(resume_text)
        st.download_button(
            "Download resume (TXT)",
            data=resume_text.encode("utf-8"),
            file_name="resume.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    main()
