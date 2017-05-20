class Item(object):

    def __init__(self, index_number, width, weight):
        self.index_number = index_number
        self.width = width
        self.weight = weight

    def __add__(self, other):
        index_numbers = [];
        index_numbers.extend(self.index_number)
        index_numbers.extend(other.index_number)
        total_width = self.width + other.width
        total_weight = self.weight + other.weight
        return Item(index_numbers, total_width, total_weight)

    def __gt__(self, other):
        if self.width > other.width:
            return True
        
            return True            


def read_input():

    array_of_items = []
    while True:
        inp = raw_input()
        if inp == "":
            break
        attributes = [int(x) for x in inp.split()]
        array_of_items.append(Item([attributes[0]],   \
            attributes[1], attributes[2]))  
    return array_of_items    


def make_catalog(array_of_items):
    catalog = {}

    for i in array_of_items:
        catalog[str(i.index_number[0])] = i

    return catalog    

def set_as_best_combination(combination):
    highest_width = combination.width
    highest_weight = combination.weight
    most_number_of_items = len(combination.index_number)
    best_combination = combination

    return highest_width, highest_weight, most_number_of_items, best_combination 


def compare_ids_in_combinations(combination, best_combination):

    ids_in_new_combination = combination.index_number
    ids_in_old_combination = best_combination.index_number

    for i,j in zip(sorted(ids_in_new_combination), sorted(ids_in_old_combination)):
        if i < j:
            return combination
        elif i > j:
            return best_combination
        else:
            continue
    return combination                


def remove_best_combination(best_combination, array_of_items):
    items_to_remove = best_combination.index_number
    return [i for i in array_of_items if i.index_number[0] not in items_to_remove]

def find_best_combination(array_of_items):
    max_width = 1100
    max_weight = 1000
    highest_width = 0
    highest_weight = 0
    most_number_of_items = 0
    best_combination = 0
    #lowest_id = 99
    combinations = []

    for i in range(len(array_of_items)):
        combinations.append(array_of_items[i])

        for j in range(i+1, len(array_of_items)):
            new_combinations = []
            for k in combinations:
                total_width = k.width + array_of_items[j].width
                total_weight = k.weight + array_of_items[j].weight

                # if within limitations, then add combination and remove old one
                if (total_width <= max_width) and (total_weight <= max_weight):
                    new_combinations.append(k + array_of_items[j])

            combinations.extend(new_combinations)
        
        for combination in combinations:

            # compare widths
            if(combination.width > highest_width):
                highest_width, highest_weight, most_number_of_items, best_combination = set_as_best_combination(combination)

            # compare weights
            elif(combination.width == highest_width) and (combination.weight > highest_weight):
                highest_width, highest_weight, most_number_of_items, best_combination = set_as_best_combination(combination)

            # compare number of items
            elif(combination.width == highest_width) and (combination.weight == highest_weight) \
                and (len(combination.index_number) > most_number_of_items):
                highest_width, highest_weight, most_number_of_items, best_combination = set_as_best_combination(combination)

            # compare ids
            elif(combination.width == highest_width) and (combination.weight == highest_weight) \
                and (len(combination.index_number) == most_number_of_items):
                best_combination = compare_ids_in_combinations(combination, best_combination)    
                highest_width, highest_weight, most_number_of_items, best_combination = set_as_best_combination(best_combination)

        combinations = []

    return best_combination



def sort_to_subsets(array_of_items):
    combinations = []
    while(array_of_items):
        best_combination = find_best_combination(array_of_items)
        combinations.append(best_combination)
        array_of_items = remove_best_combination(best_combination, array_of_items)
    return combinations


def sort_within_subsets(combinations, catalog_of_items):
    new_combinations = []
    for combination in combinations:
        items_in_combination = combination.index_number
        items_list = [catalog_of_items[str(i)] for i in items_in_combination]

        items_sorted_by_width = sorted(items_list, key=lambda x: x.width, reverse=True)

        # no duplicate width values
        if len([i.width for i in items_sorted_by_width]) == len(set([i.width for i in items_sorted_by_width])):
            new_combinations.append(items_sorted_by_width)
            continue
        else:
            # sort by weight    
            items_sorted_by_weight = []
            same_width_items = []
            current_width_value = items_sorted_by_width[0].width
            same_width_items.append(items_sorted_by_width[0])
            for i in range(1, len(items_sorted_by_width)):
                if items_sorted_by_width[i].width != current_width_value:
                    items_sorted_by_weight.extend(sorted(same_width_items, key=lambda x: x.weight, reverse=True))
                    same_width_items = []
                    current_width_value = items_sorted_by_width[i].width
                same_width_items.append(items_sorted_by_width[i])    
                print same_width_items
            if same_width_items:
                items_sorted_by_weight.extend(sorted(same_width_items, key=lambda x: x.weight, reverse=True))

            if len([i.weight for i in items_sorted_by_weight]) == len(set([i.weight for i in items_sorted_by_weight])):
                new_combinations.append(items_sorted_by_weight)
                continue
            else:
                # sort by ids
                items_sorted_by_id = []
                same_weight_items = []
                current_weight_value = items_sorted_by_weight[0].weight
                same_weight_items.append(items_sorted_by_weight[0])
                for i in range(1, len(items_sorted_by_weight)):
                    if items_sorted_by_weight[i].weight != current_weight_value:
                        items_sorted_by_id.extend(sorted(same_weight_items, key=lambda x: x.index_number[0]))
                        same_weight_items = []
                        current_weight_value = items_sorted_by_weight[i].weight
                    same_weight_items.append(items_sorted_by_weight[i])    
                if same_weight_items:
                    items_sorted_by_id.extend(sorted(same_weight_items, key=lambda x: x.index_number[0]))

                new_combinations.append(items_sorted_by_id)  
    return new_combinations                     

def main():

    array_of_items = read_input()

    catalog_of_items = make_catalog(array_of_items)

    combinations = sort_to_subsets(array_of_items)

    new_combinations = sort_within_subsets(combinations, catalog_of_items)

    if len(new_combinations) > 0:
        print "A:" + ','.join(str(x.index_number[0]) for x in new_combinations[0])
    else:
        print "A:"

    if len(new_combinations) > 1:
        print "B:" + ','.join(str(x.index_number[0]) for x in new_combinations[1])
    else:
        print "B:"        

    if len(new_combinations) > 2:
        print "C:" + ','.join(str(x.index_number[0]) for x in new_combinations[2])
    else:
        print "C:"                



if __name__ == '__main__':
    main()