import os

import firebase_admin
from firebase_admin import credentials

# cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "/home/pawan/vendor-site/api/badidukkan-firebase-service.json"))
cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "/backend/api/badidukkan-firebase-service.json"))
try:
    default_app = firebase_admin.initialize_app(cred)
except ValueError:
    print("firebase app already initialized")