# Election_Analysis

## Election Audit Overview
The Colorado Board of Elections engaged us to complete an election audit of a recent local congressional election, specifically requesting that software be written and executed to complete the following tasks:
1.	Calculate the total number of votes cast.
2.	Generate a complete list of candidates who received votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won. 
5.	Determine the winner of the election based on popular vote.
#### Addendum
In an addendum, the following additional request was made:
	-  
	-  
 6.	Determine the county with the largest voter turnout.
#### Resources
The following resources were used to complete the requested work:
- Data Source: election_results.csv provided by client
- Software: Python 3.7.6, Visual Studio Code 1.56.0
## Election-Audit Results
	(Use a bulleted list.) (Insert images or examples of my code as support where necessary.)
- **A total of 369,711 votes were cast in the election.**
	- To determine this, a variable was initialized as show below:
	-  
![Image of total vote variable initialization](images/total_vote_initialization_Screenshot_2021-05-14_165416.png)
	-  
	- Next, a for loop was constructed as follows (Note that the header row was stripped off before processing the remaining rows):
	-  
![Image of total vote for loop](images/total_vote_for_loop_Screenshot_2021-05-14_165838.png)
	-  
	- Then the results were output to the terminal and a text file:
	-  
![Image of total vote output logic](images/total_vote_output_to_terminal_and_file_Screenshot_2021-05-14_170127.png)
	-   
- **The specifics for each county were as follows:**
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
	- Denver had the largest county turnout.
	- In order to obtain this,  a list and a dictionary were intialized
	-  
![Image of county list and dictionary intializations](images/largest_county_turnout_initialization_Screenshot_2021-05-14_173705.png)
	-  
	-
	- Then, the county analysis was preformed and the output was sent both to the terminal and the text file.
	-   
![Iamge of county for loop and output logic](images/county_for_loop_and_output_Screenshot_2021-05-14_173945.png)
	-  
	-  
- **The specifics for each candidate were as follows:**
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
	- The logic for the candidate calculations is as follows:
	- 
![Image of candidate calculation](images/candidate_calculation_for_loop_Screenshot_2021-05-14_175004.png)
	-
- **Here are the details for the winning candidate:**
	- Winner: Diana DeGette
	- Winning Vote Count: 272,892
	- Winning Percentage: 73.8%
	- Here is an image of variable initialization for the winning candidate:
	-  

![Image of winning candidate variable initialization](images/winning_candidate_initialization_Screenshot_2021-05-14_174626.png)
	-  
	- ...and here is an image of the winning candidate calculation:
	-  
![Image of winning candidate output logic](images/'winning_candidate_output_Screenshot 2021-05-14 175407.png')
	-  
- **Here is an image of the terminal output:**
-   

![Screenshot of Terminal Output](images/Terminal_Output_Screenshot_2021-05-14_164717.png)
-  
- **Here is an image of the output file contents:**
-   

![Screenshot of Text File Output](images/Text_File_Output_Screenshot_2021-05-14_164525.png)
-  
## Election-Audit Summary (Further Work)
The requirements of the Colorado Board of Elections for this project were implemented in the simplest manner possible. These requirements could be expanded upon in various ways including the following:
1. **Candidate Performance by County**
	- Using the provided CSV file “as-is”, a new code implementation could break out the performance of each candidate in each county possibly in a “nested for loop.”
2. **Independent Formatting of Terminal and File Output**
	- Using the provided CSV file “as-is”, a new code implementation could format the output to the terminal and the output to the file independently possibly by implementing separate for loops for each and re-initializing shared variables between the loops.
3. **Party Affiliation**
	- It would be useful to see which political party each of the candidates is representing. While this could be achieved simplistically by including the candidate’s party affiliation in the same field with their name in the CSV file, a more sophisticated approach would be to create another field in the CSV file rows specifically for party affiliation. This in turn could be used in a new code implementation to calculate party performance at the county level, for instance.
4. **District Level Data**
	- A logical extension would be to collect and process data at the district level.  A new field would need to be added to the CSV file that indicates which district each county resides in. A new code implementation could then provide insight into candidate (and if implemented, party) performance at the district level. 

