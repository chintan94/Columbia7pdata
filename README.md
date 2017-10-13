# 7pdata-corr
This is a private repository for 7park Correlation project

## The Entity-Ticker Mapper
### Input: tsv files
### Output: enriched file with entities mapped

### Basic Idea:

**Start**: Ignore all the entries which already have the ticker and cleansed_name set. 

### First Time Creation:

    1. Pick up the transaction description field. Strip out the state and city part.
    2. Run a word frequency algo on that. (A little complicated logic) 
    3. Define a threshold frequency. (If is crosses the threshold than consider for mapping)
       Maintain a central frequency counter persistant database. (word : count)
    4. For all those who cross the threshold -> define ticker and cleansed_name (Hardcoding) 
       Create a rule. Maintain a rule-system. 

### Automated Processing: 
    1. Strip the State and city.
    2. Check the rule book for all the substrings. 
    3. If the rule is found:
        Update the ticker and cleansed_name
    4. Updae the frequency counter. 

**End**: Write all the entries with mapped entity to output file. 

### Suggestion to Joel:
This is maintained by 7park. Why not filter out City and States and maintain them seperately? 

### Suggestion from Joel:
What should be the threshold? 
