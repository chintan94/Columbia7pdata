# 7pdata-corr
This is a private repository for 7park Correlation project

## The Entity-Ticker Mapper
### Input: tsv files
### Output: enriched tsv files with entities mapped
### Storage elements
TTFD: Total Token Frequency Dictionary

TTM: Token -> Ticker Map 

### Basic Idea:
**Start**
    
    0. Ignore all the entries which already have the ticker and cleansed_name set. 
    1. Clean the transaction description and tokenize with spacy.

### First Time Creation:
    2. Calculate the token frequency. Update TTFD.
    3. Take the top 10-15-20 until we get 10-15 organizations out of those.
    4. Manually Create TTM. 
    
### Automated Processing:  
    2. Check TTM for each token. And map accordingly. 
    3. If the rule is found:
        Update the ticker and cleansed_name
    4. Update the frequency counter. 

### Derivative Creation
    5. For each month create seperate derivative files for each mapped ticker.
    
**End**

Note: All the following modules are generic

## Clustering Framework

### Input: Any tsv file
### Output: Clusters (For correlations)

**Start**

### Generating the Dataframe for Clustering 

    1. Group the users based on the following:
        Sum the total spending
        Aggregate the location
        Gender
        Start date (optional) 
        End date (optional) 
    2. Prepare a tsv based on 1 and provide it for the next step. 

### Finding the right K for K-means

    3. Test for different Ks. Plot the cohesion within the cluster, seperability among the clusters.
    4. Fix a K.
    5. Define the clusters for all the time periods and output those.

## Correlation Framework

## Input: Clusters, Financial Record(FR) 
## Output: Correlation Coefficient(CC)

    1. Fix the FR. 
    2. Find the CC for all the clusters. 
    3. Look for patterns.
    
**End**

## Thinking To Do:
    1. K definition. 
    2. FRs we want to use. 
    
## Coding To Do: 
    1. Generating the dataframe clustering. 
    2. Debug the derivative generation part. 
