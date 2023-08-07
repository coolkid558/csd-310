db.student.insert({
    1007: {
        "Player ID": 1,
        "First Name": 'Thorin',
        "Last Name": 'Oakenshield',
        "Team Name": 'Team Gandalf',
    },
    1008: {
        "Player ID": 2,
        "First Name": 'Bilbo',
        "Last Name": 'Baggins',
        "Team Name": 'Team Gandalf',
    },
    1009: {
        "Player ID": 3,
        "First Name": 'Frodo',
        "Last Name": 'Baggins',
        "Team Name": 'Team Gandalf',
    },
    1010: {
        "Player ID": 4,
        "First Name": 'Saruman',
        "Last Name": 'The White',
        "Team Name": 'Team Sauron',
    },
    1011: {
        "Player ID": 5,
        "First Name": 'Angmar',
        "Last Name": 'Witch-king',
        "Team Name": 'Team Sauron',
    },
    1012: {
        "Player ID": 6,
        "First Name": 'Azog',
        "Last Name": 'The Defiler',
        "Team Name": 'Team Sauron'
    },
    1013: {
        "Player ID": 21
        "First Name": 'Smeagol',
        "Last Name": 'Shire Folk',
        "Team Name": 'Team Gandolf',
    }
})
print(students)
db.students.remove({1013})
db.students.insert({
    1014: {
        "Player ID": 21
        "First Name": 'Gollum',
        "Last Name": 'Ring Stealer',
        "Team Name": ' Team Sauron',
    }
})
print(students)
db.students.remove({1014})
print(students)