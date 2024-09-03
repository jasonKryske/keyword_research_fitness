def search_volume_level(volume):
    if volume > 499:
        return 'ideal'
    elif 500 > volume > 300:
        return 'backup'
    else:
        return 'too low'

def difficulty_level(difficulty):
    if difficulty <= 31:
        return 'easy'
    elif difficulty <=60:
        return 'medium'
    else:
        return 'difficult'

