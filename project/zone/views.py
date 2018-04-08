from flask import jsonify, render_template
from project.models.CRUD import crud
from . import mod


NAME = "Zone"

@mod.route("/")
@mod.route("/<page>")
def zone_list(page=1):
    temp = crud(model_name=NAME)
    title = temp.getAllTitle()
    result = temp.listAll(page)
    return render_template("base.html",name=NAME,title=title,list=result)

