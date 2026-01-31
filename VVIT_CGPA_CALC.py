import streamlit as st

def calculate_cgpa():
    st.title("VVIT CGPA Calculator")

    st.write("Select mode:")
    mode = st.radio("", ("Custom Credits", "Fixed Credits (VVIT)"), horizontal=True)

    if mode == "Custom Credits":
        semesters = st.number_input("Enter the number of semesters:", min_value=1, max_value=7, step=1)
        if semesters:
            sgpas = []
            credits = []
            total_weighted_sgpa = 0
            total_credits = 0
            with st.form(key='cgpa_form_custom'):
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
    else:
        st.write("\n**Fixed Credits per Semester (VVIT):**\n\n1: 19.5, 2: 19.5, 3: 21.5, 4: 21.5, 5: 21.5, 6: 21.5, 7: 23")
        semesters = st.number_input("Enter the number of semesters:", min_value=1, max_value=7, step=1, key="fixed_sem")
        fixed_credits = {1: 19.5, 2: 19.5, 3: 21.5, 4: 21.5, 5: 21.5, 6: 21.5, 7: 23}
        if semesters:
            sgpas = []
            total_weighted_sgpa = 0
            total_credits = 0
            with st.form(key='cgpa_form_fixed'):
                for sem in range(1, semesters + 1):
                    sgpa = st.number_input(f"Enter SGPA for Semester {sem} (Credits: {fixed_credits[sem]}):", min_value=0.0, format="%.2f", key=f"fixed_sgpa_{sem}")
                    sgpas.append(sgpa)
                submit_button = st.form_submit_button(label='Calculate CGPA')
            if submit_button:
                for sem, sgpa in enumerate(sgpas, 1):
                    total_weighted_sgpa += sgpa * fixed_credits[sem]
                    total_credits += fixed_credits[sem]
                if total_credits == 0:
                    st.error("Total credits cannot be zero. Please check your inputs.")
                else:
                    cgpa = total_weighted_sgpa / total_credits
                    st.success(f"🎯 Your CGPA across {semesters} semesters is: **{cgpa:.2f}**")

if __name__ == "__main__":
    calculate_cgpa()
