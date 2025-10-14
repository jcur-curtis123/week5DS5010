class ParentStrategy:
    
    def probability(self, records, label):
        '''
        probability method - calculates the proportion of labels with records

        ie; how often does "High Risk" show up in all records?
        '''
        count = 0
        for i in records:
            '''
            define var i to access records param

            if the label in the record is our target label, increase this count
            '''
            if i.actual_label == label:
                count += 1
            
        probability = (count)/len(records) # probability var - count/number of records
        return probability
    

    def calculate_weights(self, partition):

        '''
        calculate_weights takes the partition (True, False groups for example)

        determines the weights according to the each partition records

        ie; true group consist of 6 records, 4 in false partition 

        weight for true group is 0.6 and false 0.4
        '''
        
        total = 0

        for i in partition:
            total = total + len(i)

        weights = []
        for i in partition:
            weight = len(i) / total
            weights.append(weight) # append the weight to the list once calculated

        return weights





