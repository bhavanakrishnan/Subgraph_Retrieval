import re
import string

def normalize_answer(s):
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

def exact_match_score(prediction, ground_truth):
    # import pdb
    # pdb.set_trace()
    return normalize_answer(prediction) == normalize_answer(ground_truth)

def ems(prediction, ground_truths):
    return max([exact_match_score(prediction, gt) for gt in ground_truths])

def f1(preds, answers):
    """
    pred - 1st hit from model for answer.
    answers - all the answers available in test data features.
    """
    correct, total = 0.0, 0.0
    preds = normalize_answer(preds)
    # answers=normalize_answer(answers)
    for ans in answers:
        if preds in normalize_answer(ans):
            correct += 1

    if len(answers) == 0:
        if total == 0:
            return 1.0, 1.0, 1.0, 1.0 # precision, recall, f1, hits
        else:
            return 0.0, 1.0, 0.0, 1.0 # precision, recall, f1, hits
    else:
        # hits = float(best_pred in answers)
        if total == 0:
            return 1.0, 0.0, 0.0 # precision, recall, f1, hits
        else:

            precision, recall = correct / total, correct / len(answers)  

            f1 = 2.0 / (1.0 / precision + 1.0 / recall) if precision != 0 and recall != 0 else 0.0
            
            print(f"correct : {correct}, total: {total}, Precision: {precision}, Recall: {recall}, f1: {f1}")
            return correct, precision, recall, f1