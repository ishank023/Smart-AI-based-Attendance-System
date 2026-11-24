import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time
from PIL import Image
@st.dialog('Capture or Uploadd photos')
def add_photos_dialog():
  st.write('Add Classroom photos to scan for Attendance')

  if 'photo_tab' not in st.session_state:
    st.session_state.photo_tab = 'camrea'


  t1,t2 = st.columns(2)
  with t1:
    type_camrea = 'primary' if st.session_state.photo_tab == 'camrea' else 'tertiary'
    if st.button('Camrea',type=type_camrea,width='stretch'):
      st.session_state.photo_tab = 'camrea'
  with t2:
    type_upload = 'primary' if st.session_state.photo_tab == 'upload' else 'tertiary'
    if st.button('upload photos',type=type_upload,width='stretch'):
      st.session_state.photo_tab = 'upload'
  if st.session_state.photo_tab == 'camrea':
    cam_photo = st.camera_input('Take Snapshot',key='dialog_cam')
    if cam_photo:
       st.session_state.attendance_images.append(Image.open(cam_photo))
       st.toast('Photo Captured')
       st.rerun()
  if st.session_state.photo_tab == 'upload':
    uploaded_files = st.file_uploader('Choose Image Files',type = ['jpg','png','jpeg'],accept_multiple_files=True,key = 'dialog_upload')
    if uploaded_files:
      for f in uploaded_files:
        st.session_state.attendace_images.append(Image.open(f))
        st.toast("Photo Uploaded Succesfully")
        st.rerun()

  st.divider()
  if st.button('Done', type='primary',width='stretch'):
    st.rerun()