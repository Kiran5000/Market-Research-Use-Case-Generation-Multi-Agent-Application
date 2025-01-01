# Market Research & Use Case Generation Multi Agent Application

## Overview
The Market Research & Use Case Generation Multi AgentApplicaiton is an AI-powered platform designed to revolutionize industry research and innovation. By leveraging state-of-the-art generative AI and machine learning technologies, this application provides actionable insights, innovative AI use cases, and tailored resources to businesses aiming to gain a competitive edge. The system integrates seamlessly into existing workflows, offering decision-makers unparalleled efficiency and scalability in strategic planning.

## Key Features
1. **Comprehensive Industry Analysis:**
   - Conduct in-depth market research, analyzing trends, competitors, and strategic opportunities for specific companies or industries.

2. **AI Use Case Ideation:**
   - Identify cutting-edge applications of AI/ML tailored to a company's domain, emphasizing innovation, efficiency, and potential ROI.

3. **Resource Compilation:**
   - Curate high-quality datasets, libraries, and tools essential for implementing proposed AI use cases.

4. **Dynamic Report Generation:**
   - Generate professional, ready-to-share PDF reports summarizing research findings, use cases, and resources.

5. **User-Friendly Interface:**
   - Utilize an intuitive Streamlit-based interface for streamlined input and real-time output display.

## High-Level System Architecture

**1. Frontend Layer:**
   - **Streamlit Application**
     - Allows users to input queries and receive insights dynamically.
     - Supports exporting insights as PDF reports.

**2. Backend Layer:**
   - **CrewAI Agents:**
     - **Industry Researcher Agent:** Conducts industry analysis.
     - **AI Use Case Strategist:** Generates tailored AI use cases.
     - **Resource Collector:** Identifies and curates implementation resources.
   - **CrewAI Workflow:** Coordinates task execution across agents using a sequential process.

**3. Tools & Utilities Layer:**
   - **Search Tool:** Performs online searches for relevant data.
   - **Scrape Tool:** Extracts structured information from websites.
   - **PDF Tool:** Searches and extracts information from PDF documents.

**4. AI Layer:**
   - **Language Models:** Powered by `openai/Qwen2.5-72B-Instruct-Turbo` and Google's Gemini for embedding and retrieval tasks.

**5. Data Management Layer:**
   - Environment variable management using `.env` file for secure API key handling.

## Technology Stack
- **Programming Languages:** Python
- **Frameworks & Libraries:**
  - `crewai`
  - `crewai_tools`
  - `langchain_community`
  - `langchain-together`
  - `langchain-google-genai`
  - `streamlit`
  - `fpdf`
  - `python-dotenv`
- **APIs and Tools:**
  - Together API for LLM integration.
  - SerperDevTool and ScrapeWebsiteTool for web search and scraping.
  - Google AI for embedding and document retrieval.
- **Environment Management:** `python-dotenv` for managing API keys and configurations.

## Installation

### Prerequisites
- Python 3.8 or higher.
- A virtual environment (recommended).
- API keys for Together, Google, and SerperDevTool (to be set in the `.env` file).

### Steps
1. **Clone the Repository:**
   ```bash
   git clone "https://github.com/Kiran5000/Market-Research-Use-Case-Generation-Multi-Agent-Application.git"
   cd Market-Research-Use-Case-Generation-Multi-Agent-Application

   ```

2. **Set Up Virtual Environment:**
   ```bash
   python3 -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```env
     GOOGLE_API_KEY="<your_google_api_key>"
     SERPER_API_KEY="<your_serper_api_key>"
     TOGETHER_API_KEY="<your_together_api_key>"
     ```

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

6. **Access the Application:**
   - Open your web browser and navigate to `http://localhost:8501`.

The system is now ready to generate insights, AI use cases, and resource recommendations for your chosen industry or company!

