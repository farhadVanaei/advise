from flask import jsonify

from project.models.CRUD import crud
from project.models.models import Zone
from . import *
from extensions import db

@mod.route("/")
@mod.route("/<page>")
def asset_list(page=1):
    temp = crud(model_name='asset')
    return jsonify(temp.listAll(page))
