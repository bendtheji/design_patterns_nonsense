class Item(object):

    def __init__(self, id_number, width, weight):
        self.id_number = id_number
        self.width = width
        self.weight = weight

    def __add__(self, other):
        id_numbers = [];
        id_numbers.extend(self.id_number)
        id_numbers.extend(other.id_number)
        total_width = self.width + other.width
        total_weight = self.weight + other.weight
        return Item(id_numbers, total_width, total_weight)

    def __gt__(self, other):
        if(self.width > other.width):
            return True
        elif(self.width == other.width) and (self.weight > other.weight):
            return True
        elif(self.width == other.width) and (self.weight == other.weight) \
            and (len(self.id_number) > len(other.id_number)):
            return True
        elif(self.width == other.width) and (self.weight == other.weight) \
            and (len(self.id_number) == len(other.id_number)) and \
            compare_ids_in_combinations(self.id_number, other.id_number):
            return True
        else:
            return False             


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
        catalog[str(i.id_number[0])] = i

    return catalog    


def compare_ids_in_combinations(combination_id_number, best_combination_id_number):

    for i,j in zip(sorted(combination_id_number), sorted(best_combination_id_number)):
        if i < j:
            return True
        elif i > j:
            return False
        else:
            continue
    return True                


def remove_best_combination(best_combination, array_of_items):
    items_to_remove = best_combination.id_number
    return [i for i in array_of_items if i.id_number[0] not in items_to_remove]

def find_best_combination(array_of_items):
    max_width = 1100
    max_weight = 1000
    best_combination = None
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

            if best_combination is None:
                best_combination = combination
            if(combination > best_combination):
                best_combination = combination

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
        items_in_combination = combination.id_number
        items_list = [catalog_of_items[str(i)] for i in items_in_combination]
        items_sorted = []
        next_highest_priority_item = None

        while(items_list):
            for i in items_list:
                if next_highest_priority_item is None:
                    next_highest_priority_item = i
                else:
                    if i > next_highest_priority_item:
                        next_highest_priority_item = i
            items_sorted.append(next_highest_priority_item)
            items_list.remove(next_highest_priority_item) 
            next_highest_priority_item = None         

        new_combinations.append(items_sorted)

    return new_combinations                     

def main():

    array_of_items = read_input()

    catalog_of_items = make_catalog(array_of_items)

    combinations = sort_to_subsets(array_of_items)

    new_combinations = sort_within_subsets(combinations, catalog_of_items)

    if len(new_combinations) > 0:
        print "A:" + ','.join(str(x.id_number[0]) for x in new_combinations[0])
    else:
        print "A:"

    if len(new_combinations) > 1:
        print "B:" + ','.join(str(x.id_number[0]) for x in new_combinations[1])
    else:
        print "B:"        

    if len(new_combinations) > 2:
        print "C:" + ','.join(str(x.id_number[0]) for x in new_combinations[2])
    else:
        print "C:"                



if __name__ == '__main__':
    main()