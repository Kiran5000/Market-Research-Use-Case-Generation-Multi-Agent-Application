import streamlit as st
from crew import ask
from fpdf import FPDF

# PDF generation function
def save_to_pdf(content, filename="Company_Research_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in content:
        try:
            # Handle any Unicode characters that might cause issues
            line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, line)
        except Exception as e:
            print(f"Error encoding line: {e}")
    
    pdf.output(filename)

# Streamlit app
def main():
    # Set up the main title and introduction
    st.title("🌐 AI-Powered Insight Wizard 🌐")
    st.subheader("Your Ultimate Assistant for Industry Research & Innovation")
    st.markdown(
        """
        Welcome to the **AI Insight Wizard**, where cutting-edge technology meets your business needs. 
        Generate in-depth industry insights, discover transformative AI use cases, and compile tailored resources 
        for seamless innovation. Transform your ideas into actionable strategies in just a few clicks! 🚀
        """
    )

    # Input section with clearer label and a styled text input
    st.markdown("### 🔍 Let's Begin with Your Query:")
    question = st.text_input(
        "Enter a Company or Industry Name", 
        placeholder="e.g., Fintech, Renewable Energy, SpaceX"
    )

    # Placeholder for storing results in session state
    if 'response' not in st.session_state:
        st.session_state.response = []

    # Submit button with response handling and result display
    if st.button("🎉 Generate Insights", key="generate_insights"):
        # Call the ask function and display the result
        response = ask(question)
        st.session_state.response = [
            f"**Industry Research Report**:\n{response.tasks_output[0].raw}",
            f"**AI Use Cases**:\n{response.tasks_output[1].raw}",
            f"**Resource Collection**:\n{response.tasks_output[2].raw}"
        ]

        # Display results with styled output
        for i, section in enumerate(["Industry Research Report", "AI Use Cases", "Resource Collection"]):
            st.markdown(f"### 🔬 {section}")
            st.write(st.session_state.response[i])

    # PDF Generation section
    st.markdown("---")
    st.markdown("### 📄 Export Your Insights")
    st.write(
        "Download your comprehensive AI-generated report as a beautifully formatted PDF. Perfect for sharing or offline review!"
    )

    # Save to PDF button
    if st.button("🔗 Save as PDF", key="save_pdf") and 'response' in st.session_state:
        save_to_pdf(st.session_state.response)
        st.session_state.pdf_saved = True
        st.success("📧 Report saved as PDF successfully!")

    # Dynamically generate the key for the download button
    download_button_key = "download_pdf_" + str(st.session_state.get('response', None))

    # Download PDF button (unique key)
    if st.session_state.get('pdf_saved', False):
        if st.button("💾 Download PDF", key=download_button_key):
            with open("Company_Research_Report.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
                st.download_button(
                    label="📚 Download PDF Report",
                    data=pdf_data,
                    file_name="Company_Research_Report.pdf",
                    mime="application/pdf"
                )

# Run the app
if __name__ == "__main__":
    main()
