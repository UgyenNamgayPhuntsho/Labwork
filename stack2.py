from queue import Queue
patient_queue= Queue()

while True:
    print("\nDesk Manager - Patient Registration and Appointment")
    print("1. Register patient")
    print("2. Remove Patient after Meeting with Doctor")
    print("3. Patient Queue ")
    print("4. Exist")

def register_patient(self, patient_name):
        self.patient_queue.put(patient_name)
        print(f"{patient_name} has been registered.")

def remove_patient(self):
        if self.patient_queue.empty():
            print("Queue is empty.")
        else:
            removed_patient = self.patient_queue.get()
            print(f"{removed_patient} has seen the doctor.")

def display_queue(self):
        if self.patient_queue.empty():
            print("Queue is empty.")
        else:
            print("Current Patient Queue:")
            for idx, patient in enumerate(self.patient_queue.queue, start=1):
                print(f"{idx}. {patient}")

choice = input("Enter your choice: ")

if choice == '1':
    patient_name = input("Enter patient name: ")
    desk_manager.register_patient(patient_name)
elif choice == '2':
    desk_manager.remove_patient()
elif choice == '3':
    desk_manager.display_queue()
elif choice == '4':        
    print("Exiting program.")
    break
else:
        print("Invalid choice. Please enter a valid option.")