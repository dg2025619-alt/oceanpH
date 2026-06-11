import os

st.write("현재 폴더 파일 목록")
st.write(os.listdir())

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="해양 생물 다양성 분석",
    layout="wide"
)

# 제목
st.title("🌊 해양 생물 다양성 감소의 원인은 무엇일까?")
st.markdown("""
### 탐구 질문
해수 온도(SST)와 pH 변화는 해양 생물 다양성에 어떤 영향을 줄까?
""")

# 데이터 불러오기
df = pd.read_csv("realistic_ocean_climate_dataset 2.csv")

# 필요한 컬럼만 사용
analysis_df = df[[
    "SST (°C)",
    "pH Level",
    "Species Observed",
    "Marine Heatwave"
]]

# 데이터 미리보기
st.header("1️⃣ 데이터 확인")

st.dataframe(analysis_df.head())

# 기본 통계
st.header("2️⃣ 기본 통계")

st.dataframe(analysis_df.describe())

# 상관관계 계산
corr_temp = analysis_df["SST (°C)"].corr(
    analysis_df["Species Observed"]
)

corr_ph = analysis_df["pH Level"].corr(
    analysis_df["Species Observed"]
)

st.header("3️⃣ 상관관계 분석")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "수온 ↔ 생물종 수",
        f"{corr_temp:.3f}"
    )

with col2:
    st.metric(
        "pH ↔ 생물종 수",
        f"{corr_ph:.3f}"
    )

# 수온과 종 수
st.header("4️⃣ 수온과 생물 다양성")

temp_data = analysis_df[[
    "SST (°C)",
    "Species Observed"
]]

st.scatter_chart(
    temp_data,
    x="SST (°C)",
    y="Species Observed"
)

# pH와 종 수
st.header("5️⃣ pH와 생물 다양성")

ph_data = analysis_df[[
    "pH Level",
    "Species Observed"
]]

st.scatter_chart(
    ph_data,
    x="pH Level",
    y="Species Observed"
)

# 해양 열파 비교
st.header("6️⃣ 해양 열파 영향")

heatwave_avg = (
    analysis_df
    .groupby("Marine Heatwave")
    ["Species Observed"]
    .mean()
)

st.bar_chart(heatwave_avg)

# 결론
st.header("7️⃣ 결론")

st.success(f"""
• 수온과 종 수 상관계수: {corr_temp:.3f}

• pH와 종 수 상관계수: {corr_ph:.3f}

데이터 분석 결과 수온이 높아질수록
생물종 수가 감소하는 경향이 나타났다.

또한 pH가 낮아질수록
생물종 수가 감소하는 경향도 확인되었다.

따라서 해양 생물 다양성 감소는
수온 상승과 해양 산성화와 관련이 있다고 볼 수 있다.
""")
