import streamlit as st
import time
from pathlib import Path
import base64

# Initialize session state for button cooldown
if 'last_audio_click' not in st.session_state:
    st.session_state.last_audio_click = 0

# Set background image using base64 encoding (more reliable)
image_path = Path(r"c:\Users\kwstr\OneDrive\Pictures\Screenshots 1\Screenshot 2026-01-03 002326.png")
if image_path.exists():
    with open(image_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{img_data}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Make all text bright orange */
        .stApp, .stApp * {{
            color: #FFA500 !important;
        }}
        /* Increase text size for everything except the h1 title */
        .stApp *:not(h1) {{
            font-size: 18px !important;
        }}
        /* Ensure titles and headings are orange */
        h1, h2, h3, h4, h5, h6 {{
            color: #FFA500 !important;
        }}
        /* Input labels and text orange */
        label, p, div, span {{
            color: #FFA500 !important;
        }}
        /* Button text orange */
        button {{
            color: #FFA500 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Background image not found at provided path.")

st.title("goat rater 3009")

ace = st.text_input("is ace a goat:")

if ace:
    if ace in ("lowkey", "yes", "perhaps", "ofc", "idk"):
        st.write("ding ding ding!")
    else:
        st.write("something someone with 67 iq would say")

ace2 = st.text_input("how much of a goat is he:")
if ace2:
    if ace2 in ("hes a pretty big goat", "lowkey a big goat", "goated enough"):
        st.write("yeah our awesome leader no cap")
    else:
        st.write("your tweaking on fahads soul")


sami = st.text_input("is sami a good artist:")
if sami:
    if sami in ("yes yes my bro", "yeah", "i think so", "duh", "yes"):
        st.write("facts!")
    else:
        st.write("boy what the hell boy.")

# Check if button should be disabled (4 second cooldown)
current_time = time.time()
time_since_click = current_time - st.session_state.last_audio_click
button_disabled = time_since_click < 4

if st.button("aces voice", disabled=button_disabled):
    st.session_state.last_audio_click = current_time
    from pathlib import Path
    import base64
    import streamlit.components.v1 as components

    audio_path = Path(r"C:\Users\kwstr\Downloads\guy with deep voice says hello there.mp3")
    if audio_path.exists():
        data = audio_path.read_bytes()
        b64 = base64.b64encode(data).decode()
        # Render audio and stop after 3 seconds using JS
        audio_html = f"""
        <audio id='ace-audio' autoplay>
          <source src="data:audio/mp3;base64,{b64}" type="audio/mpeg">
        </audio>
        <script>
        setTimeout(function() {{
            var audio = document.getElementById('ace-audio');
            if(audio) {{
                audio.pause();
                audio.currentTime = 0;
                audio.remove();
            }}
        }}, 3000);
        </script>
        """
        components.html(audio_html, height=1)
    else:
        st.write("Could not play audio. Check the file path.")

# Show cooldown timer if button is disabled
if button_disabled:
    remaining = int(4 - time_since_click)
    st.write(f"Button available in {remaining} seconds")
    st.rerun()

# Photo display: hidden default path (not shown to users) and show image for 4 seconds
photo_path = r"C:\Users\kwstr\Downloads\photo.jpg"
if st.button("Show photo"):
    from pathlib import Path
    import base64
    import streamlit.components.v1 as components

    p = Path(photo_path)
    if p.exists():
        data = p.read_bytes()
        b64 = base64.b64encode(data).decode()
        html = f"""
        <script>
        (function() {{
            try {{
                const parentDoc = window.parent.document;
                const existing = parentDoc.querySelectorAll('[id^="st-photo-"]');
                existing.forEach(e => e.remove());
                const id = 'st-photo-' + Date.now();
                const img = parentDoc.createElement('img');
                img.id = id;
                img.src = "data:image/jpeg;base64,{b64}";
                img.style.position = 'fixed';
                img.style.top = '10px';
                img.style.right = '10px';
                img.style.maxWidth = '300px';
                img.style.zIndex = 2147483647;
                parentDoc.body.appendChild(img);
                setTimeout(function() {{
                    const e = parentDoc.getElementById(id);
                    if (e) e.remove();
                }}, 4000);
            }} catch(e) {{ console.log(e); }}
        }})();
        </script>
        """
        components.html(html, height=1)
    else:
        st.write("Photo not found at configured path.")


if st.button("sami's art"):
    from PIL import Image
    image_path = r"c:\Users\kwstr\OneDrive\Pictures\Screenshots 1\Screenshot 2026-01-02 225453.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="sami's masterpiece")
    except Exception:
        st.write("Could not open image. Check the file path.")

