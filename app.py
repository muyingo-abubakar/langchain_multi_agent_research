import streamlit as st
from src.pipeline.pipeline import research_pipeline
import time
from src.agents.agent import build_reader_agent, build_search_agent, writer_chain, critic_chain


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #13265C;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hero */
    .hero {
        padding: 35px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #151b2b,
            #111827
        );
        border: 1px solid #273249;
        margin-bottom: 30px;
    }

  .hero-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
    background: #0B1F3A;
    color: white;
    padding: 20px 30px;
    border-radius: 12px;
    text-align: center;
}

.hero-title span {
    color: #2196F3;
}

.hero-subtitle {
    text-align: center;
    font-size: 18px;
    color: #9ca3af;
    margin-top: 15px;
}

    .hero-subtitle {
        font-size: 18px;
        color: #9ca3af;
    }

    /* Agent cards */
    .agent-card {
        padding: 20px;
        border-radius: 16px;
        background: #151a24;
        border: 1px solid #252d3d;
        text-align: center;
        min-height: 150px;
    }

    .agent-icon {
        font-size: 35px;
    }

    .agent-title {
        font-weight: 700;
        font-size: 17px;
        margin-top: 8px;
    }

    .agent-status {
        color: #9ca3af;
        font-size: 13px;
        margin-top: 5px;
    }

    /* Active agent */
    .active-agent {
        border: 1px solid #6366f1;
        box-shadow: 0 0 20px rgba(99,102,241,0.2);
    }

    /* Result cards */
    .result-card {
        background: #151a24;
        border: 1px solid #252d3d;
        border-radius: 16px;
        padding: 25px;
        margin-top: 15px;
    }

    /* Metrics */
    .metric-card {
        background: #151a24;
        border: 1px solid #252d3d;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
    }

    .metric-number {
        font-size: 30px;
        font-weight: 800;
    }

    .metric-label {
        color: #9ca3af;
        font-size: 13px;
    }

    /* Divider */
    .divider {
        margin-top: 30px;
        margin-bottom: 30px;
        border-top: 1px solid #252d3d;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        padding: 30px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🧠 ResearchAI")

    st.markdown("""
    **Multi-Agent Research System**

    Your AI research team can:

    🔎 Search the web  
    📖 Read sources  
    ✍️ Write reports  
    🧐 Critique results
    """)

    st.divider()

    st.markdown("### ⚙️ Configuration")

    model = st.selectbox(
        "AI Model",
        [
            "GPT OSS 20B",
            "GPT OSS 120B"
        ]
    )

    st.markdown("### 🤖 Agents")

    st.success("🔎 Search Agent")
    st.success("📖 Reader Agent")
    st.success("✍️ Writer Agent")
    st.success("🧐 Critic Agent")

    st.divider()

    st.caption("ResearchAI • Multi-Agent Architecture")


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero-title">
    🧠 RESEARCHER <span>AI</span> AGENT
</div>

<div class="hero-subtitle">
    Your autonomous multi-agent research assistant.
    Search. Read. Write. Critique.
</div>
""", unsafe_allow_html=True)


# ============================================================
# INPUT
# ============================================================

st.markdown("### 🔬 What do you want to research?")

topic = st.text_input(
    "",
    placeholder="Example: How is AI transforming football scouting?",
    label_visibility="collapsed"
)


col1, col2 = st.columns([4, 1])

with col1:
    st.caption(
        "💡 Try: AI in football, Falcon LLM architecture, "
        "Agentic AI in healthcare..."
    )

with col2:

    start = st.button(
        "🚀 Start Research",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# RESEARCH
# ============================================================

if start:

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        st.markdown("---")

        # ----------------------------------------------------
        # AGENT WORKFLOW
        # ----------------------------------------------------

        st.markdown("### 🤖 Research Team")

        a1, a2, a3, a4 = st.columns(4)

        with a1:
            st.markdown("""
            <div class="agent-card active-agent">
                <div class="agent-icon">🔎</div>
                <div class="agent-title">Search Agent</div>
                <div class="agent-status">
                    Finding sources...
                </div>
            </div>
            """, unsafe_allow_html=True)

        with a2:
            st.markdown("""
            <div class="agent-card">
                <div class="agent-icon">📖</div>
                <div class="agent-title">Reader Agent</div>
                <div class="agent-status">
                    Waiting...
                </div>
            </div>
            """, unsafe_allow_html=True)

        with a3:
            st.markdown("""
            <div class="agent-card">
                <div class="agent-icon">✍️</div>
                <div class="agent-title">Writer Agent</div>
                <div class="agent-status">
                    Waiting...
                </div>
            </div>
            """, unsafe_allow_html=True)

        with a4:
            st.markdown("""
            <div class="agent-card">
                <div class="agent-icon">🧐</div>
                <div class="agent-title">Critic Agent</div>
                <div class="agent-status">
                    Waiting...
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("")

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info("🔎 Search Agent is searching for reliable sources...")
            progress.progress(10)

            time.sleep(0.5)

            # ------------------------------------------------
            # RUN PIPELINE
            # ------------------------------------------------

            result = research_pipeline(topic)

            progress.progress(100)

            status.success(
                "✅ Research completed successfully!"
            )

            # =================================================
            # METRICS
            # =================================================

            st.markdown("### 📊 Research Overview")

            m1, m2, m3, m4 = st.columns(4)

            with m1:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-number">4</div>
                    <div class="metric-label">
                        AI Agents
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with m2:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-number">1</div>
                    <div class="metric-label">
                        Research Topic
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with m3:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-number">✓</div>
                    <div class="metric-label">
                        Sources Analyzed
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with m4:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-number">AI</div>
                    <div class="metric-label">
                        Powered Research
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # =================================================
            # FINAL REPORT
            # =================================================

            st.markdown("---")

            st.markdown("## 📝 Research Report")

            st.markdown(
                f"""
                <div class="result-card">

                <h3>Research Topic</h3>

                <p>{topic}</p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("")

            st.write(result["report"])

            # =================================================
            # AGENT RESULTS
            # =================================================

            st.markdown("---")

            st.markdown("### 🔍 Research Process")

            with st.expander(
                "🔎 Search Agent — Sources discovered"
            ):

                st.write(
                    result["search_results"]
                )

            with st.expander(
                "📖 Reader Agent — Source analysis"
            ):

                st.write(
                    result["scraped_content"]
                )

            with st.expander(
                "🧐 Critic Agent — Report review"
            ):

                st.write(
                    result["feedback"]
                )

            # =================================================
            # DOWNLOAD
            # =================================================

            st.markdown("---")

            st.markdown("### 📥 Export")

            report_text = f"""
RESEARCH TOPIC
{topic}

==============================

FINAL REPORT

{result["report"]}

==============================

CRITIC FEEDBACK

{result["feedback"]}
"""

            st.download_button(
                label="📄 Download Research Report",
                data=report_text,
                file_name="research_report.txt",
                mime="text/plain"
            )

        except Exception as e:

            if "429" in str(e):

                st.error(
                    "⏳ Groq rate limit reached."
                )

                st.info(
                    "Your research pipeline is making several "
                    "LLM calls. Wait a few seconds and try again."
                )

            else:

                st.error(
                    f"❌ Research failed: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    🧠 ResearchAI<br>

    Multi-Agent Research • LangChain • LangGraph • Groq

</div>
""", unsafe_allow_html=True)
