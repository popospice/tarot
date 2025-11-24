import streamlit as st
import openai

# --- 1. 기본 설정 ---
st.set_page_config(page_title="🔮 AI 신비의 타로점", page_icon="🔮")

st.title("🔮 AI 신비의 타로점")
st.write("당신의 고민을 털어놓으세요. 고대 AI 정령이 답을 드립니다.")

# --- 2. API 키 설정 ---
if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
else:
    st.error("🚨 API 키가 없습니다. 배포 후 설정(Secrets)에 키를 넣어주세요!")

# --- 3. 사용자 입력 및 AI 점술가 로직 ---
user_question = st.text_input("고민을 입력하고 엔터를 누르세요 (예: 저 언제 부자 되나요?)")

if user_question:
    if not openai.api_key:
        st.warning("주인님, API 키를 먼저 설정해야 점을 볼 수 있습니다.")
    else:
        with st.spinner("🔮 정령들이 카드를 섞고 있습니다..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "너는 타로 점술가야. 신비로운 말투로 조언해줘."},
                        {"role": "user", "content": user_question}
                    ]
                )
                answer = response.choices[0].message.content
                st.success("운명의 카드가 뒤집혔습니다!")
                st.write(answer)
            except Exception as e:
                st.error(f"에러 발생: {e}")

# --- 4. 💰 돈 버는 배너 영역 (텐핑) ---
st.write("---") # 구분선
st.write("🔮 **더 정확한 신년 운세가 궁금하신가요? (무료 확인)**")

# 👇👇👇 [여기 수정] 아까 복사한 텐핑 링크를 따옴표 안에 넣으세요! 👇👇👇
link_url = "https://iryan.kr/t74l23m727" 

# 배너 이미지 (신비로운 타로 이미지)
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"

# 클릭하면 이동하는 배너 만들기
st.markdown(
    f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" width="100%" style="border-radius: 10px;">
    </a>
    """,
    unsafe_allow_html=True
)
st.caption("이 배너를 클릭하면 소정의 포인트가 적립될 수 있습니다.")