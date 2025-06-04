import streamlit as st

st.markdown("<h2>📊 Weekly Job Forecast Calculator</h2>", unsafe_allow_html=True)

st.markdown("""
This tool helps forecast how many **new jobs** you need this week based on last week's performance and current capacity.
""")

# --- Inputs ---
with st.form("forecast_form"):
    last_week_total = st.number_input("📆 Jobs Booked Last Week", min_value=0)
    completion_rate = st.number_input("✅ Completion Rate (%)", min_value=0.0, max_value=100.0, step=0.1)
    this_week_capacity = st.number_input("📈 Capacity This Week", min_value=0)
    jobs_booked_so_far = st.number_input("🟡 Jobs Already Booked This Week (optional)", min_value=0, value=0)

    submitted = st.form_submit_button("🔍 Calculate")

# --- Calculation ---
if submitted:
    completed_jobs = (completion_rate / 100) * last_week_total
    recycled_jobs = last_week_total - completed_jobs
    jobs_required = this_week_capacity - recycled_jobs
    final_jobs_required = jobs_required - jobs_booked_so_far

    # Display results
    st.markdown("### 📊 Forecast Results")

    # Highlighted big result
    st.markdown(
        f"<h4> Jobs Required This Week: {max(int(final_jobs_required), 0)}</h4>",
        unsafe_allow_html=True
    )
	
    # Supporting breakdown
    st.markdown("---")
    st.markdown(f"✅ Completed Jobs Last Week: **{int(completed_jobs)}**")
    st.markdown(f"🔄 Recycled Jobs This Week: **{int(recycled_jobs)}**")

    if jobs_booked_so_far > 0:
        st.markdown(f"🟡 Jobs Already Booked: **{int(jobs_booked_so_far)}**")

    if final_jobs_required <= 0:
        st.success("🎉 You're already at or over target capacity!")
