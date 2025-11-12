## Unique Question Sampler - Documentation

### Purpose
Select unique questions from each database based on difficulty and save as a CSV.

### Main Steps

1. **Define Sampling Sizes**
   - Simple: 15 questions
   - Moderate: 7 questions
   - Challenging: 3 questions

2. **Loop Through Databases**
   - For each `db_id`, filter data for that database.

3. **Loop Through Difficulty Levels**
   - For each difficulty, sample the required number of unique questions.
   - Ensure no duplicates and do not exceed available questions.

4. **Aggregate Sampled Questions**
   - Concatenate sampled questions from all databases and difficulties into a single DataFrame.

5. **Reset Index**
   - Clean up the DataFrame index for better readability.

6. **Save to CSV**
   - Save the resulting DataFrame to `sampled_questions_unique.csv`.


