import streamlit as st
from rembg import remove
from PIL import Image
import io

# Page Configuration
st.set_page_config(page_title="AI Background Remover", layout="centered")

st.title("✂️ AI Background Remover")
st.write("Apni image upload karein aur AI khud background saaf kar dega!")

# Image Upload
uploaded_file = st.file_uploader("Image select karein...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Original Image dikhana
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original")
        st.image(image, use_container_width=True)

    # Background Removal Process
    with st.spinner("AI kaam kar raha hai..."):
        # Image ko bytes mein convert karna aur remove function chalana
        input_bytes = uploaded_file.getvalue()
        output_bytes = remove(input_bytes)
        output_image = Image.open(io.BytesIO(output_bytes))

    with col2:
        st.header("Result")
        st.image(output_image, use_container_width=True)

    # Download Button
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Transparent Image",
        data=byte_im,
        file_name="bg_removed.png",
        mime="image/png"
    )