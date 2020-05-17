from yaat import Yaat
from yaat.responses import JSONResponse
from yaat.staticfiles import StaticFiles
from yaat.templating import Jinja2Template
import mimetypes
import tempfile
import os

from prediction import is_hotdog


statics = StaticFiles("static")
templates = Jinja2Template("templates")

app = Yaat()
app.mount(statics, "/static")


@app.route("/")
async def index(request):
    return templates.TemplateResponse("index.html")


@app.route("/seefood", methods=["POST"])
async def seefood(request):
    form = await request.form()
    picture = form.get("picture")

    # check if image exists
    if picture is None:
        return JSONResponse({
            "error": "File is not uploaded."
        }, status_code=400)

    # check if image
    if "image" not in picture.content_type.split("/"):
        return JSONResponse({
            "error": "Invalid picture."
        }, status_code=400)

    # write image into temporary file
    file_ext = mimetypes.guess_extension(picture.content_type)
    tmp = tempfile.NamedTemporaryFile(suffix=file_ext, prefix=os.path.basename(__file__))

    with open(tmp.name, 'wb') as tf:
        content = await picture.read()
        tf.write(content)

    # do some magic here
    hotdog = is_hotdog(tf.name)
    return JSONResponse({
        "hotdog": True if hotdog else False
    })
