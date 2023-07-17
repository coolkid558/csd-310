from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster1.ptzzspe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
si = db.students.find({"thorin":"student_id"})
sf = db.students.find({"thorin":"first_name"})
sl = db.students.find({"thorin":"last_name"})
ei = db.students.find({"bilbo":"student_id"})
ef = db.students.find({"bilbo":"first_name"})
el = db.students.find({"bilbo":"last_name"})
ni = db.students.find({"frodo":"student_id"})
nf = db.students.find({"frodo":"first_name"})
nl = db.students.find({"frodo":"last_name"})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
print("Student ID: " + str(si) + "\n First Name: " + str(sf) + "\n Last Name: " + str(sl))
print()
print("Student ID: " + str(ei) + "\n First Name: " + str(ef) + "\n Last Name: " + str(el))
print()
print("Student ID: " + str(ni) + "\n First Name: " + str(nf) + "\n Last Name: " + str(nl))
print()
db.students.update({
    "thorin": "last_name"
},
$set:
{
    "last_name":"Oakenshield III"
})
print("-- DISPLAY STUDENT DOCUMENT 1007 --")
print("Student ID: " + str(si) + "\n First Name: " + str(sf) + "\n Last Name: " + str(sl))