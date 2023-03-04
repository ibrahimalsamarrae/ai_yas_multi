import streamlit as st


from streamlit_option_menu import option_menu


selected = option_menu("Main Menu", ["Home", 'Settings'], 
icons=['house', 'gear'], menu_icon="cast", default_index=1)
selected
st.title("Hakkında")
st.header("Yapay zeka tarafından makine öğrenimi kullanılarak oluşturulmuş bir programdır. Model, farklı yaşlardaki 23.000 görüntü örneği kullanılarak eğitildi. Modelin eğitiminde sinir ağlarından en son algoritmalar kullanılmıştır. Program çok güvenlidir ve gizliliğinizi korur")


          
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 60%;
background-color: black;
color: white;
text-align: center;
}
 #MainMenu {visibility: hidden;}
</style>

<div class="footer">
</center><p> by ALSAMARRAE</p><center> 
</div>

"""

st.markdown(footer, unsafe_allow_html=True)

 