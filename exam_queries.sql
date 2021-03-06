-- Write a query that allows you to inspect the schema of the naep table.

SELECT *
FROM naep;

-- Write a query that returns the first 50 records of the naep table.

SELECT *
FROM naep
LIMIT 50;

/* Write a query that returns summary statistics 
for avg_math_4_score by state. 
Make sure to sort the results alphabetically by state name. */

SELECT naep.state AS states, COUNT(avg_math_4_score), AVG(avg_math_4_score), MIN(avg_math_4_score), MAX(avg_math_4_score)
FROM naep 
GROUP BY states 
ORDER BY states ASC;

/*Write a query that alters the previous query so that it 
returns only the summary statistics for avg_math_4_score by state 
with differences in max and min values that are greater than 30.*/

SELECT naep.state AS states, MIN(avg_math_4_score)- MAX(avg_math_4_score) >30 
FROM naep
GROUP BY states 
ORDER BY states ASC;

/* Write a query that returns a field called bottom_10_states 
that lists the states in the bottom 10 for avg_math_4_score 
in the year 2000.*/

SELECT *
FROM naep
GROUP BY naep.state AS states
ORDER BY avg_math_4_score DESC
LIMIT 10;

/*  Write a query that calculates the average avg_math_4_score 
rounded to the nearest 2 decimal places over all states in the 
year 2000.*/

SELECT naep.state AS states
    ROUND( AVG( amount ), 2 ) avg_math_4_score
FROM
    naep
INNER JOIN avg_math_4_score
        USING(states)
GROUP BY
    avg_math_4_score
ORDER BY
    naep.year.2000 DESC;

/*  Write a query that returns a field called 
below_average_states_y2000 that lists all states with 
an avg_math_4_score less than the average 
over all states in the year 2000. */

SELECT naep.state AS states, AVG(avg_math_4_score)
FROM naep
WHERE AVG(avg_math_4_scores) as below_average_states_y2000
INNER JOIN avg_math_4_score
        USING(states)
GROUP BY
    avg_math_4_score
ORDER BY
    naep.year.2000 DESC;
	
/*Write a query that returns a field called scores_missing_y2000 
that lists any states with missing values in the avg_math_4_score
column of the naep data table for the year 2000.*/

SELECT  naep *
FROM    naep.year.2000 
LEFT JOIN
        avg_math_4_score
ON      naep.state AS states
WHERE   avg_math_4_score IS NULL;

Write a query that returns for the year 2000 the state, 
avg_math_4_score, and total_expenditure from the naep 
table left outer joined with the finance table, 
using id as the key and ordered by total_expenditure 
greatest to least. Be sure to round avg_math_4_score to 
the nearest 2 decimal places, and then filter out 
NULL avg_math_4_scores in order to see any correlation 
more clearly.


