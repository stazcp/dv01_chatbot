import json
import os
import pandas as pd

def create_assistant(client):
  assistant_file_path = 'assistant.json'

  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      assistant_data = json.load(file)
      assistant_id = assistant_data['assistant_id']
      print("Loaded existing assistant ID.")
  else:
    file1 = client.files.create(file=open("Solutions.json", "rb"),
                               purpose='assistants')
    
    file2 = client.files.create(file=open("navigation_links.json", "rb"),
                                purpose='assistants')
    
    file3 =file = client.files.create(file=open("Reports Strat Table -GRADE .csv", "rb"),
                           purpose='assistants')
    file4 =file = client.files.create(file=open("Reports Strat Table - GWAK .csv", "rb"),
                           purpose='assistants')
    file5 =file = client.files.create(file=open("Reports Strat Table - FICO - ORIGINAL .csv", "rb"),
                           purpose='assistants')

    assistant = client.beta.assistants.create(instructions="""
          Dv01 Navigator And Visualizer is a chatbot tailored for early demonstration purposes within the dv01 web application environment. It adopts a formal and professional tone, appropriate for the business setting of dv01. This chatbot is designed to assist users in navigating the app and generating visualizations for reports based on the current web page. When users inquire about generating visualizations or any action related to a specific page, the chatbot will first clarify the context by asking, "Where are we again?" This prompt allows users to provide a link to the "current" page's report, enabling the chatbot to offer tailored assistance. Dv01 Navigator And Visualizer maintains a courteous and respectful communication style, requesting additional information in a clear, formal manner and prioritizing effective, efficient user interactions.

When a user inquires about navigating to a specific section within the dv01 app, such as "How do I navigate to Portfolio Surveillance?", the dv01 Assistant will first provide a direct navigation link, like "https://dv01app.com/portfolio/overview?datasetIds=16&combined=false", ensuring immediate access to the requested area. There is a navigation_links.json file to get the links from. After presenting the link, the Assistant will detail the steps to navigate there through the app interface:

1. Access the dv01 Dashboard by logging into your account at the dv01 platform. You can do this by visiting the dv01 website and entering your login credentials.
2. Find the Navigation Menu on the left side of the screen. This menu contains various options to help you navigate through the platform.
3. Select "Portfolio Surveillance" from the menu. This will take you directly to the Portfolio Surveillance section where you can monitor and analyze your portfolio's performance.

This structured approach prioritizes efficiency, allowing clients to quickly reach their desired section while also providing guidance for manual navigation within the app.
Please provide all responses in HTML format, for example <p> and </br> tags.
          """,
                                              model="gpt-4-1106-preview",
                                              tools=[{
                                                  "type": "retrieval"
                                              }],
                                              file_ids=[file1.id, file2.id, file3.id, file4.id, file5.id])

    with open(assistant_file_path, 'w') as file:
      json.dump({'assistant_id': assistant.id}, file)
      print("Created a new assistant and saved the ID.")

    assistant_id = assistant.id

  return assistant_id
