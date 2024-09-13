import streamlit as st
import csv
import time 
import pandas as pd
import datetime
st.title("Study time recorder")

df = pd.read_csv("time_for_subject.csv")


# name of csv file
filename = "subjects_table.csv"
filename_time = "time_for_subject.csv"

# import matplotlib as mpl

# my data rows as dictionary objects
# mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
#           {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
#           {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
#           {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
#           {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
#           {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]




# add new subject into csv file 
new_subject = st.text_input("Add a new subject")
if st.button("Add subject"):
    mydict = [{'Subject': new_subject}]
    # field names
    fields = ['Subject']
        # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)


        # writing data rows
        writer.writerows(mydict)
        






subjects = []



with open(filename, mode ='r') as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        for line in lines:
        

            subjects.append(line)

            # print(line)



subjects.remove("subject")



# choosing_subject
# subject = st.selectbox(
#     "Which subject do you want to study now?", subjects)








end_time = 0




# with open('time_for_subject.csv', mode ='r') as file:
#     csvFile = csv.reader(file)
    
    
    
#     for row in csvFile:

#         cur_subject = row[-1]
#         cur_start_time = row[0]
#         if cur_subject == subject:
#             time_used = end_time - start_time

#             print("--------------",time_used)


# # my_dict = [{"end_time": end_time}]
# my_dict = [{"start_time": start_time,"end_time": end_time,"expected_time": expected_time,"subject": subject}]

# time_used = end_time - start_time
# print(time_used)

fields_end_time = ["end_time"]
with open(filename_time, 'a') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields_end_time)


    # writing data rows
    
    # writer.writerows(my_dict)



for subject in subjects:
    
    # st.text(subject)
    with st.expander(subject):
        # expacted_time_button
        expected_time = st.number_input(f"Time you want to spend for studying {subject} (minutes)")

        if len(df[df["subject"]==subject]) > 0 and float(df[df["subject"]==subject]["end_time"].iloc[-1]) == float(0):
            df.loc[df['subject'] == subject].index[-1]

            last_index = df.loc[df['subject'] == subject].index[-1]

            # Update the 'end_time' of the last row meeting the condition to the current time
            start_time = datetime.datetime.fromtimestamp(df.loc[last_index, "start_time"])
            expected_time = df.loc[last_index, "expected_time"]





            st.text(f"You started at {start_time} and your expected time for studying is {expected_time} min")




        # start_button
        if st.button(f"Start {subject}"):

            if expected_time <= 0:
                st.warning("Please choose a study time that is > 0")

            else:

                # load data frame
                df = pd.read_csv("time_for_subject.csv")

                # print("-----------", df[df["subject"]==subject]["end_time"])


                # chevk if subject already exist
                if len(df[df["subject"]==subject]) > 0 and float(df[df["subject"]==subject]["end_time"].iloc[-1]) == float(0):
                    # if exists st.warning CANNOT ADD SAME TASK NAME
                    st.warning("Please press end button if u want to start a new task")

                # else add it
                else:


                    start_time = time.time()
                    my_dict = [{"start_time": start_time,"end_time": end_time,"expected_time": expected_time,"subject": subject}]
                    
                    fields_start_time = ["start_time","end_time","expected_time","subject"]
                    with open(filename_time, 'a') as csvfile:
                        # creating a csv dict writer object
                        writer = csv.DictWriter(csvfile, fieldnames=fields_start_time)


                        # writing data rows
                        writer.writerows(my_dict)
                        


        # end_button
        if st.button(f"End {subject}"):
            end_time = time.time()

            last_index = df.loc[df['subject'] == subject].index[-1]

            # Update the 'end_time' of the last row meeting the condition to the current time
            df.loc[last_index, 'end_time'] = end_time
            
            df.to_csv('time_for_subject.csv', index = False)

            
