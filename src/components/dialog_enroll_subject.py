import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time

@st.dialog("Enroll in subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to Enroll")
    join_code = st.text_input('Subject_code',placeholder='AI101')

    if st.button('Enroll Now',type='primary',width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id','name','subject_code').eq("subject_code",join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']
                # if subject even exist or not 
                check = supabase.table('subjects_student').select("*").eq("subject_id",subject['subject_id']).eq("student_id",student_id).execute()
                # is student already enrolled or not
                if check.data:
                    st.warning('You are already Enrolled in this program')
                else:
                    enroll_student_to_subject(student_id,subject['subject_id'])
                    st.success('Succesfully Enrolled!')
                    time.sleep(1)
                    st.rerun()

        else:
            st.warning("Please Enter the subject Code")