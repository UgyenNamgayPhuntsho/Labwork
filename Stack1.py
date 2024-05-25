from queue import Queue

patient_queue = Queue()

def register_patient(patient_name):
    patient_queue.put(patient_name)
    print(f"{patient_name} has been registered.")

def remove_patient():
    if patient_queue.empty():
        print(f"Patient {patient_name} has met the Doctor.")
    else:
        removed_patient = patient_queue.get()
        print(f"{removed_patient} has meet the doctor.")

def display_queue():
    if patient_queue.empty():
        print(f"Patient {patient_name} has meet with the doctor")
    else:
        print("Current Patient Queue:")
        for idx, patient in enumerate(patient_queue.queue, start=1):
            print(f"{idx}. {patient}")

while True:
    print("\nDesk Manager - Patient Registration and Appointment")
    print("1. Register patient")
    print("2. Remove Patient after Meeting with Doctor")
    print("3. Patient Queue ")
    print("4. Exit")

    choice = input("Enter your choice: ")
    patient_name = input("Enter patient name: ")
    if choice == '1':
        register_patient(patient_name)
    elif choice == '2':
        remove_patient()
    elif choice == '3':
        display_queue()
    elif choice == '4':        
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

    