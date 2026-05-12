import streamlit as st

SEMESTER_LABELS = {
    1: "1-1 (1st Sem)",
    2: "1-2 (2nd Sem)",
    3: "2-1 (3rd Sem)",
    4: "2-2 (4th Sem)",
    5: "3-1 (5th Sem)",
    6: "3-2 (6th Sem)",
    7: "4-1 (7th Sem)",
    8: "4-2 (8th Sem)",
}


def calculate_cgpa():
    st.title("VVIT CGPA Calculator")
    st.caption("Vasireddy Venkatadri Institute of Technology (Autonomous)")

    student_type = st.radio("Select student type:", ("Regular", "Lateral"), horizontal=True)
    start_semester = 3 if student_type == "Lateral" else 1

    st.write("Select mode:")
    mode = st.radio("", ("Custom Credits", "Fixed Credits (VVIT)"), horizontal=True)

    if mode == "Custom Credits":
        semesters = st.selectbox(
            "Select last completed semester:",
            options=list(range(start_semester, 9)),
            format_func=lambda sem: SEMESTER_LABELS[sem],
        )
        if semesters:
            sgpas = []
            credits = []
            total_weighted_sgpa = 0
            total_credits = 0
            with st.form(key='cgpa_form_custom'):
                for sem in range(start_semester, semesters + 1):
                    sgpa = st.number_input(
                        f"Enter SGPA for Semester {SEMESTER_LABELS[sem]}:",
                        min_value=0.0,
                        format="%.2f",
                        key=f"sgpa_{sem}",
                    )
                    credit = st.number_input(
                        f"Enter total credits for Semester {SEMESTER_LABELS[sem]}:",
                        min_value=0.0,
                        format="%.1f",
                        key=f"credit_{sem}",
                    )
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
                    st.success(f"🎯 Your CGPA up to {SEMESTER_LABELS[semesters]} is: **{cgpa:.2f}**")
    else:
        st.write("\n**Fixed Credits per Semester (VVIT):**\n\n1: 19.5, 2: 19.5, 3: 21.5, 4: 21.5, 5: 21.5, 6: 21.5, 7: 23, 8: 12")
        semesters = st.selectbox(
            "Select last completed semester:",
            options=list(range(start_semester, 9)),
            format_func=lambda sem: SEMESTER_LABELS[sem],
            key="fixed_sem",
        )
        fixed_credits = {1: 19.5, 2: 19.5, 3: 21.5, 4: 21.5, 5: 21.5, 6: 21.5, 7: 23, 8: 12}
        if semesters:
            sgpas = []
            total_weighted_sgpa = 0
            total_credits = 0
            with st.form(key='cgpa_form_fixed'):
                for sem in range(start_semester, semesters + 1):
                    sgpa = st.number_input(
                        f"Enter SGPA for Semester {SEMESTER_LABELS[sem]} (Credits: {fixed_credits[sem]}):",
                        min_value=0.0,
                        format="%.2f",
                        key=f"fixed_sgpa_{sem}",
                    )
                    sgpas.append(sgpa)
                submit_button = st.form_submit_button(label='Calculate CGPA')
            if submit_button:
                for sem, sgpa in zip(range(start_semester, semesters + 1), sgpas):
                    total_weighted_sgpa += sgpa * fixed_credits[sem]
                    total_credits += fixed_credits[sem]
                if total_credits == 0:
                    st.error("Total credits cannot be zero. Please check your inputs.")
                else:
                    cgpa = total_weighted_sgpa / total_credits
                    st.success(f"🎯 Your CGPA up to {SEMESTER_LABELS[semesters]} is: **{cgpa:.2f}**")


if __name__ == "__main__":
    calculate_cgpa()
