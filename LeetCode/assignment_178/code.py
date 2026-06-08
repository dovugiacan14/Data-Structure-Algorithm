

def order_scores(scores: pd.DataFrame):
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    return scores.sort_values("score", ascending=False)[["score", "rank"]]
