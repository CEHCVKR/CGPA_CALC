import streamlit as st

def calculate_cgpa():
    st.title("VVIT CGPA Calculator")

    semesters = st.number_input("Enter the number of semesters:", min_value=1, step=1)

    if semesters:
        sgpas = []
        credits = []
        total_weighted_sgpa = 0
        total_credits = 0

        with st.form(key='cgpa_form'):
            for sem in range(1, semesters + 1):
                sgpa = st.number_input(f"Enter SGPA for Semester {sem}:", min_value=0.0, format="%.2f", key=f"sgpa_{sem}")
                credit = st.number_input(f"Enter total credits for Semester {sem}:", min_value=0.0, format="%.1f", key=f"credit_{sem}")
                sgpas.append(sgpa)
                credits.append(credit)
            submit_button = st.form_submit_button(label='Calculate CGPA')

        if submit_button:
            for sgpa, credit in zip(sgpas, credits):
                total_weighted_sgpa += sgpa * credit
                total_credits += credit

            if total_credits == 0:
                st.error("Total credits cannot be zero. Please check your inputs.")
            else:
                cgpa = total_weighted_sgpa / total_credits
                st.success(f"🎯 Your CGPA across {semesters} semesters is: **{cgpa:.2f}**")

if __name__ == "__main__":
    calculate_cgpa()
