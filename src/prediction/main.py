from fastai.vision import load_learner, open_image

# load model
model = load_learner('./prediction/data/models', 'seefood_model.pkl')

def is_hotdog(filepath: str) -> bool:
    """
    in current model, hotdog is 0 and not hotdog is 1
    """

    category, tensor, probs = model.predict(
        open_image(filepath)
    )
    return False if model.data.c2i.get(
        str(category)
    ) else True
