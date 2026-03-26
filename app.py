import streamlit as st
import time


def score_tone(score: int) -> str:
    if score >= 75:
        return "high"
    if score >= 45:
        return "mid"
    return "low"


st.set_page_config(
    page_title="Sustainlytics",
    page_icon="🌿",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Manrope', 'Segoe UI', sans-serif !important;
        color: #22312B !important;
    }

    .stApp {
        background-color: #F3F5F4;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        color: #1F4D3A !important;
        letter-spacing: 0.2px;
    }

    div[data-testid="stMetricValue"],
    div[data-testid="stMetricLabel"] {
        color: #1F4D3A !important;
    }

    div[data-baseweb="select"] > div,
    .stTextInput > div > div > input,
    .stNumberInput input,
    .stTextArea textarea {
        background-color: #E5EAE7 !important;
        border: 1px solid #C7D1CB !important;
        border-radius: 10px !important;
        color: #22312B !important;
    }

    .stButton > button {
        background-color: #1F4D3A !important;
        color: #F3F5F4 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.55rem 1rem !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        background-color: #2B6A50 !important;
    }

    .supplier-card {
        background: #FFFFFF;
        border-radius: 10px;
        border: 1px solid #DFE5E1;
        box-shadow: 0 8px 22px rgba(21, 49, 37, 0.10);
        padding: 1rem 1rem 0.8rem 1rem;
        margin-bottom: 0.8rem;
    }

    .score-label {
        font-weight: 600;
        font-size: 0.92rem;
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }

    .score-low .score-label { color: #C0352B; }
    .score-mid .score-label { color: #C98A1F; }
    .score-high .score-label { color: #1F8A4C; }

    .score-low div[data-testid="stProgressBar"] > div > div {
        background-color: #D94A3A !important;
    }
    .score-mid div[data-testid="stProgressBar"] > div > div {
        background-color: #E0A02F !important;
    }
    .score-high div[data-testid="stProgressBar"] > div > div {
        background-color: #2E9F5A !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Keep validation messages at the top of the page.
alert_placeholder = st.empty()

st.title("Sustainlytics")
st.caption("Cost vs Carbon decision support")

st.subheader("Supplier Optimization")
left, right = st.columns(2)
with left:
    st.text_input("Company")
    st.slider("Cost vs Sustainability", min_value=0, max_value=100, value=50)
with right:
    budget_input = st.text_input("Budget (USD)", placeholder="e.g. 10000")
    run_clicked = st.button("Run optimization")

if run_clicked:
    budget_value = budget_input.strip()
    if not budget_value:
        alert_placeholder.error(
            "Budget is required. Please enter a valid numeric budget value before starting analysis."
        )
    else:
        normalized_budget = budget_value.replace(",", "")
        try:
            budget = float(normalized_budget)
            if budget <= 0:
                alert_placeholder.error(
                    "Budget must be greater than 0. Please enter a valid numeric value."
                )
            else:
                alert_placeholder.empty()

                with st.spinner(
                    "Sustainlytics verileri işliyor ve en yeşil rotayı hesaplıyor..."
                ):
                    # Placeholder for Gemini + optimization pipeline.
                    time.sleep(1.8)
                    suppliers = [
                        {
                            "name": "EcoTrans Logistics",
                            "cost": 9200,
                            "sustainability_score": 84,
                            "carbon_kg": 120,
                        },
                        {
                            "name": "GreenPath Supply",
                            "cost": 8700,
                            "sustainability_score": 78,
                            "carbon_kg": 142,
                        },
                        {
                            "name": "TerraChain Partners",
                            "cost": 9900,
                            "sustainability_score": 91,
                            "carbon_kg": 109,
                        },
                    ]

                cheapest_name = min(suppliers, key=lambda item: item["cost"])["name"]
                greenest_name = max(
                    suppliers, key=lambda item: item["sustainability_score"]
                )["name"]

                st.success("Analysis completed. Top supplier candidates:")

                card_columns = st.columns(3)
                for col, supplier in zip(card_columns, suppliers):
                    badge_labels = []
                    if supplier["name"] == cheapest_name:
                        badge_labels.append("💰 Cüzdan Dostu")
                    if supplier["name"] == greenest_name:
                        badge_labels.append("🌱 Doğa Dostu")

                    with col:
                        tone_class = score_tone(supplier["sustainability_score"])
                        st.markdown(
                            f'<div class="supplier-card score-{tone_class}">',
                            unsafe_allow_html=True,
                        )
                        with st.container():
                            st.markdown(f"### {supplier['name']}")
                            if badge_labels:
                                st.markdown("  \n".join(badge_labels))
                            st.metric("Cost (USD)", f"${supplier['cost']:,}")
                            st.markdown(
                                (
                                    '<div class="score-label">'
                                    f"Sustainability: {supplier['sustainability_score']}/100"
                                    "</div>"
                                ),
                                unsafe_allow_html=True,
                            )
                            st.progress(supplier["sustainability_score"] / 100)
                            st.metric("Carbon (kg CO2e)", supplier["carbon_kg"])
                        st.markdown("</div>", unsafe_allow_html=True)
        except ValueError:
            alert_placeholder.error(
                "Invalid budget format. Please use only numbers (e.g. 10000 or 10,000)."
            )
