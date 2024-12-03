import matplotlib.pyplot as plt
from treelib import Tree
import sys, os, ast

line_year = [1]
line_population = [0]
line_avg_age = [0]
line_deaths = [0]
line_children_born = [0]
line_food = [0]

def plot_graph(people, child, death, food):
    global line_year, line_population, line_avg_age, line_max_workers, line_deaths, line_children_born, born_this_year, died_this_year
    line_year.append(line_year[-1] + 1)
    line_population.append(len(people))
    line_food.append(food)

    avg = []
    for person in people:
        avg.append(person.age)
    try:
        line_avg_age.append(sum(avg) / len(people))
    except ZeroDivisionError:
        line_avg_age.append(0)

def show_graph():
    plt.plot(line_year, line_population, label="Population", color=[0, 1, 0])
    plt.plot(line_year, line_avg_age, label="Average Age", color=[1, 1, 0])
    plt.plot(line_year, line_food, label="Food", color=[0, 0, 1])
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Population Simulation')
    plt.legend()
    plt.show()

def familyTree(peopleDictionaryHistory):
    tree = Tree()
    tree.create_node("THE CREATOR", "God") # Root node

    # Use a dictionary to track unique nodes
    added_nodes = {"God"}

    for record in peopleDictionaryHistory:
        name = record[0]
        parent_name = record[2]

        # Generate unique IDs for nodes
        unique_id = f"{name}_{peopleDictionaryHistory.index(record)}"
        parent_unique_id = None
        for r in peopleDictionaryHistory:
            if r[0] == parent_name:
                parent_unique_id = f"{parent_name}_{peopleDictionaryHistory.index(r)}"
                break

        # If the parent is missing, assign it to "God"
        if parent_unique_id is None:
            parent_unique_id = "God"

        # Add the parent node if it does not exist
        if parent_unique_id not in added_nodes:
            try:
                tree.create_node(parent_name, parent_unique_id, parent="God")
                added_nodes.add(parent_unique_id)
            except Exception as e:
                print(f"Error creating parent node {parent_name}: {e}")

        # Add the current node
        if unique_id not in added_nodes:
            try:
                tree.create_node(name, unique_id, parent=parent_unique_id)
                added_nodes.add(unique_id)
            except Exception as e:
                print(f"Error creating node for {name}: {e}")

    # Save and open the output
    output_path = os.path.join(os.path.dirname(__file__), 'output.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        tree.show()
    sys.stdout = sys.__stdout__  # Reset standard output
    with open(output_path, "r", encoding="utf-8") as file: # Open the file in binary mode
        family_tree = file.read()  # Read the entire content as bytes
        decoded_tree = ast.literal_eval(family_tree).decode('utf-8')
        print(decoded_tree)
