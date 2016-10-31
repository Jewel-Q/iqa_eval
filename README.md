iqa_eval is a tool for evaluating interactive question answering, given the results file from Mechanical Turk. 

Usage: python eval.py input.csv time eval_row
Assume that you cloned iqa_eval and now are in the directory that contains this README, to run the example input file would be something like: 
python eval.py “Batch_2565336_batch_results.csv” 60 53 

input.cv: this is the directory of a cvs file returned by Mechanical Turk. An example of input file is Batch_2565336_batch_results.csv, in the input file, the 17th row is “Approved” or “Rejected”, which is obtained in the process of managing the results from the workers on Mechanical Turk. Only the “Approved” result will be considered. The evaluation result from each worker is 6 strings with numbers separated by “|”. The first string is the binary evaluation for each answer to the corresponding question, such as “01011” if there are 5 questions involved in the conversation. The rest of the 5 strings are the scores from 1 to 5 to fill in the questionnaire questions.

time: this is the total elapsed time for conducting all the tasks, which is measured in minutes.

eval_row: this is the number of row that contains the evaluation result from the worker on Mechanical Turk.

The output of the program including accuracy of the question answering success measuring with 5 metrics respectively and the following metrics:
Total number of user/system turns
Total number of system turns
Average number of user/system turns per task 
Total elapse time
Average elapsed time per task
Get all the wanted information
Clarity
Naturalness
Willingness to use system again
User satisfactory

The definition for each of the 5 metrics is as the following:
Metric1 is the majority vote, which means the final evaluation is determined by the results with more than 2 workers’ agreement. Metric2 assesses the evaluation would be “1” only when there are more than 3 workers believe that the answer is correct. Metric3 judged the final assessment would be “1” only when all the workers believe the answer is correct, otherwise the final evaluation would be “0”. Metric4 gives more confidence on the workers who think the answer is correct, which gives “1” when more than 1 worker judge the answer is correct. Metric5 set the result to be “1” as long as there is some worker believe the answer is correct.


