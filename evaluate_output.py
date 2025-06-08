import textstat

def evaluate_description(desc, target_length=(80, 120)):
    length = len(desc.split())
    score = textstat.flesch_reading_ease(desc)
    return {
        "word_count": length,
        "within_bounds": target_length[0] <= length <= target_length[1],
        "readability_score": score,
        "readability_level": textstat.text_standard(desc)
    }
