from src.parent_strategy import ParentStrategy

'''
import the parent class ParentStrategy - need weight and probability methods
'''

class CollectiveImpurityGini(ParentStrategy):

    def calculate(self, partition):

        '''
        calculate is very similar to that of the entropy calculate method

        total_gini is initialized at 0.0 prior to the running total in the latter for loop

        for loop to access each susbet in our partition

        '''

        total_records = sum(len(group) for group in partition) # total number of numbers - len of elements in each group
        total_gini = 0.0

        for group in partition:
            '''
            calculate the probability of "High Risk", "Low Risk" labels for the subset partitions

            calculate gini score with provided formula

            total gini for this partition includes the weight of each group in relevance to its partition 
            '''
            if group: # if group (subset) exists in our partition, compute the following
               
                p_high = self.probability(group, "High Risk")
                p_low = self.probability(group, "Low Risk")

                gini = 1 - (p_high ** 2 + p_low ** 2) # gini formula
                weight = len(group) / total_records 
                total_gini += weight * gini 

            return total_gini