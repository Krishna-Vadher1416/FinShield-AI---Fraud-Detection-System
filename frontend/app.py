import streamlit as st
import requests

# ✅ Page config
st.set_page_config(page_title="FinShield AI", layout="wide")

st.title("🛡️ FinShield AI - Fraud Detection System")
st.subheader("💳 Transaction Checker")

# ✅ API URL (keep in one place)
API_URL = "http://127.0.0.1:8000/fraud/check"
HEALTH_URL = "http://127.0.0.1:8000/fraud/health"

# ✅ Check backend status
def check_backend():
    try:
        res = requests.get(HEALTH_URL, timeout=3)
        return res.status_code == 200
    except:
        return False

# 🔴 Show backend status
if check_backend():
    st.success("🟢 Backend Connected")
else:
    st.error("🔴 Backend Not Running (Start FastAPI first)")
    st.stop()  # 🚨 Stop app if backend not running


# ✅ Input fields
user_id = st.number_input("User ID", min_value=1, value=1)
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
location = st.text_input("Location", value="India")
merchant = st.text_input("Merchant", value="Amazon")
timestamp = st.text_input("Timestamp", value="2026-07-31 10:00:00")


# ✅ Button action
if st.button("🚀 Check Fraud"):

    data = {
        "user_id": int(user_id),
        "amount": float(amount),
        "location": location,
        "merchant": merchant,
        "timestamp": timestamp
    }

    try:
        with st.spinner("Analyzing transaction..."):
            

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/fraud/check",
                    json=data,
                    timeout=20
                )
                result = response.json()

                st.success("Result received")
                st.write(result["ai_explanation"])

            except requests.exceptions.Timeout:
                st.error("Backend is slow. Try again.")

        # ✅ Success response
        if response.status_code == 200:
            result = response.json()

            st.success("✅ Analysis Complete")

            # 🔍 Result
            st.markdown("### 🔍 Result")
            st.write(f"**Fraud:** {'🚨 Yes' if result['is_fraud'] else '✅ No'}")
            st.write(f"**Risk Score:** {result['risk_score']}")

            # ⚠️ Reasons
            st.markdown("### ⚠️ Reasons")
            reasons = [r for r in result["reasons"] if r]
            if reasons:
                for r in reasons:
                    st.write(f"- {r}")
            else:
                st.write("No major risk factors detected.")

            # 🤖 AI Explanation
            st.markdown("### 🤖 AI Explanation")
            st.info(result["ai_explanation"])

        else:
            # ❌ API returned error
            try:
                error_msg = response.json().get("detail", "Unknown error")
            except:
                error_msg = response.text

            st.error(f"❌ API Error: {error_msg}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to backend. Is FastAPI running?")

    except requests.exceptions.Timeout:
        st.error("❌ Request timed out")

    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")