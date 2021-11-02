import csv
import pandas as pd
import numpy as np 


class LoanAssignments:

    def __init__(self,facilities,banks,covenants,loans):
        self.facilities = facilities
        self.banks = banks
        self.covenants = covenants
        self.loans = loans
    '''
    This function creates the data frame provided the paths of the csv files 
    '''
    def createDataFrame(self):
        self.df_facilities = pd.read_csv(self.facilities).rename(columns = {'id':'facility_id', 'amount':'facility_amount', 'interest_rate':'facility_interest_rate'})
        self.df_banks = pd.read_csv(self.banks)
        self.df_covenants = pd.read_csv(self.covenants)
        self.df_loans = pd.read_csv(self.loans).rename(columns = {'id':'loan_id', 'interest_rate':'loan_interest_rate'})
        self.FACILITY_DICT = {}
        for _, facility in self.df_facilities.iterrows():
            self.FACILITY_DICT[int(facility['facility_id'])] = int(facility['facility_amount'])

    def decideAssignments(self,LOANS,COVENANT,FACILITIES):
        
        mergedCovenants = pd.merge(COVENANT,FACILITIES, on='facility_id').sort_values(by=['facility_amount','facility_interest_rate'])
        # Creating Assignments Data frame to store the output data 
        assignmentsDataFrame = pd.DataFrame(columns=['loan_id','facility_id'])

        for _, loan in LOANS.iterrows():
            for _, covenant in mergedCovenants.iterrows():
                difference = self.FACILITY_DICT.get(covenant['facility_id']) - loan['amount']
                if (loan['default_likelihood'] < covenant['max_default_likelihood']) and (loan['state'] != covenant['banned_state']) and difference >= 0:
                    self.FACILITY_DICT[covenant['facility_id']] = difference
                    assignmentsDataFrame = assignmentsDataFrame.append({'loan_id': loan['loan_id'], 'facility_id':covenant['facility_id']}, ignore_index=True)
                    break
        return assignmentsDataFrame

    def getOutput(self):
        assignmentData = self.decideAssignments(self.df_loans,self.df_covenants,self.df_facilities)
        assignmentData.to_csv(path_or_buf = 'assignments.csv', index=False)
        

    '''
    Sample functions to check if the Dataframes are created or not 
    '''
    def printFacilities(self):
        print(self.df_facilities.to_string())
    
    def printBanks(self):
        print(self.df_banks.to_string())
    
    def printCovenants(self):
        print(self.df_covenants.to_string())
    
    def printLoans(self):
        print(self.df_loans.to_string())

    
def main():
    LA = LoanAssignments("large/facilities.csv","large/banks.csv","large/covenants.csv","large/loans.csv")
    LA.createDataFrame()
    LA.getOutput()
    
if __name__ == "__main__":
    main()