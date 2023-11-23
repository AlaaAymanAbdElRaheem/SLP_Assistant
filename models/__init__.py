#!/usr/bin/env python3
'''Initailize the models package and the storage engine'''
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
