import streamlit as st
import os
from services.reviewer import review


st.set_page_config(page_title="Code Review Agent", layout="wide")

st.title("Code Review System")
st.write("Upload files, paste code, or scan folders to get intelligent review feedback.")
st.write("Created by HET MAYUR THORIA")

# ---- INPUT MODE ----
mode = st.radio(
    "Choose Input Type",
    ["Paste Code", "Upload File(s)", "Folder Path"]
)


# ---- PASTE CODE ----
if mode == "Paste Code":
    code_input = st.text_area("Paste your code here", height=300)

    if st.button("Run Review") and code_input.strip():
        with st.spinner("Reviewing..."):
            issues, ai_review = review(code_input)

        st.subheader("📏 Rule Based Findings")
        if issues:
            for i in issues:
                st.warning(i)
        else:
            st.success("No basic rule violations.")

        st.subheader("🤖 AI Review")
        st.write(ai_review)


# ---- FILE UPLOAD ----
elif mode == "Upload File(s)":
    files = st.file_uploader("Upload code files", accept_multiple_files=True)

    if files and st.button("Run Review"):
        for file in files:
            code = file.read().decode("utf-8", errors="ignore")

            st.divider()
            st.subheader(f"📄 {file.name}")

            with st.spinner("Reviewing..."):
                issues, ai_review = review(code)

            st.subheader("📏 Rule Based Findings")
            if issues:
                for i in issues:
                    st.warning(i)
            else:
                st.success("No basic rule violations.")

            st.subheader("🤖 AI Review")
            st.write(ai_review)


# ---- FOLDER SCAN ----
elif mode == "Folder Path":
    folder = st.text_input("Enter folder path")

    if st.button("Run Review") and os.path.isdir(folder):
        for root, _, filenames in os.walk(folder):
            for name in filenames:
                if name.endswith(".py"):
                    path = os.path.join(root, name)

                    with open(path, "r", errors="ignore") as f:
                        code = f.read()

                    st.divider()
                    st.subheader(f"📄 {name}")

                    with st.spinner("Reviewing..."):
                        issues, ai_review = review(code)

                    st.subheader("📏 Rule Based Findings")
                    if issues:
                        for i in issues:
                            st.warning(i)
                    else:
                        st.success("No basic rule violations.")

                    st.subheader("🤖 AI Review")
                    st.write(ai_review)

    elif folder:
        st.error("Invalid folder path.")
