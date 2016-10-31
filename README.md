{\rtf1\ansi\ansicpg936\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;\f2\froman\fcharset0 TimesNewRomanPSMT;
}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 iqa_eval is a tool for evaluating interactive question answering, given the results file from Mechanical Turk. \
\
Usage: python eval.py input.csv time eval_row\
Assume that you cloned iqa_eval and now are in the directory that contains this README, to run the example input file would be something like: \
python eval.py \'93
\f1\fs22 \CocoaLigature0 Batch_2565336_batch_results.csv\'94 60 53 
\f0\fs24 \CocoaLigature1 \
\
input.cv: this is the directory of a cvs file returned by Mechanical Turk. An example of input file is Batch_2565336_batch_results.csv, in the input file, the 17th row is \'93Approved\'94 or \'93Rejected\'94, which is obtained in the process of managing the results from the workers on Mechanical Turk. Only the \'93Approved\'94 result will be considered. The evaluation result from each worker is 6 strings with numbers separated by \'93|\'94. The first string is the binary evaluation for each answer to the corresponding question, such as \'9301011\'94 if there are 5 questions involved in the conversation. The rest of the 5 strings are the scores from 1 to 5 to fill in the questionnaire questions.\
\
time: this is the total elapsed time for conducting all the tasks, which is measured in minutes.\
\
eval_row: this is the number of row that contains the evaluation result from the worker on Mechanical Turk.\
\
The output of the program including accuracy of the question answering success measuring with 5 metrics respectively and the following metrics:\
Total number of user/system turns\
Total number of system turns\
Average number of user/system turns per task \
Total elapse time\
Average elapsed time per task\
Get all the wanted information\
Clarity\
Naturalness\
Willingness to use system again\
User satisfactory\
\
The definition for each of the 5 metrics is as the following:\
\pard\pardeftab720\ri380\sl480\slmult1

\f2 \cf0 Metric1 is the majority vote, which means the final evaluation is determined by the results with more than 2 workers\'92 agreement. Metric2 assesses the evaluation would be \'931\'94 only when there are more than 3 workers believe that the answer is correct. Metric3 judged the final assessment would be \'931\'94 only when all the workers believe the answer is correct, otherwise the final evaluation would be \'930\'94. Metric4 gives more confidence on the workers who think the answer is correct, which gives \'931\'94 when more than 1 worker judge the answer is correct. Metric5 set the result to be \'931\'94 as long as there is some worker believe the answer is correct.\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0 \cf0 \
}