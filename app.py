
import streamlit as st
from PIL import Image
import os
from src.save_img import save_uploaded_img_face1 , save_uploaded_img_face2
from src.similarity import Similarity
from src.option_menus import option_menus
from src.pictures_mode import pictures_mode
from src.camera_mode import camera_mode
from src.remove_ import remove

st.set_page_config(page_title="Two-Face-Similarity", page_icon=":🙂:", layout="wide", initial_sidebar_state="expanded")

selected_mode , selected_model , selected_backend = option_menus()
remove()


st.title('Two Faces✌🏻(Similarity between two Faces)')
# st.markdown('> #### This Poject is made using  ')


if selected_mode == 'Pictures':
   

    col1 ,col2 = st.columns(2)
    with col1:
        img1 = st.file_uploader('Upload Image',key='image1')

    with col2:
        img2 = st.file_uploader('Upload New Image',key='image2')


    if img1 and img2 is not None:
        if save_uploaded_img_face1(img1) and save_uploaded_img_face2(img2):
            display_img1 = Image.open(img1)
            display_img2 = Image.open(img2)


            col3 , col4 = st.columns(2)
            with col3:
                st.image(image=display_img1,width=350,channels='BGR',caption='Your Image')

            with col4:
                st.image(image=display_img2,width=350,channels='BGR',caption='Your New Image')

            img1_path =os.path.join('images/uploaded_images/face1',img1.name)
            img2_path =os.path.join('images/uploaded_images/face2',img2.name)

            if st.button('Show Similarity'):
                try:
                    sim = Similarity()

                    similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
                    st.title(f'Similarity score: {similarity_score} %')
                except:
                    st.write('Please select Different Backend Or Model')


else:
    # if camera_mode() is not None:
        # img1_path1 , img2_path2 = camera_mode()

    col1 ,col2 = st.columns(2)
    with col1:
        img1_cam = st.camera_input('Smile Please',key='image111')

    with col2:
        img2_cam = st.camera_input('Smile Please new',key='image222')


    if img1_cam and img2_cam is not None:
        if save_uploaded_img_face1(img1_cam) and save_uploaded_img_face2(img2_cam):

            img1_path =os.path.join('images/uploaded_images/face1',img1_cam.name)
            img2_path =os.path.join('images/uploaded_images/face2',img2_cam.name)


        if st.button('Show Similarity'):
            try:
                sim = Similarity()

                similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
                st.title(f'🙂Similarity score is {similarity_score} %\n made by 👨🏻‍💻Gyan Prakash Kushwaha')
            except Exception as e:
                st.write(f'Please select Different Backend Or Model {e}')


