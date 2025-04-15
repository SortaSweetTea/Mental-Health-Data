# Mental Health Insights in the Gaming Community

This repository contains a data analysis project focused on mental health within the gaming community. The goal is to analyze how gaming habits and environments might affect mental well-being, drawing from various surveys, datasets, and other resources.

## Project Overview

With the increasing popularity of gaming, it’s important to understand its potential impact on mental health. This project explores trends, correlations, and insights from data about gamers’ mental health. By analyzing this data, we aim to identify key factors that contribute to mental wellness or challenges within the gaming community.

### Key Insights:
- Understanding the correlation between gaming time and mental health status.
- Identifying mental health trends across different gaming genres.
- Exploring the impact of online gaming communities on mental well-being.

## Folder Structure

```
mental-health-data/
├── data/
│   ├── raw/             # Raw, unprocessed data
│   ├── cleaned/         # Cleaned data, ready for analysis
│   └── external/        # External datasets or data sources
├── scripts/             # Python scripts for analysis and EDA using Spyder
├── visuals/             # Generated graphs, charts, and infographics
├── reports/             # Written reports, markdown files, or presentations
├── dashboard/           # Interactive dashboard files (if any)
├── LICENSE              # The project's open-source license
├── README.md            # Project documentation (this file)
└── requirements.txt     # List of dependencies for the project
```

## Getting Started

Follow the steps below to set up and run the project locally.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Spyder IDE or any Python IDE
- Git (for cloning the repository)

### Installation

1. **Clone the repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/mental-health-data.git
   cd mental-health-data
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   Install the necessary Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open Spyder**
   Launch Spyder and open any script from the `scripts/` folder to begin your analysis.

## Data Sources

The data used in this project comes from multiple sources:
- **Mental Health Survey Data**: Custom surveys created for this project.
- **External datasets**: Includes data sourced from platforms like Kaggle, WHO, and other research databases.

### Example Datasets:
- `mental_health_survey_raw.csv`: A raw dataset of survey responses regarding gaming habits and mental health.
- `WHO_mental_health_data_2023.csv`: A dataset from the World Health Organization providing global mental health statistics.

## Analyzing the Data

1. **Exploratory Data Analysis (EDA)**:  
   In `scripts/eda_mental_health.py`, we explore the data with basic statistics and visualizations to understand trends and identify key patterns.

2. **Data Cleaning**:  
   Data preprocessing steps, including handling missing values and transforming data, can be included in scripts like `scripts/data_cleaning.py`.

3. **Modeling**:  
   For predictive analysis (if applicable), models can be created and tested in `scripts/modeling.py`.

## Visualizations

Visuals and charts are generated throughout the analysis and saved in the `visuals/` folder.

Some example outputs include:
- **Mental Health vs. Gaming Time**: A graph showing the relationship between hours spent gaming and reported mental health status.
- **Mental Health Trends**: Line plots and bar charts showing mental health trends in different gaming genres or across time.

## Reports

In the `reports/` folder, you can find:
- **Final Report**: A summary of all findings from the project.
- **Presentation**: A slide deck that summarizes the key insights for potential presentations or interviews.

## Dashboard (Optional)

If applicable, an interactive dashboard can be found in the `dashboard/` folder. This allows users to explore the data interactively using tools like Streamlit, Dash, or Tableau.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## How to Contribute

If you'd like to contribute to this project, feel free to fork the repository, make improvements, and submit pull requests. Here’s a general guide on how to contribute:
1. Fork the repository
2. Create a new branch for your changes
3. Make your modifications
4. Push your changes and create a pull request

## Contact

For questions or feedback, feel free to reach out to me at:  
**Email**: tbaker4@albany.edu  
**GitHub**: [SortaSweetTea](https://github.com/SortaSweetTea)
