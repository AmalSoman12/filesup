import pyrebase

config={ 
 "apiKey":"AIzaSyAAeW916nD4atHeIyz2KAEIeVajgLOMMdg",

 "authDomain": "filesup-421cc.firebaseapp.com",
 
 "databaseURL":"filesup-421cc.firebaseapp.com",

 "projectId": "filesup-421cc",

 "storageBucket": "filesup-421cc.appspot.com",

 "messagingSenderId": "243025574698",

 "appId": "1:243025574698: web:0bfb8e5655db37c1cf3c53",

 "measurementId":"G-JT13V14XD"
 }
firebase=pyrebase.initialize_app(config)

storage= firebase.storage()

path_on_cloud=("videos/vidtest1.mp4") 
path_local="vidtest.mp4"
storage.child(path_on_cloud).put(path_local)
