def full_jusify(words, maxWidth): 
    result = []
    line_words = []
    line_len = 0
    for word in words: 
        if line_len + len(word) + len(line_words) > maxWidth: 
            total_spaces = maxWidth - line_len
            gaps= len(line_words) - 1 
            if gaps == 0: 
                result.append(line_words[0] + " "*total_spaces)
            else: 
                space_per_gap = total_spaces // gaps 
                extra_spaces = total_spaces % gaps 
                line = ""
                for i, w in enumerate(line_words): 
                    line += w 
                    if i < gaps: 
                        line += " "*space_per_gap
                        if i < extra_spaces:
                            line += " "
                result.append(line)
            line_words, line_len = [], 0 
        line_words.append(word)
        line_len += len(word)
    last_line = " ".join(line_words)
    remaining_spaces = maxWidth - len(last_line)
    result.append(last_line + " "*remaining_spaces)
    return result
