/* Question 1 */
SELECT *
FROM information_schema.COLUMNS
WHERE
   TABLE_NAME = 'naep';

/* Question 2 */
SELECT *
FROM naep
LIMIT 50;

/* Question 3 */
SELECT naep.state AS states, COUNT(avg_math_4_score), AVG(avg_math_4_score), MIN(avg_math_4_score), MAX(avg_math_4_score)
FROM naep 
GROUP BY state 
ORDER BY state ASC;

/*Question 4*/
SELECT
   state,
   MIN (avg_math_4_score)
FROM
   naep
GROUP BY
   state
HAVING MIN(avg_math_4_score) > 30; 
/* */
SELECT
   state,
   MAX (avg_math_4_score)
FROM
   naep
GROUP BY
   state
HAVING MAX(avg_math_4_score) > 30;

/* Question 5*/
SELECT state AS bottom_10_states 
FROM naep 
WHERE year = '2000' 
ORDER BY avg_math_4_score 
LIMIT 10;

/*Question 6*/
SELECT round(AVG(avg_math_4_score), 2)
FROM naep
WHERE year = '2000';

/*Question 7*/
WITH AVR_ST AS
    (SELECT avg(avg_math_4_score) as AVG_STATES
    FROM naep
    WHERE year = '2000'
    GROUP BY state)
SELECT avg_math_4_score AS below_average_states_y2000, state
FROM naep, AVR_ST
WHERE avg_math_4_score < AVG_STATES;

/* Question8*/
SELECT state as  scores_missing_y2000
FROM naep
WHERE year = '2000' AND avg_math_4_score IS NULL;

/*Question 9*/
SELECT naep.state, ROUND(naep.avg_math_4_score, 2) as avg_math_4_score, finance.total_expenditure
FROM naep
LEFT OUTER JOIN finance ON naep.id = finance.id
WHERE naep.year = '2000' AND avg_math_4_score IS NOT NULL
ORDER BY finance.total_expenditure DESC;




