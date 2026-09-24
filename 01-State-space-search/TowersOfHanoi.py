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

    def __init__(
        self,
        a: List[int],
        b: List[int],
        c: List[int],
        parent: Optional['ToHState'] = None,
        action: str = "",
        towers_names=None,
        discs=None
    ):
        """
        Initializes a ToHState instance.

        Parameters
        ----------
        a : List[int]
            List of discs on tower A.
        b : List[int]
            List of discs on tower B.
        c : List[int]
            List of discs on tower C.
        parent : Optional[ToHState], optional
            The parent state from which this state was derived, by default None.
        action : str, optional
            Description of the action taken to reach this state, by default "".
        towers_names : List[str]
            Names of the towers, default is ['A', 'B', 'C'].
        discs : List[int]
            List of disc identifiers, default is [1, 2, 3].
        """
        self.towers = deepcopy([a, b, c])  # State of the towers
        self.parent = parent               # Previous state
        self.action = action               # Action leading to this state
        self.towers_names = ['A', 'B', 'C'] if towers_names is None else towers_names
        self.discs = [1, 2, 3] if discs is None else discs

    def test(self) -> bool:
        """
        Checks if the current state adheres to the rules of the Towers of Hanoi game.

        Returns
        -------
        bool
            True if the state is valid according to the game rules, False otherwise.

        Notes
        -----
        In the Towers of Hanoi game, a larger disc cannot be placed on top of a smaller disc.
        This method verifies that this rule is not violated in any of the towers.
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

        Returns
        -------
        List[ToHState]
            A list of valid next states that can be reached from the current state.

        Notes
        -----
        Considers all possible moves of the top disc from one tower to another,
        ensuring the move is legal according to the game rules.
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
                            action=f"Move disk {move} from {self.towers_names[idx]} to {self.towers_names[available_tower]}",
                            towers_names=self.towers_names,
                            discs=self.discs
                        )
                        # Check if the new state is valid
                        if new_state.test():
                            states.append(new_state)
        return states

    def ancestors(self) -> List['ToHState']:
        """
        Returns a list of all ancestor states in order from the initial state to the parent of the current state.

        Returns
        -------
        List[ToHState]
            List of ancestor states, starting from the initial state up to the parent of the current state.

        Notes
        -----
        Iteratively collects all parent states, which is useful for reconstructing the path
        taken to reach the current state.
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

        Returns
        -------
        str
            A string describing the action and the state of the towers.
        """
        return (
            f'Action="{self.action}", '
            f'ToHState(a={self.towers[0]}, b={self.towers[1]}, c={self.towers[2]})'
        )

    def __eq__(self, other: object) -> bool:
        """
        Checks if two ToHState instances are equal.

        Parameters
        ----------
        other : object
            The object to compare with.

        Returns
        -------
        bool
            True if both states have the same configuration, False otherwise.
        """
        if not isinstance(other, ToHState):
            return NotImplemented
        return self.towers == other.towers

    def __hash__(self) -> int:
        """
        Returns a hash value for the ToHState.

        Returns
        -------
        int
            The hash value of the state.

        Notes
        -----
        This method makes ToHState instances hashable, allowing them to be used in sets
        and as dictionary keys, which is useful for tracking visited states efficiently.
        """
        return hash(tuple(tuple(tower) for tower in self.towers))

def breadth_first_search(start: ToHState, final: ToHState) -> Optional[ToHState]:
    """
    Performs breadth-first search to find a solution from the start state to the final state.

    Parameters
    ----------
    start : ToHState
        The initial state.
    final : ToHState
        The target state.

    Returns
    -------
    Optional[ToHState]
        The solution state (if found), otherwise None.

    Notes
    -----
    Implements the breadth-first search algorithm to find the shortest path
    from the start state to the final state in the state space of the Towers of Hanoi game.
    """
    seen: Set[ToHState] = set([start])  # Set of already visited states

    queue = deque([start])  # deque is a double-ended queue

    # while queue:
        # YOUR CODE HERE

    return None  # No solution found

def depth_first_search(start: ToHState, final: ToHState) -> Optional[ToHState]:
    """
    Performs depth-first search to find a solution from the start state to the final state.

    Parameters
    ----------
    start : ToHState
        The initial state.
    final : ToHState
        The target state.

    Returns
    -------
    Optional[ToHState]
        The solution state (if found), otherwise None.

    Notes
    -----
    Implements the depth-first search algorithm to find a path
    from the start state to the final state in the state space of the Towers of Hanoi game.
    """
    seen: Set[ToHState] = set([start])  # Set of already visited states

    stack = deque([start])  # deque is used as a stack here

    # while stack:
        # YOUR CODE HERE

    return None  # No solution found

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
