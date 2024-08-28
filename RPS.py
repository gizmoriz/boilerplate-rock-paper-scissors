import random

def player(prev_play, opponent_history=[]):
    # Track moves and patterns
    move_counts = {"R": 0, "P": 0, "S": 0}
    pattern_counts = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}
    
    # Append the latest move to history
    if prev_play != '':
        opponent_history.append(prev_play)

    # Update move and pattern counts
    for i in range(1, len(opponent_history)):
        move_counts[opponent_history[i]] += 1
        if i > 0:
            pattern = opponent_history[i-1] + opponent_history[i]
            if pattern in pattern_counts:
                pattern_counts[pattern] += 1

    # If this is the first move, choose randomly
    if prev_play == '':
        return random.choice(['R', 'P', 'S'])

    # Predict the opponent's next move based on the most frequent pattern
    if len(opponent_history) >= 2:
        last_move = opponent_history[-1]
        second_last_move = opponent_history[-2]
        pattern = second_last_move + last_move
        
        if pattern in pattern_counts and pattern_counts[pattern] > 0:
            # Choose the move that beats the predicted next move
            predicted_move = {'R': 'P', 'P': 'S', 'S': 'R'}[last_move]
            return predicted_move

    # If no useful pattern found, use statistical analysis and add a level of randomness
    if sum(move_counts.values()) == 0:
        return random.choice(['R', 'P', 'S'])

    # Improved strategy: Adapt based on the opponent's most recent move
    most_common_move = max(move_counts, key=move_counts.get)
    next_move = {'R': 'P', 'P': 'S', 'S': 'R'}[most_common_move]
    
    # Add a level of randomness to avoid being too predictable
    if random.random() < 0.2:  # 20% chance to play randomly
        return random.choice(['R', 'P', 'S'])
    
    return next_move
