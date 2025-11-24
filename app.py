import streamlit as st
import openai

st.set_page_config(page_title="🔮 AI 신비의 타로점", page_icon="🔮")

st.title("🔮 AI 신비의 타로점")
st.write("고민을 말하면 AI 정령이 타로카드를 뽑아줍니다.")

if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
else:
    st.error("API 키가 없습니다. 설정에서 키를 넣어주세요!")

user_question = st.text_input("고민을 입력하세요 (예: 저 언제 부자 되나요?)")

if user_question:
    if not openai.api_key:
        st.warning("API 키를 먼저 설정해주세요.")
    else:
        with st.spinner("운명을 읽는 중..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "너는 타로 점술가야. 신비로운 말투로 조언해줘."},
                        {"role": "user", "content": user_question}
                    ]
                )
                st.success("해석 결과:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"에러 발생: {e}")