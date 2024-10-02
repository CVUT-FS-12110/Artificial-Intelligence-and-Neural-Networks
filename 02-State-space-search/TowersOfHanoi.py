from copy import deepcopy
from collections import deque
from typing import List, Optional, Set


class ToHState:
    """
    Represents the state of the Towers of Hanoi game.

    Attributes
    ----------
    towers : List[List[int]]
        A list containing three lists, each representing a tower with its discs.
    parent : Optional[ToHState]
        The parent state from which this state was derived.
    action : str
        A description of the action taken to reach this state.
    towers_names : List[str]
        Names of the towers, default is ['A', 'B', 'C'].
    discs : List[int]
        List of disc identifiers, default is [1, 2, 3].
    """

    towers_names = ['A', 'B', 'C']
    discs = [1, 2, 3]

    def __init__(
            self,
            a: List[int],
            b: List[int],
            c: List[int],
            parent: Optional['ToHState'] = None,
            action: str = ""
    ):
        """
        Initializes a ToHState instance.
        """
        self.towers = deepcopy([a, b, c])  # State of the towers
        self.parent = parent  # Previous state
        self.action = action  # Action leading to this state

    def test(self) -> bool:
        """
        Checks if the current state adheres to the rules of the Towers of Hanoi game.
        """
        for tower in self.towers:
            last = max(self.discs) + 1  # Initialize to a value larger than any disc
            for disc in tower:
                if disc > last:
                    # A larger disc is on top of a smaller one, invalid state
                    return False
                last = disc  # Update last to the current disc
        return True  # All towers are valid

    def next_states(self) -> List['ToHState']:
        """
        Generates all valid states reachable from this state by making one legal move.
        """
        states = []
        for idx, tower in enumerate(self.towers):
            if tower:
                # Copy the current tower and remove the top disc
                new_tower = tower[:-1]
                move = tower[-1]
                # Identify towers to which the disc can be moved
                for available_tower in range(len(self.towers)):
                    if available_tower != idx:
                        # Create new state by moving the disc to the available tower
                        new_state_towers = deepcopy(self.towers)
                        new_state_towers[idx] = new_tower
                        new_state_towers[available_tower] = self.towers[available_tower] + [move]
                        # Instantiate new ToHState
                        new_state = ToHState(
                            *new_state_towers,
                            parent=self,
                            action=f"Move disk {move} from {self.towers_names[idx]} to {self.towers_names[available_tower]}"
                        )
                        # Check if the new state is valid
                        if new_state.test():
                            states.append(new_state)
        return states

    def ancestors(self) -> List['ToHState']:
        """
        Returns a list of all ancestor states in order from the initial state to the parent of the current state.
        """
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        ancestors.reverse()
        return ancestors

    def __repr__(self) -> str:
        """
        Returns a string representation of the ToHState.
        """
        return (
            f'Action="{self.action}", '
            f'ToHState(a={self.towers[0]}, b={self.towers[1]}, c={self.towers[2]})'
        )

    def __eq__(self, other: object) -> bool:
        """
        Checks if two ToHState instances are equal.
        """
        if not isinstance(other, ToHState):
            return NotImplemented
        return self.towers == other.towers

    def __hash__(self) -> int:
        """
        Returns a hash value for the ToHState.
        """
        return hash(tuple(tuple(tower) for tower in self.towers))


def breadth_first_search(start: ToHState, final: ToHState) -> Optional[ToHState]:
    """
    Performs breadth-first search to find a solution from the start state to the final state.
    """
    seen: Set[ToHState] = set([start])  # Set of already visited states
    queue = deque([start])  # Queue for BFS

    # while queue:
        # YOUR CODE HERE

    return None  # No solution found


def depth_first_search(start: ToHState, final: ToHState) -> Optional[ToHState]:
    """
    Performs depth-first search to find a solution from the start state to the final state.
    """
    seen: Set[ToHState] = set([start])  # Set of already visited states
    stack = deque([start])  # Stack for DFS implemented using deque

    # while stack:
        # YOUR CODE HERE

    return None # No solution found


# TEST
if __name__ == "__main__":
    start = ToHState([3, 2, 1], [], [], action="START")
    final = ToHState([], [], [3, 2, 1])  # Goal state

    # Breadth-First Search Test
    solution = breadth_first_search(start, final)
    if solution:
        print('Breadth-first search solution found')
        way = solution.ancestors() + [solution]
        for step in way:
            print(step)
    else:
        print('Breadth-first search solution not found')

    # Depth-First Search Test
    solution = depth_first_search(start, final)
    if solution:
        print('Depth-first search solution found')
        way = solution.ancestors() + [solution]
        for step in way:
            print(step)
    else:
        print('Depth-first search solution not found')
