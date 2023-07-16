#!/usr/bin/python3
"""initializes storage variable to create FileSorage object for hbnb application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
