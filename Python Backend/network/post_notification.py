# pip install firebase-admin
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()

doc_ref = store.collection(u'alerts')
doc_ref.add({
    u'name': u'This is soo cool :D'
})
