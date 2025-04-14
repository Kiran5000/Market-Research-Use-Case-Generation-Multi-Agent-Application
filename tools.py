from crewai_tools import ScrapeWebsiteTool, SerperDevTool, PDFSearchTool
import streamlit as st
import os

os.environ['SERPER_API_KEY'] = st.secrets["SERPER_API_KEY"]
os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

pdf_tool = PDFSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(model="gemini-1.5-flash-002"),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    ),
    pdf='./report.pdf'
)
