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

cloud=input(str("Enter firebase Path"))
local=input(str("Enter path of the file*))
path_on_cloud=(cloud) 
path_local=local
storage.child(path_on_cloud).put(path_local)
