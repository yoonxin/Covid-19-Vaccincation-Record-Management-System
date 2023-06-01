#LEONG CHEE YIEN (student who submit)
#TP065210 (student who submit)
#KOH YOON XIN
#TP066186
#WONG ZHI YAO
#TP066907

import time
from datetime import date, timedelta, datetime


def name_validation():
    while True:
        name = input("Full name: ")
        if all(x.isalpha() or x.isspace() for x in name) and name != "":
            return name
        else:
            print("Invalid input.")


def contact_validation():
    while True:
        contact_num = (input("Contact number (symbol is not required): "))
        if contact_num.isnumeric and len(str(contact_num)) in range(10, 12) and contact_num[0:2] == "01":
            return contact_num
        else:
            print("Invalid input.")


def email_validation():
    while True:
        email = input("Email address (optional): ")
        if "@" in email and ".com" in email or email == "":
            return email
        else:
            print("Invalid input.")


def nric_validation():

    month = ["{:02}".format(i) for i in range(1, 13)]
    day = ["{:02}".format(i) for i in range(1, 32)]

    state = ["{:02}".format(i) for i in range(1, 17)]
    state_cont = ["{:02}".format(i) for i in range(21, 60)]
    state.extend(state_cont)

    while True:
        nric = input("NRIC: ")
        if nric.isnumeric() and len(str(nric)) == 12 and nric[2:4] in month and nric[4:6] in day and nric[6:8] in state:
            return nric
        else:
            print("Invalid NRIC.")


def age_validation():
    while True:
        try:
            age = int(input("Age: "))
            if age > 0:
                return age
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Enter a valid age. ")


def gender_validation():
    while True:
        gender = input("Gender (M - male & F - female): ").upper()
        if (gender == "M") or (gender == "F"):
            return gender
        else:
            print("Invalid input.")


def ethnicity_validation():
    print("Ethnicity: ")
    print("1. Malay\n2. Chinese\n3. Indian\n4. Others")
    while True:
        choice = input("Choose your ethnicity: ")
        if choice == '1':
            ethnicity = "Malay"
            break
        elif choice == '2':
            ethnicity = "Chinese"
            break
        elif choice == '3':
            ethnicity = "Indian"
            break
        elif choice == '4':
            ethnicity = input("Enter your ethnicity: ")
            break
        else:
            print("Invalid input. You only can choose 1 to 4.")
    return ethnicity


def vc_validation():
    while True:
        vc = input("Kindly choose your vaccination centre (VC1 / VC2): ").upper()
        if (vc == "VC1") or (vc == "VC2"):
            return vc
        else:
            print("Invalid input.")


def vaccine_validation(age):
    if age < 18:
        print("You are available for vaccine AF, CZ & DM.")
        while True:
            vaccine = input("Please choose your preferred vaccine: ").upper()
            if vaccine == "AF" or vaccine == "CZ" or vaccine == "DM":
                print("Your chosen vaccine is: ", vaccine, " (2 doses required)")
                break
            else:
                print("You only can choose AF, CZ or DM.")

    elif age > 45:
        print("You are available for vaccine AF, BV, DM & EC.")
        while True:
            vaccine = input("Please choose your preferred vaccine: ").upper()
            if vaccine == "AF" or vaccine == "BV" or vaccine == "DM":
                print("Your chosen vaccine is: ", vaccine, " (2 doses required)")
                break
            elif vaccine == "EC":
                print("Your chosen vaccine is: ", vaccine, " (Only 1 dose required)")
                break
            else:
                print("You only can choose AF, BV, DM or EC.")

    else:
        print("You are available for vaccine AF, BV, CZ, DM & EC.")
        while True:
            vaccine = input("Please choose your preferred vaccine: ").upper()
            if vaccine == "AF" or vaccine == "BV" or vaccine == "CZ" or vaccine == "DM":
                print("Your chosen vaccine is: ", vaccine, " (2 doses required)")
                break
            elif vaccine == "EC":
                print("Your chosen vaccine is: ", vaccine, " (Only 1 dose required)")
                break
            else:
                print("You only can choose AF, BV, CZ, DM or EC.")

    return vaccine


def get_details():
    patient_id = 1
    each_patient_record = []

    with open("patients.txt", "r") as file1:
        while True:
            s = file1.readline()
            if s == "":
                break
            else:
                patient_id = int(s.split(",")[0]) + 1

    print("Welcome to vaccine registration. \nPlease fill up your personal information as below:")

    name = name_validation()
    contact_num = contact_validation()
    email = email_validation()
    nric = nric_validation()
    age = age_validation()
    if age < 12:
        print("You can't get vaccinated at this moment due to under age. \n")
        time.sleep(1)
        return
    gender = gender_validation()
    ethnicity = ethnicity_validation()

    time.sleep(1)
    print("Thanks for your personal information given.")
    print("Your patient ID is: ", f"{patient_id:04}")

    vc = vc_validation()
    vaccine = vaccine_validation(age)

    each_patient_record.extend([f"{patient_id:04}", vc, vaccine, name, contact_num, email, nric, str(age), gender, ethnicity])

    with open("patients.txt", "a") as file1:

        file1.write(", ".join(each_patient_record) + "\n")

    print("Registered successfully. Welcome " + name + "\n")
    print("This page will back to main menu in 5 seconds. \n")
    time.sleep(5)
    return


def read_file(filename, patient_id):
    found = False
    with open(filename, "r") as file1:

        while True:
            line = file1.readline()
            line_list = line.split(", ")
            if patient_id == line_list[0]:
                found = True
                ret_list = line_list
            elif line == "":
                break

    if found:
        return ret_list
    else:
        return None


def vaccine_administration():
    while True:
        patient_id = input("Please enter your patient ID (X to exit): ").upper()

        patient_list = read_file("patients.txt", patient_id)
        if patient_list is not None:
            print("Hi!", patient_list[3])
            vaccine_check = patient_list[2]
            break
        elif patient_id == "X":
            print()
            return
        else:
            print("Patient ID is not found.")

    # check if input is in dose   EC:1, others:2
    dose = [1]

    if vaccine_check != "EC":
        dose.append(2)
    print("Vaccine chosen: ", patient_list[2], "(", str(dose[-1]), "doses required )")

    while True:
        try:
            dose_num = int(input("Please enter dose to be received (1 / 2): Dose "))
            if dose_num in dose:
                # check vaccination file for patient dose record, no record = d0

                vac_list = read_file("vaccination.txt", patient_id)

                if vac_list is not None:
                    vac_dose = int(vac_list[1][1])
                else:
                    vac_dose = 0

                if dose_num <= vac_dose:
                    print("Record already exists.\n")
                    time.sleep(3)
                    return
                elif dose_num - vac_dose > 1:
                    print("You need to get dose 1 first.")
                else:
                    break
            else:
                print("Doses available for", vaccine_check, "vaccine is dose", ', '.join(str(d) for d in dose))
        except ValueError:
            print("Please enter a number.")

    today = date.today()
    if dose_num == dose[-1]:
        if vac_list is not None:
            next_vacc_date = datetime.strptime(vac_list[3].rstrip("\n"), '%Y-%m-%d')
            if today < next_vacc_date.date():
                print("You cannot be vaccinated now, your dose is available after ", vac_list[3])
                time.sleep(3)
                return
        print("You can receive dose", dose_num, "now.")
        next_date = "-"
    else:
        if vaccine_check == "AF":
            day = 14
        elif vaccine_check == "DM":
            day = 28
        else:
            day = 21

        next_date = today + timedelta(days=day)
        print("You can receive dose 1 now.")
        print("Next recommended vaccination date for dose 2: ", next_date)

    # write file
    vaccine_record = [patient_id, "D" + str(dose_num), str(today), str(next_date)]

    with open("vaccination.txt", "a") as file2:
        file2.write(", ".join(vaccine_record) + "\n")

    print("This page will back to main menu in 5 seconds. \n")
    time.sleep(5)
    return


def search_patient():

    while True:
        patient_id = input("Please enter your patient ID (X to exit): ").upper()
        if patient_id == "X":
            print()
            return

        patient_list = read_file("patients.txt", patient_id)
        vacc_list = read_file("vaccination.txt", patient_id)

        #if id found, print patient information
        if patient_list is not None:
            print("\nPatient ID: ", patient_list[0])
            print("Full Name: ", patient_list[3])
            print("NRIC: ", patient_list[6])
            print("Age: ", patient_list[7])
            print("Gender: ", patient_list[8])
            print("Contact Number: ", patient_list[4])
            if patient_list[5] != "":
                print("Email: ", patient_list[5])
            print("Ethnicity: ", patient_list[9].rstrip("\n"))
            print("Vaccination Centre: ", patient_list[1])
            print("Vaccine Code: ", patient_list[2])
            if patient_list[2] == 'EC':
                print("Dosage Required: 1 \n")
            else:
                print("Dosage Required: 2 \n")
            if vacc_list is not None:
                dose_num = int(vacc_list[1][1])
            else:
                dose_num = 0
            if dose_num == 0:
                print("You have not been vaccinated yet.")
            else:
                if patient_list[2] != 'EC' and dose_num == 1:
                    print("You have completed Dose 1.")
                else:
                    print("You have been fully vaccinated.")

            input("Press enter key to proceed.\n")
            return

        else:
            print("The record is not found. \n")



def information_breakdown(vacc_vc):
    vc_full = 0
    vc_wait = 0

    #if it is - means fully vaccinated
    for z in vacc_vc:
        if z[3].rstrip("\n") == "-":
            vc_full += 1
        else:
            vc_wait += 1

    return [vc_wait, vc_full]



def statistical_information():
    patient_id_vc = []
    vacc_vc1 = []
    vacc_vc2 = []

    # read patient file
    with open("patients.txt", "r") as file1:
        patients = file1.readlines()

    # split into each patient id and vc
    for x in patients:
        patient_list = x.split(", ")
        patient_id_vc.append([patient_list[0], patient_list[1]])

    # organize each patient into vc
    for y in patient_id_vc:
        check_vacc = read_file("vaccination.txt", y[0])
        if check_vacc is not None:
            if y[1] == "VC1":
                vacc_vc1.append(check_vacc)
            else:
                vacc_vc2.append(check_vacc)

    vc1breakdown = information_breakdown(vacc_vc1)
    vc2breakdown = information_breakdown(vacc_vc2)

    print("Total number of patients vaccinated by VC1 is " + str(len(vacc_vc1)))
    print("Total number of patients who are waiting for dose 2 by VC1 is " + str(vc1breakdown[0]))
    print("Total number of patients who are fully vaccinated by VC1 is " + str(vc1breakdown[1]) + "\n")

    print("Total number of patients vaccinated by VC2 is " + str(len(vacc_vc2)))
    print("Total number of patients who are waiting for dose 2 by VC2 is " + str(vc2breakdown[0]))
    print("Total number of patients who are fully vaccinated by VC2 is " + str(vc2breakdown[1]) + "\n")

    print("This page will back to main menu in 5 seconds. \n")
    time.sleep(5)
    return



def modify(modify_patient):
    # if not yet vaccinated only can modify
    vacc_change = False
    while True:
        print("1. Name")
        print("2. Contact")
        print("3. NRIC")
        print("4. Vaccine Centre")
        check_vacc = read_file("vaccination.txt", modify_patient[0])
        if check_vacc is None:
            vacc_change = True
            print("5. Vaccine Code")

        choice = input("Select a data to modify (X to exit): ").upper()
        if choice == "1":
            modify_patient[3] = name_validation()
        elif choice == "2":
            modify_patient[4] = contact_validation()
        elif choice == "3":
            modify_patient[6] = nric_validation()
        elif choice == "4":
            modify_patient[1] = vc_validation()
        elif choice == "5" and vacc_change:
            modify_patient[2] = vaccine_validation(int(modify_patient[7]))
        elif choice == "X":
            break
        else:
            print("Please enter a valid input.")

    return modify_patient



def data_modification():
    patient_lists = []
    join_patient = ""

    with open("patients.txt", "r") as file1:
        patients = file1.readlines()

    for x in patients:
        patient_list = x.split(", ")
        patient_lists.append(patient_list)

    while True:
        patient_id = input("Please enter your patient id (X to exit): ").upper()
        if patient_id == "X":
            print()
            return

        check_patient = read_file("patients.txt", patient_id)

        # modify if id is found
        if check_patient is not None:
            # get index number of patient id in file
            print("Hi", check_patient[3], ", you may select details you wish to modify.")
            index_no = patient_lists.index(check_patient)

            # pass patient id information to be modified
            # replace the original data with modified data
            modified_patient_lists = patient_lists
            modified_patient_lists[index_no] = modify(patient_lists[index_no])

            # join to write to file
            for y in modified_patient_lists:
                new_patient_list = ", ".join(y)
                join_patient += new_patient_list

            with open("patients.txt", 'w') as file1:
                file1.write(join_patient)

            print("Your details have been modified.\n")
            time.sleep(3)
            return
        else:
            print("Invalid patient ID.")



def delete_patient():
    patient_lists = []
    join_patient = ""

    with open("patients.txt", "r") as file1:
        patients = file1.readlines()

    for x in patients:
        patient_list = x.split(", ")
        patient_lists.append(patient_list)

    while True:
        patient_id = input("Please enter your patient ID (X to exit): ").upper()
        if patient_id == "X":
            print()
            return

        check_patient = read_file("patients.txt", patient_id)

        if check_patient is not None:
            # check if this patient has been vaccinated by any VC
            check_vacc = read_file("vaccination.txt", patient_id)

            if check_vacc is None:
                for y in range(3):
                    #use NRIC as a verification
                    patient_nric = input("Please verify with your NRIC (X to exit): ").upper()

                    if patient_nric == check_patient[6]:
                        index_no = patient_lists.index(check_patient)
                        del patient_lists[index_no]
                        print("You have successfully deleted your record.\n")

                        # join to string and write to file
                        for z in patient_lists:
                            new_patient_list = ", ".join(z)
                            join_patient += new_patient_list

                        with open("patients.txt", 'w') as file1:
                            file1.write(join_patient)
                        return
                    elif patient_nric == "X":
                        break
                    else:
                        print("Your NRIC is incorrect. Chances Remaining: " + str(2-y) + "\n")
            else:
                print("You cannot delete your record as you have already been vaccinated by this VC.\n")
                return
        else:
            print("Invalid patient ID.\n")


# main menu
def main_menu():

    # create file if it doesn't exist
    patient_file = open("patients.txt", "a")
    patient_file.close()
    vaccination_file = open("vaccination.txt", "a")
    vaccination_file.close()

    while True:
        print("Thank you for downloading our vaccination app. \nWelcome to the main menu!")
        print("Your options are: ")
        print("1. Patient Registration \n2. Vaccine Administration \n3. Search Patient Record & Vaccination Status "
              "\n4. Statistical Information on Patients Vaccinated \n5. Modify Patient Record \n6. Delete Patient Record \n7. Exit ")

        while True:
            choice = input("Select your choice: ")
            if choice == '1':
                get_details()
                break

            elif choice == '2':
                vaccine_administration()
                break

            elif choice == '3':
                search_patient()
                break

            elif choice == '4':
                statistical_information()
                break

            elif choice == '5':
                data_modification()
                break

            elif choice == '6':
                delete_patient()
                break

            elif choice == '7':
                return

            else:
                print("Invalid choice.")

main_menu()
