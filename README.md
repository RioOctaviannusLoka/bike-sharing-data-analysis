<h1 align="center">Bike Sharing Rentals Data Analysis and Dashboard</h1>

# Table of Contents

- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Project Structure](#project-structure)
- [Project Goals](#project-goals)
- [Key Insights](#key-insights)
- [Tech Stack](#tech-stack)
- [Installation](#installation)

# Project Overview

The **Bike Sharing Rentals Data Analysis and Dashboard** project focuses on uncovering insights from a public bike-sharing dataset collected over two years (2011–2012). The dataset captures various factors such as seasonality, weather conditions, and user behavior that influence bike rental demand in an urban setting.

The main objectives of this project are:
- To explore and understand the patterns and trends in bike rental usage.
- To analyze how environmental and temporal variables affect rental counts.
- To develop an interactive dashboard that helps visualize and communicate these insights effectively.

This project is a great example of applying data analytics and visualization techniques to real-world data for better decision-making and urban mobility planning.

Please visit this link to view the deployed version: [streamlit dashboard](https://bike-sharing-data-analysis-dashboard.streamlit.app)

# Data Source

Data used in this project is taken from [Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

# Project Structure

```
├── dashboard/
    ├── dashboard.py                          # dashboard code
    ├── cleaned_day.csv                       # cleaned dataset
├── data/                                     # original dataset
├── Proyek_Analisis_Data_Bike_Sharing.ipynb   # notebook for data analysis
├── README.md                                 # documentation for this project
├── requirements.txt                          # dependencies used in the project
```

#  Project Goals

1. Perform **exploratory data analysis (EDA)** to understand rental trends.
2. Discover how external factors such as weather and season influence the number of rentals.
3. Create an **interactive dashboard** to visualize the insights.

#  Key Insights

Some of the key findings from the analysis:

- Rental counts significantly increase during the summer season.
- Registered users are more active on working days.
- High humidity and poor weather conditions reduce the number of rentals.
- Yearly trends show user growth from 2011 to 2012.

# Tech Stack

<a href="https://www.python.org/"><img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python Icon" title="Python" width="65" height="65" /></a>
<a href="https://jupyter.org/"><img src="https://go-skill-icons.vercel.app/api/icons?i=jupyter" alt="Jupyter Notebook Icon" title="Jupyter Notebook" width="65" height="65" /></a>
<a href="https://pandas.pydata.org/"><img src="https://go-skill-icons.vercel.app/api/icons?i=pandas" alt="Pandas Icon" title="Pandas" width="65" height="65" /></a>
<a href="https://matplotlib.org/"><img src="https://go-skill-icons.vercel.app/api/icons?i=matplotlib" alt="Matplotlib" title="Matplotlib" width="65" height="65"/></a>
<a href="http://seaborn.pydata.org/"><img src="https://go-skill-icons.vercel.app/api/icons?i=seaborn" alt="Seaborn" title="Seaborn" width="65" height="65"/></a>
<a href="https://streamlit.io/"><img src="https://go-skill-icons.vercel.app/api/icons?i=streamlit" alt="Streamlit" title="Streamlit" width="65" height="65"/></a>
<a href="https://code.visualstudio.com/"><img src="https://go-skill-icons.vercel.app/api/icons?i=vscode" alt="Visual Studio Code" title="Visual Studio Code" width="65" height="65"/></a>

# Installation

1. Clone this repository

   ```bash
   git clone https://github.com/RioOctaviannusLoka/bike-sharing-data-analysis.git
   ```

2. Create Python Virtual Environment
   
   • For Anaconda:
   ```bash
   conda create --name main-ds python=3.9
   ```

   • For Shell/Terminal:
   ```bash
   cd proyek_akhir
   pipenv install
   ```

3. Activate the Environment

   • For Anaconda:
   ```bash
   conda activate main-ds
   ```

   • For Shell/Terminal:
   ```bash
   pipenv shell
   ```

4. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

5. Run the streamlit dashboard

   ```bash
   streamlit run dashboard\dashboard.py
   ```

6. Stop the streamlit dashboard press `ctrl + c`

---

Copyright &copy; 2025 - Rio Octaviannus Loka