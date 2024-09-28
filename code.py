import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class SoftwareArchitectureVisualizationTool:
    def __init__(self):
        self.components = {}
        self.relationships = {}

    def create_component(self):
        component_id = input("Enter component ID: ")
        if component_id in self.components:
            print(f"Component {component_id} already exists.")
            return
        name = input("Enter component name: ")
        metadata = input("Enter component metadata (optional): ")
        self.components[component_id] = {"name": name, "metadata": metadata}
        print(f"Component {component_id} created successfully.")

    def update_component(self):
        component_id = input("Enter component ID to update: ")
        if component_id in self.components:
            name = input("Enter new component name (optional): ")
            metadata = input("Enter new component metadata (optional): ")
            if name:
                self.components[component_id]["name"] = name
            if metadata:
                self.components[component_id]["metadata"] = metadata
            print(f"Component {component_id} updated successfully.")
        else:
            print(f"Component {component_id} not found.")

    def delete_component(self):
        component_id = input("Enter component ID to delete: ")
        if component_id in self.components:
            del self.components[component_id]
            print(f"Component {component_id} deleted successfully.")
        else:
            print(f"Component {component_id} not found.")

    def create_relationship(self):
        component_id1 = input("Enter first component ID: ")
        component_id2 = input("Enter second component ID: ")
        relationship_type = input("Enter relationship type: ")
        if component_id1 in self.components and component_id2 in self.components:
            self.relationships[(component_id1, component_id2)] = relationship_type
            print(f"Relationship between {component_id1} and {component_id2} created successfully.")
        else:
            print("One or both components not found.")

    def update_relationship(self):
        component_id1 = input("Enter first component ID: ")
        component_id2 = input("Enter second component ID: ")
        if (component_id1, component_id2) in self.relationships:
            relationship_type = input("Enter new relationship type: ")
            self.relationships[(component_id1, component_id2)] = relationship_type
            print(f"Relationship between {component_id1} and {component_id2} updated successfully.")
        else:
            print(f"Relationship between {component_id1} and {component_id2} not found.")

    def delete_relationship(self):
        component_id1 = input("Enter first component ID: ")
        component_id2 = input("Enter second component ID: ")
        if (component_id1, component_id2) in self.relationships:
            del self.relationships[(component_id1, component_id2)]
            print(f"Relationship between {component_id1} and {component_id2} deleted successfully.")
        else:
            print(f"Relationship between {component_id1} and {component_id2} not found.")

    def print_architecture(self):
        print("Components:")
        for component_id, component in self.components.items():
            print(f"{component_id}: {component['name']} (Metadata: {component['metadata']})")

        print("\nRelationships:")
        for (component_id1, component_id2), relationship_type in self.relationships.items():
            print(f"{component_id1} {relationship_type} {component_id2}")

    def detect_architecture_smells(self):
        cyclic_dependencies = []
        for component_id1 in self.components:
            for component_id2 in self.components:
                if (component_id1, component_id2) in self.relationships and (component_id2, component_id1) in self.relationships:
                    cyclic_dependencies.append((component_id1, component_id2))
        return cyclic_dependencies

    def visualize_architecture(self):
        G = nx.Graph()

        # Add components as nodes
        for comp_id, comp in self.components.items():
            G.add_node(comp_id, label=comp['name'])

        # Add relationships as edges
        for (comp_id1, comp_id2), relationship_type in self.relationships.items():
            G.add_edge(comp_id1, comp_id2, label=relationship_type)

        pos = nx.spring_layout(G)  # Positions for all nodes

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.title("Software Architecture Visualization")
        plt.show()

    def visualize_flowchart(self):
        fig, ax = plt.subplots(figsize=(10, 6))

        # Draw flowchart-like layout
        y_pos = np.arange(len(self.components))
        ax.barh(y_pos, np.ones(len(self.components)), align='center', color='lightgreen')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(list(self.components.keys()))
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Flowchart Representation')
        ax.set_title('Software Architecture Flowchart')

        # Show relationships as arrows
        for (comp_id1, comp_id2), relationship_type in self.relationships.items():
            ax.annotate(relationship_type, xy=(0.5, y_pos[list(self.components.keys()).index(comp_id2)]),
                                                xytext=(0.5, y_pos[list(self.components.keys()).index(comp_id1)]),
                                                arrowprops=dict(facecolor='black', shrink=0.05))

        plt.show()


def main():
    tool = SoftwareArchitectureVisualizationTool()

    while True:
        print("\nSoftware Architecture Visualization Tool")
        print("1. Create Component")
        print("2. Update Component")
        print("3. Delete Component")
        print("4. Create Relationship")
        print("5. Update Relationship")
        print("6. Delete Relationship")
        print("7. Print Architecture")
        print("8. Detect Architecture Smells")
        print("9. Visualize Architecture")
        print("10. Visualize Flowchart")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tool.create_component()
        elif choice == "2":
            tool.update_component()
        elif choice == "3":
            tool.delete_component()
        elif choice == "4":
            tool.create_relationship()
        elif choice == "5":
            tool.update_relationship()
        elif choice == "6":
            tool.delete_relationship()
        elif choice == "7":
            tool.print_architecture()
        elif choice == "8":
            smells = tool.detect_architecture_smells()
            print("Cyclic Dependencies:", smells)
        elif choice == "9":
            tool.visualize_architecture()
        elif choice == "10":
            tool.visualize_flowchart()
        elif choice == "11":
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
