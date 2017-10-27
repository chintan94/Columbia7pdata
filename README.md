# 7pdata-corr
This is a private repository for 7park Correlation project

## The Entity-Ticker Mapper
### Input: tsv files
### Output: enriched file with entities mapped
### Storage elements
TTFD: Total Token Frequency Dictionary

TTM: Token -> Ticker Map 

### Basic Idea:
**Start**: 
    
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
    
**End**: 

### Suggestion from Joel:
We need 10 more tickers more than the the ones which are already mapped. 
