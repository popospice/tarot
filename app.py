# --- 광고 배너 영역 ---
st.write("---") # 구분선

# 1. 광고 문구
st.write("🔮 **이 타로 카드가 마음에 드시나요? 실물로도 만나보세요!**")

# 2. 클릭 가능한 이미지 배너 만들기 (HTML 사용)
# 아래 링크는 예시입니다. 나중에는 본인의 쿠팡 파트너스 링크로 바꾸세요.
link_url = "https://www.coupang.com/np/search?component=&q=타로카드" 
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-Xn2XyTq7YyXvR7p_Xw&usqp=CAU" # 타로카드 이미지 주소

st.markdown(
    f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" width="100%" style="border-radius: 10px;">
    </a>
    """,
    unsafe_allow_html=True
)