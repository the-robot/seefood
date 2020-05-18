### Seefood

The model is trained in Transfer Learning with [Resnet34](https://towardsdatascience.com/understanding-and-visualizing-resnets-442284831be8). Seefood model `./src/prediction/data/models` has 89% accuracy.

For the dataset used to train the model, you can [download it here](https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog).

It can predict not just **hotdog**, also **not hotdog!**.

---

I made a web application on top. The app is built with [Yaat framework](https://github.com/yaat-project/yaat) and to run the application, you can follow the instruction below.

```bash
pip install requirements.txt
uvicorn app:app
```

<p align="center">
    <img src="https://raw.githubusercontent.com/the-robot/seefood/master/screenshots/homepage.png">
</p>
