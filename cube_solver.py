import time
import copy
import heapq

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))    


solved = {
          (0,0,0): ("w","r","b"), (1,0,0): ("o","w","b"),
          (0,1,0): ("w","g","r"), (1,1,0): ("o","g","w"), 
          (0,1,1): ("r","g","y"), (1,1,1): ("y","g","o"),
          (0,0,1): ("r","y","b"), (1,0,1): ("y","o","b"),
          }


def right_turn(state):
    return hashabledict({
            (0,0,0): state[(0,0,0)], (1,0,0): (state[(1,0,1)][1], state[(1,0,1)][2], state[(1,0,1)][0]),
            (0,1,0): state[(0,1,0)], (1,1,0): state[(1,0,0)],
            (0,1,1): state[(0,1,1)], (1,1,1): (state[(1,1,0)][1], state[(1,1,0)][2], state[(1,1,0)][0]),
            (0,0,1): state[(0,0,1)], (1,0,1): (state[(1,1,1)][1], state[(1,1,1)][2], state[(1,1,1)][0]),
            })


def right_p_turn(state):
    return hashabledict(right_turn(right_turn(right_turn(state))))


def right_2_turn(state):
    return hashabledict(right_turn(right_turn(state)))


def left_turn(state):
    return hashabledict({
            (0,0,0): (state[(0,1,0)][1], state[(0,1,0)][2], state[(0,1,0)][0]), (1,0,0): state[(1,0,0)],
            (0,1,0): (state[(0,1,1)][1], state[(0,1,1)][2], state[(0,1,1)][0]), (1,1,0): state[(1,1,0)],
            (0,1,1): state[(0,0,1)], (1,1,1): state[(1,1,1)],
            (0,0,1): (state[(0,0,0)][1], state[(0,0,0)][2], state[(0,0,0)][0]), (1,0,1): state[(1,0,1)],
            })


def left_p_turn(state):
    return hashabledict(left_turn(left_turn(left_turn(state))))


def left_2_turn(state):
    return hashabledict(left_turn(left_turn(state)))


def front_turn(state):
    return hashabledict({
            (0,0,0): (state[(1,0,0)][1], state[(1,0,0)][2], state[(1,0,0)][0]), (1,0,0): (state[(1,1,0)][1], state[(1,1,0)][2], state[(1,1,0)][0]),
            (0,1,0): state[(0,0,0)], (1,1,0): (state[(0,1,0)][1], state[(0,1,0)][2], state[(0,1,0)][0]),
            (0,1,1): state[(0,1,1)], (1,1,1): state[(1,1,1)],
            (0,0,1): state[(0,0,1)], (1,0,1): state[(1,0,1)],
            })


def front_p_turn(state):
    return hashabledict(front_turn(front_turn(front_turn(state))))


def front_2_turn(state):
    return hashabledict(front_turn(front_turn(state)))


def back_turn(state):
    return hashabledict({
            (0,0,0): state[(0,0,0)], (1,0,0): state[(1,0,0)],
            (0,1,0): state[(0,1,0)], (1,1,0): state[(1,1,0)],
            (0,1,1): (state[(1,1,1)][1], state[(1,1,1)][2], state[(1,1,1)][0],), (1,1,1): state[(1,0,1)],
            (0,0,1): (state[(0,1,1)][1], state[(0,1,1)][2], state[(0,1,1)][0],), (1,0,1): (state[(0,0,1)][1], state[(0,0,1)][2], state[(0,0,1)][0],),
            })


def back_p_turn(state):
    return hashabledict(back_turn(back_turn(back_turn(state))))


def back_2_turn(state):
    return hashabledict(back_turn(back_turn(state)))


def up_turn(state):
    return hashabledict({
            (0,0,0): state[(0,0,0)], (1,0,0): state[(1,0,0)],
            (0,1,0): state[(1,1,0)], (1,1,0): state[(1,1,1)],
            (0,1,1): state[(0,1,0)], (1,1,1): state[(0,1,1)],
            (0,0,1): state[(0,0,1)], (1,0,1): state[(1,0,1)],
            })


def up_p_turn(state):
    return hashabledict(up_turn(up_turn(up_turn(state))))


def up_2_turn(state):
    return hashabledict(up_turn(up_turn(state)))


def down_turn(state):
    return hashabledict({
            (0,0,0): state[(0,0,1)], (1,0,0): state[(0,0,0)],
            (0,1,0): state[(0,1,0)], (1,1,0): state[(1,1,0)],
            (0,1,1): state[(0,1,1)], (1,1,1): state[(1,1,1)],
            (0,0,1): state[(1,0,1)], (1,0,1): state[(1,0,0)],
            })


def down_p_turn(state):
    return hashabledict(down_turn(down_turn(down_turn(state))))


def down_2_turn(state):
    return hashabledict(down_turn(down_turn(state)))


turns = {
         "r": right_turn, "rp": right_p_turn, "r2": right_2_turn,
         "l": left_turn, "lp": left_p_turn, "l2": left_2_turn,
         "f": front_turn, "fp": front_p_turn, "f2": front_2_turn,
         "b": back_turn, "bp": back_p_turn, "b2": back_2_turn,
         "u": up_turn, "up": up_p_turn, "u2": up_2_turn,
         "d": down_turn, "dp": down_p_turn, "d2": down_2_turn,
         }

rotations = {"front": hashabledict(solved),
             "back": [turns["r2"], turns["l2"]],
             "top": [turns["rp"], turns["l"]],
             "bottom": [turns["r"], turns["lp"]],
             "right": [turns["u"], turns["dp"]],
             "left": [turns["up"], turns["d"]],
             "spin": [turns["bp"], turns["f"]],
             }


def rotated_solutions(state):
    cube = copy.deepcopy(state)
    faces = [
                     rotations["back"], 
                     rotations["top"], rotations["bottom"],
                     rotations["right"], rotations["left"],
                     ]
    all_rotations = set()

    for face in faces:
        for half_rot in face:
            cube = half_rot(cube)

        for i in range(4):
            for spin in rotations["spin"]:
                cube = spin(cube)
            all_rotations.add(hashabledict(cube))
        
        cube = copy.deepcopy(state)

    for i in range(4):
        for spin in rotations["spin"]:
            cube = spin(cube)
        all_rotations.add(hashabledict(cube))

    return all_rotations


solutions = rotated_solutions(solved)
    

def cube_solver(cube_position):
    agenda = [(0, 0, cube_position)]
    visited = {cube_position: (None, None, 0)} # tuple is (turn, state, f score)

    def next_positions(cube_position):
        """
        Given a cube position, return the possible positions
        reachable by making only one move.
        """
        positions = []
        for turn, pos in turns.items():
            positions.append((pos(cube_position), turn))

        return positions
    
    def heuristic(cube_position):
        """
        This heuristic function estimates the cost of the shortest path
        from the given cube position to any of the solution positions.
        """
        min_distance = float('inf')
        for solution in solutions:
            distance = sum([1 for key, val in cube_position[0].items() if cube_position[0][key] != solution[key]])
            if distance < min_distance:
                min_distance = distance
        return min_distance
    
    counter = 0
    while agenda:
        current_f, entry, current_position = heapq.heappop(agenda)

        for position in next_positions(current_position):

            g_score = visited[current_position][2] + 1
            f_score = g_score + heuristic(position)
            counter += 1

            if position[0] not in visited or f_score < visited[position[0]][2]:
                visited[position[0]] = (position[1], current_position, f_score)
                heapq.heappush(agenda, (f_score, counter, position[0]))

            if current_position in solutions:
                movement = visited[current_position][0]
                path = []

                while movement is not None:
                    path.append(movement)
                    current_position = visited[current_position][1]
                    movement = visited[current_position][0]
                return path[::-1]
            
    return None


def scrambler(state, scramble):
    for move in scramble:
        state = turns[move](state)

    return state

start = time.time()
official_scramble = scrambler(solved, ["u", "r", "f2", "up", "rp", "f2", "u", "r", "u2"])
print(cube_solver(official_scramble))
end = time.time()
print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["u", "r", "f2", "d", "r", "b", "d"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["u", "r", "f2", "r", "b", "d"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["u", "r", "f2", "r", "b"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["r", "f2", "r", "b"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["r", "f2", "d"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start = time.time()
# scramble1 = scrambler(solved, ["b", "d"])
# print(cube_solver(scramble1))
# end = time.time()
# print(end-start)

# start_back = time.time()
# scramble_back = scrambler(solved, ["b2"])
# print(cube_solver(scramble_back))
# end_back = time.time()
# print(end_back - start_back)

# start_front = time.time()
# scramble_front = scrambler(solved, ["f2"])
# end_front = time.time()
# print(cube_solver(scramble_front))
# print(end_front - start_front)

# start_right = time.time()
# scramble_right = scrambler(solved, ["r2"])
# print(cube_solver(scramble_right))
# end_right = time.time()
# print(end_right - start_right)

# start_left = time.time()
# scramble_left = scrambler(solved, ["l2"])
# end_left = time.time()
# print(cube_solver(scramble_left))
# print(end_left - start_left)

# start_up = time.time()
# scramble_up = scrambler(solved, ["u2"])
# end_up = time.time()
# print(cube_solver(scramble_up))
# print(end_up - start_up)

# start_down = time.time()
# scramble_down = scrambler(solved, ["d2"])
# end_down = time.time()
# print(cube_solver(scramble_down))
# print(end_down - start_down)
