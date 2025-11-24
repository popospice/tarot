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
    st.error("🚨 API 키가 설정되지 않았습니다. 배포 후 설정(Secrets)에 키를 넣어주세요!")

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
                        {"role": "system", "content": "너는 신비로운 타로 점술가야. 말투는 '~하게나', '~하는군' 같은 신비로운 말투를 써. 사용자의 고민에 대해 타로 카드 한 장을 무작위로 뽑은 척하고, 그 카드의 의미를 해석해줘. 희망적이지만 뼈 때리는 조언도 섞어서 해줘."},
                        {"role": "user", "content": user_question}
                    ]
                )
                answer = response.choices[0].message.content
                st.success("운명의 카드가 뒤집혔습니다!")
                st.write(answer)
                st.balloons()
            except Exception as e:
                st.error(f"정령과의 연결이 끊겼습니다: {e}")

# --- 4. 광고 배너 영역 (이미지 주소 수정됨!) ---
st.write("---") 
st.write("🔮 **이 타로 카드가 마음에 드시나요? 실물로도 만나보세요!**")

# 클릭 가능한 배너
link_url = "https://www.coupang.com/np/search?component=&q=타로카드" 
# 안정적인 위키백과 타로카드 이미지 사용
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"

st.markdown(
    f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" width="100%" style="border-radius: 10px;">
    </a>
    """,
    unsafe_allow_html=True
)
# --- 광고 배너 설정 ---

# 1. 링크 붙여넣기 (텐핑에서 복사한 주소)
link_url = "http://tenping.kr/xxxxxx" 

# 2. 이미지 바꾸기 (텐핑 광고랑 어울리는 이미지로)
# 운세 광고라면 아래 같은 신비한 이미지 그대로 써도 좋습니다.
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"

# 3. 배너 제목 바꾸기
st.write("🔮 **더 정확한 2025년 신년 운세가 궁금하다면? (무료 보기)**") # 멘트 수정