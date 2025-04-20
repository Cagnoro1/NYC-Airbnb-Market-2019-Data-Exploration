# NYC Airbnb Market 2019 Data Exploration

![Airbnb-NYC- image](https://github.com/user-attachments/assets/66dcab0c-bf43-4c2c-a5c1-5335f22aad3f)

## Table of contents
- [Project Description ](#project-description) 
- [Data Source](#data-sources)
- [Dataset](#dataset)
- [Tools Used ](#tools-used)
- [Analysis Steps](#analysis-steps)
- [Key Findings](#key-findings)
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

# Conclusion
This exploratory analysis of NYC Airbnb listings in 2019 revealed critical patterns in pricing, distribution, and host behavior across the city’s boroughs. Key takeaways include:

## 1. Market Dynamics
**- Manhattan dominates** the Airbnb market, with 44% of listings and the highest average prices (peaking at $249 for entire homes).

**-Brooklyn** emerges as a competitive alternative, offering 41% of listings at relatively lower prices, particularly for shared rooms ($51 on average).

**- Staten Island** and the **Bronx** represent niche markets with fewer listings but notable affordability (e.g., Bronx private rooms average $67).

## 2. Pricing Strategies
**-Room type significantly impacts price:** Entire homes command premiums (230% higher than shared rooms in Manhattan), while shared rooms appeal to budget travelers.

**-Geographic pricing tiers** suggest opportunities for hosts to adjust rates based on neighborhood demand and competition.

## 3. Host and Guest Behavior
**-High availability** (>200 days/year for many listings) indicates potential oversupply in certain areas.

**-Review patterns** correlate with location and room type, with Manhattan and entire homes receiving more engagement—a proxy for guest satisfaction.

## 4. Business Implications
**-For hosts:** Optimize pricing by room type and borough; Brooklyn hosts might leverage affordability to attract longer stays.

**-For travelers:** Bronx and Queens offer value without sacrificing proximity to Manhattan attractions.

**-For policymakers:** Data highlights neighborhood-level tourism pressures, useful for regulatory balancing (e.g., short-term rental laws).

# Future Directions
To deepen insights, this analysis could expand to:

**-Multi-year trends** to post-pandemic recovery.

**-Machine learning models** to predict optimal pricing.

**-Integration with external data** (e.g., transit access, local events).

# Final Thoughts
This project demonstrates how data-driven approaches can decode complex market behaviors, offering actionable insights for stakeholders. The full code and visualizations are available for further exploration or extension.



  
  
