# NYC Airbnb Market 2019 Data Exploration

![Airbnb-NYC- image](https://github.com/user-attachments/assets/66dcab0c-bf43-4c2c-a5c1-5335f22aad3f)

## Table of contents
- [Project Description ](#project-description) 
- [Data Source](#data-sources)
- [Tools Used ](#tools-used)
- [Data Cleaning ](#data-cleaning)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis)

## Project Description
This project explores the NYC Airbnb Market through data analysis, uncovering trends in pricing, availability, and neighborhood demand. Using Python (pandas, seaborn, matplotlib), the analysis follows a structured approach: 
1. Data Exploration and cleaning
2. Price patterns
3. Neighborhood trends
4. Host behavior

## Data Source
The data used for this analysis was collected from kaggle: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

## Dataset
The dataset contains 48,895 listings with 16 features including:
- Neighborhood information (borough and specific area)
- Room type (Entire home, Private room, Shared room)
- Pricing data
- Availability
- Review metrics
- Host information
  
The dataset was composed of: 
- **id :** listing ID
- **name :** name of the listing
- **host_id :** host ID
- **host_name :** name of the host
- **neighbourhood_group :** location
- **neighbourhood :** area
- **latitude :** latitude coordinates
- **longitude :** longitude coordinates
- **room_type :** listing space type
- **price :** price in dollars
- **minimum_nights :** amount of nights minimum
- **number_of_reviews :** number of reviews
- **last_review :** latest review date
- **reviews_per_month :** number of reviews per month
- **calculated_host_listings_count :** amount of listing per host
- **availability_365 :** number of days when listing is available for booking

  ## Tools Used
  - Python 3.x
  - Jupyter Notebook 
  - Required libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
 
  ## Analysis Steps

1. **Data Loading & Initial Exploration**
   - Imported necessary Python libraries (Pandas, NumPy, Matplotlib, Seaborn)
   - Examined dataset structure and basic statistics
   - Identified missing values and data types

2. **Data Cleaning**
   - Handled missing values (dropped rows with nulls)
   - Checked for duplicate entries
   - Verified data consistency

3. **Exploratory Data Analysis**
   - Analyzed price distributions and outliers
   - Explored neighborhood distributions
   - Examined room type prevalence
   - Investigated review patterns

4. **Visualizations**
   - Created geographic distribution maps
   - Generated comparative bar charts of pricing by neighborhood and room type
   - Produced scatter plots showing review/price relationships
   - Developed pair plots for multivariate analysis

## Key Findings

### Pricing Insights
- **Manhattan** has the highest average prices ($249 for entire homes, $117 for private rooms)
- **Bronx** offers the most affordable options ($128 for entire homes, $67 for private rooms)
- Shared rooms are most economical in **Brooklyn** (average $51)

### Market Distribution
- **Manhattan** dominates with 21,661 listings (44% of total)
- **Brooklyn** follows with 20,104 listings (41%)
- **Staten Island** has the fewest listings (373)

### Review Patterns
- Listings in **Manhattan** receive the most reviews on average
- Entire homes tend to have higher review counts than shared rooms

### Availability
- Many listings show high annual availability (>200 days)
- Some neighborhoods show seasonal patterns with lower availability


  
  
