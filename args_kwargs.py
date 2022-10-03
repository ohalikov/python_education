# *args и **kwargs

def printStudentScores(student, *scores):
    print(f"Hi, {student}, you scores:")
    for score in scores:
        print('\n score = ', score)


def printPetNames(owner, **pets):
    print(f"Owner name = {owner}")
    for pet, name in pets.values():
        print(f": {name}")


# printStudentScores("Leos", 10, 30, 50, 150, 20)

# printPetNames("Leos2", dog="Brook", fish=[
#               'Lary', 'Clart', 'Den'], turtle="Sheldon")

dialog_state = {}

id_record = "p5pdf32koff3k43k["
patient_fullname = "Иванов Иван Иванович"
id_patient = "v3b4sas3g3g3-032kwk"
mo_name = "Областная больница № 2"
mo_address = 'ул.50 лет октября 38'
medical_specialty = "хирург"
visit_date = "2022-03-22T20:30:00"
project = "mfc72"
datetime_recall = "2022-03-25T20:30:00"

data_obj = {
    "id_record": id_record,
    "patient_fullname": patient_fullname,
    "id_patient": id_patient,
    "mo_name": mo_name,
    "mo_address": mo_address,
    "medical_specialty": medical_specialty,
    "visit_date": visit_date,
    "project": project,  # если в NCC, будет несколько проектов 
    "datetime_recall": datetime_recall
}
# print(data_obj)
def get_filled_dialog_state(**data_obj):
    for key, value in data_obj.items():
        dialog_state[key] = value
        # print(dialog_state[key])
    

get_filled_dialog_state(**data_obj)
print(dialog_state)