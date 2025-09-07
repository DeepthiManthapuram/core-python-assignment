class HospitalPatientManagement:

    def __init__(self,patients):
        self.patients = patients
    
    #Function to search the person with the specified disease
    def searchDisease(self,disease):
        diseased_patients = []
        for patient in self.patients:
            if(patient["Disease"] == disease):
                diseased_patients.append(patient["Name"])
        
        return diseased_patients


patients_list = eval(input("patients = "))      #converting input into list
disease = input("search_disease = ")
 
hospital_obj = HospitalPatientManagement(patients_list)
print(hospital_obj.searchDisease(disease))      #displaying patient names with disease