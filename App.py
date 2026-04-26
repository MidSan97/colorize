from colorize import device
from colorize .device_id import DeviceId
from colorize .visualize import *
import warnings
import streamlit as st
from PIL import Image
from pathlib import Path

device.set(device = DeviceId.GPU0)

plt.style.use('dark_background')
warnings.filterwarnings("ignore", category = UserWarning, message = ".*?Your .*? set is empty.*?")



def ImageColorizer(render_factor):
    imageColorizer = get_image_colorizer(artistic = True)

    source_url = None
    source_path = './test_images/image.png'
    result_path = None

    if source_url is not None:
        result_path = imageColorizer.plot_transformed_image_from_url(url = source_url, path = source_path, render_factor = render_factor, compare = True)
    else:
        result_path = imageColorizer.plot_transformed_image(path = source_path, render_factor = render_factor, compare = True)

    return Image.open(result_path)


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.title("Colorizer")
    st.header("")

    activities = ["About", "Image Colorization"]
    activity = st.sidebar.selectbox("Select Activty", activities)

    if activity == 'About':
        intro_markdown = read_markdown_file('./doc/about.md')
        st.markdown(intro_markdown, unsafe_allow_html = True)
    
    if activity == 'Image Colorization':
        st.subheader("Image Colorization")
        
        image_file = st.file_uploader("Upload Image")
        
        render_factor = ["35", "40", "45"]
        factor = st.selectbox("Render Factor", render_factor)
        
        st.markdown("* * *")

        if image_file is not None: 
            img = Image.open(image_file)
            img.save('./test_images/image.png')
            
            if st.button('Process'):
                factor = int(factor)
                colorImg = ImageColorizer(render_factor = factor)
                
                st.image(img, use_column_width = True)
                st.image(colorImg, use_column_width = True)
                
                st.balloons()

main()