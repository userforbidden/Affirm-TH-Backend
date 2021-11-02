# Affirm-TH-Backend

## Write Up 
### 1. How long did you spend working on the problem? What did you find to be the most difficult part?
I spent around four hours to complete this problem. As I am new to fin tech, the most difficult part for me was understanding the data and finding a relation among the provided dataset. I took some time undertanding the data and how they were related. After this I took the approach of renaming the dataframes to have unique column names made it easier for me to work on further. I am excited to discuss this task more given an opportunity.
### 2. How would you modify your data model or code to account for an eventual introduction of new, as-of-yet unknown types of covenants, beyond just maximum default likelihood and state restrictions?
I will try to add a default value to the NaN values. Instead of a NaN. This avoids usage of cleaning code inside of the calculation functions. Apart from this I could not think of any improvements to the data model at this time. I will update the writeup, If I remember any improvements before our discussion 
### 3. How would you architect your solution as a production service wherein new facilities can be introduced at arbitrary points in time. Assume these facilities become available by the finance team emailing your team and describing the addition with a new set of CSVs.
The provided solution could easily be able to handle more facilties because the covenant data is merged with facilites data for analysis. Due to this merging if there exists a covenant for a facility it will be used for analysis before assigning a loan
### 4. Your solution most likely simulates the streaming process by directly calling a method in your code to process the loans inside of a for loop. What would a REST API look like for this same service? Stakeholders using the API will need, at a minimum, to be able to request a loan be assigned to a facility, and read the funding status of a loan, as well as query the capacities remaining in facilities.

### 5. How might you improve your assignment algorithm if you were permitted to assign loans in batch rather than streaming? We are not looking for code here, but pseudo code or description of a revised algorithm appreciated.

### 6. Discuss your solution’s runtime complexity.
I have used a nested loop to process the two dataFrames this gives a complexity of O(n^2). I am aware this is not a optimal solution in realtime. I need more time to look into optimizing this code to run faster than the current way it is programmed. 