class Graph:

    def __init__(self):
        self.graph = {}

    # Add a location
    def add_location(self, location):

        if location not in self.graph:
            self.graph[location] = []

    # Add a route between two locations
    def add_route(self, location1, location2):

        self.add_location(location1)
        self.add_location(location2)

        self.graph[location1].append(location2)
        self.graph[location2].append(location1)

    # View all locations and routes
    def view_routes(self):

        if not self.graph:
            print("No locations available.")
            return

        print("\n--- LOCATIONS AND ROUTES ---")

        for location in self.graph:
            print(location, "->", self.graph[location])

    # BFS traversal
    def bfs(self, start):

        if start not in self.graph:
            print("Location not found.")
            return

        visited = []
        queue = [start]

        while queue:

            current = queue.pop(0)

            if current not in visited:

                visited.append(current)

                for neighbour in self.graph[current]:

                    if neighbour not in visited:
                        queue.append(neighbour)

        print("BFS Route:", " -> ".join(visited))

    # Find shortest route
    def shortest_route(self, start, end):

        if start not in self.graph:
            print("Starting location not found.")
            return

        if end not in self.graph:
            print("Destination not found.")
            return

        queue = [[start]]
        visited = []

        while queue:

            path = queue.pop(0)
            current = path[-1]

            if current == end:

                print("Shortest Route:", " -> ".join(path))
                return

            if current not in visited:

                visited.append(current)

                for neighbour in self.graph[current]:

                    if neighbour not in visited:

                        new_path = path + [neighbour]
                        queue.append(new_path)

        print("No route found.")


# Testing the graph module
if __name__ == "__main__":

    graph = Graph()

    graph.add_route("Home", "University")
    graph.add_route("Home", "Market")
    graph.add_route("University", "Library")
    graph.add_route("Market", "Hospital")
    graph.add_route("Library", "Hospital")

    graph.view_routes()

    print()

    graph.bfs("Home")

    print()

    graph.shortest_route("Home", "Hospital")