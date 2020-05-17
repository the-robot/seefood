from fastai.metrics import error_rate
from fastai.vision import (
    ImageDataBunch,
    cnn_learner,
    get_image_files,
    get_transforms,
    imagenet_stats,
    models,
)
from pathlib import Path

# Config and data path
bs = 64
path = Path("./data")

# Load data
tfms = get_transforms(do_flip=False)
data = ImageDataBunch.from_folder(path, ds_tfms=get_transforms(), size=224, bs=bs).normalize(imagenet_stats)

# Train data in transfer learning using resnet34
learn = cnn_learner(data, models.resnet34, metrics=error_rate)

# Find the best learning rate
learn.lr_find()

# Retrain the whole model
learn.unfreeze()
learn.fit_one_cycle(4, max_lr=slice(1e-6, 1e-3))

# Export the trained model
learn.export('seefood_model.pkl')
