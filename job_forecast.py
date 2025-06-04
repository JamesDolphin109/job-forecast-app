import streamlit as st

st.title("Weekly Job Forecast Tool")

# Inputs
last_week_jobs = st.number_input("Jobs Booked Last Week", min_value=0, step=1)
completion_percent = st.number_input("Completion % (e.g. 63 for 63%)", min_value=0.0, max_value=100.0, step=0.1)
this_week_capacity = st.number_input("This Week's Job Capacity", min_value=0, step=1)

# Calculation
if last_week_jobs and completion_percent and this_week_capacity:
    completion_rate = completion_percent / 100
    completed_jobs = last_week_jobs * completion_rate
    recycled_jobs = last_week_jobs - completed_jobs
    jobs_required = this_week_capacity - recycled_jobs

    # Outputs
    st.subheader("Forecast Results")
    st.write(f"✅ **Completed Jobs Last Week:** {int(completed_jobs)}")
    st.write(f"🔄 **Recycled Jobs This Week:** {int(recycled_jobs)}")
    st.markdown(f"""
###  Jobs Required This Week:  {int(jobs_required)}
""")

    if jobs_required < 0:
        st.warning("⚠️ You are over capacity! Consider reducing incoming jobs.")
    elif jobs_required == 0:
        st.info("You are exactly at capacity.")
    else:
        st.success("You are within capacity limits.")