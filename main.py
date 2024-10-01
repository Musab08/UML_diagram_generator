from flask import Flask, request
import google.generativeai as genai
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, Response
from plantuml import PlantUML
from dotenv import load_dotenv
import os
import io

load_dotenv()  # Load environment variables from .env file


app = Flask(__name__)

PLANTUML_URL = os.getenv("PLANTUML_URL")
API_KEY = os.getenv("API_KEY")


plantuml = PlantUML(PLANTUML_URL)


genai.configure(api_key=API_KEY)
Model_Name="gemini-pro"
model=genai.GenerativeModel(Model_Name)


def generate_uml_code(prompt, option):
    if option == "Activity diagram":
        response = model.generate_content(f"""
                                            As an experienced software engineer, systems analyst, business analyst, or UML Activity diagram designer,\n
                                            your task is to create a detailed and error-free UML Activity diagram using PlantUML code.\n
                                            The diagram should encompass all necessary entities, attributes, methods \n
                                            and relationships as specified in the provided prompt, which will be delimited by angle bracket <>.\n

                                            Start your code with '@startuml' and end it with '@enduml'.\n
                                            Please ensure that your PlantUML code is correctly formatted and follows the proper syntax guidelines.\n
                                            Double-check for any missing or mismatched brackets, parentheses, or other symbols. \n
                                            Verify that you're using the appropriate keywords and modifiers for elements and relationships.\n
                                            Additionally, ensure that your code does not contain any typographical errors or misspellings.\n
                                            Finally, confirm that you're not using any unsupported features or syntax. \n
                                            Reviewing your code with attention to these details should help ensure it is error-free.

                                            not use comment in code.

                                            it is example code of plantUML Activity Diagram for

                                            @startuml
                                            start
                                            :Login;
                                            if (Login successful?) then (yes)
                                                :Show main menu;
                                                repeat
                                                :Select option;
                                                if (Option = "Add Student") then
                                                    :Add student details;
                                                    :Update database;
                                                else if (Option = "Edit Student") then
                                                    :Select student;
                                                    :Edit student details;
                                                    :Update database;
                                                else if (Option = "Delete Student") then
                                                    :Select student;
                                                    :Delete student details;
                                                    :Update database;
                                                else if (Option = "View Student") then
                                                    :Select student;
                                                    :Display student details;
                                                else if (Option = "View All Students") then
                                                    :Retrieve all students;
                                                    :Display all student details;
                                                else if (Option = "Exit") then
                                                    :Logout;
                                                    :End;
                                                else
                                                    :Invalid option;
                                                endif
                                                repeat while (Option != "Exit")
                                            else (no)
                                                :Show error message;
                                                :Retry login;
                                            endif
                                            stop
                                            @enduml

                                            Create a activity diagram following the syntax . \n
                                            If there are any errors or missing steps, start over from the beginning and continue \n
                                            until the code is completely error-free and completed.
                                            """ + f"< {prompt} >")

        return response.text
    
    elif option == "Sequence diagram":
        response = model.generate_content(f"""
                                            As an experienced software engineer, systems analyst, business analyst, or UML Sequence diagram designer,\n
                                            your task is to create a detailed and error-free UML Sequence diagram using PlantUML code.\n
                                            The diagram should encompass all necessary entities, attributes, methods \n
                                            and relationships as specified in the provided prompt, which will be delimited by angle bracket <>.\n

                                            Start your code with '@startuml' and end it with '@enduml'.\n
                                            Please ensure that your PlantUML code is correctly formatted and follows the proper syntax guidelines.\n
                                            Double-check for any missing or mismatched brackets, parentheses, or other symbols. \n
                                            Verify that you're using the appropriate keywords and modifiers for elements and relationships.\n
                                            Additionally, ensure that your code does not contain any typographical errors or misspellings.\n
                                            Finally, confirm that you're not using any unsupported features or syntax. \n
                                            Reviewing your code with attention to these details should help ensure it is error-free.

                                            not use comment in code.

                                            it is example code of plantUML Sequence Diagram for

                                            @startuml
                                            actor User
                                            participant "Web Application" as App
                                            participant "Database" as DB

                                            User -> App : Login
                                            App -> DB : Validate User
                                            DB --> App : User Validated
                                            App --> User : Display Dashboard
                                            @enduml

                                            Create a sequence diagram following the syntax. \n
                                            If there are any errors or missing steps, start over from the beginning and continue \n
                                            until the code is completely error-free and completed.
                                            """ + f"< {prompt} >")

        return response.text

    elif option == "Use case diagram":
        response = model.generate_content(f"""
                                            As an experienced software engineer, systems analyst, business analyst, or UML Use Case diagram designer,\n
                                            your task is to create a detailed and error-free UML Use Case diagram using PlantUML code.\n
                                            The diagram should encompass all necessary entities, attributes, methods \n
                                            and relationships as specified in the provided prompt, which will be delimited by angle bracket <>.\n

                                            Start your code with '@startuml' and end it with '@enduml'.\n
                                            Please ensure that your PlantUML code is correctly formatted and follows the proper syntax guidelines.\n
                                            Double-check for any missing or mismatched brackets, parentheses, or other symbols. \n
                                            Verify that you're using the appropriate keywords and modifiers for elements and relationships.\n
                                            Additionally, ensure that your code does not contain any typographical errors or misspellings.\n
                                            Finally, confirm that you're not using any unsupported features or syntax. \n
                                            Reviewing your code with attention to these details should help ensure it is error-free.

                                            not use comment in code.

                                            it is example code of plantUML Use Case Diagram for

                                            @startuml
                                            actor User
                                            usecase "Login" as UC1
                                            usecase "View Dashboard" as UC2
                                            usecase "Manage Account" as UC3

                                            User --> UC1
                                            User --> UC2
                                            User --> UC3
                                            @enduml

                                            Create a use case diagram following the syntax. \n
                                            If there are any errors or missing steps, start over from the beginning and continue \n
                                            until the code is completely error-free and completed.
                                            """ + f"< {prompt} >")

        return response.text


    elif option == "Component diagram":
        pass  # Implement logic for component diagrams if needed
    elif option == "Deployment diagram":
        response = model.generate_content(f"""
                                            As an experienced software engineer, systems analyst, business analyst, or UML Deployment diagram designer,\n
                                            your task is to create a detailed and error-free UML Deployment diagram using PlantUML code.\n
                                            The diagram should encompass all necessary entities, attributes, methods \n
                                            and relationships as specified in the provided prompt, which will be delimited by angle bracket <>'.\n

                                            Start your code with '@startuml' and end it with '@enduml'.\n
                                            Please ensure that your PlantUML code is correctly formatted and follows the proper syntax guidelines.\n
                                             Double-check for any missing or mismatched brackets, parentheses, or other symbols. \n
                                             Verify that you're using the appropriate keywords and modifiers for elements and relationships.\n
                                            Additionally, ensure that your code does not contain any typographical errors or misspellings.\n
                                            Finally, confirm that you're not using any unsupported features or syntax. \n
                                            Reviewing your code with attention to these details should help ensure it is error-free.

                                            not use comment in code.

                                            it is example code of plantUML Deployment Diagram for

                                            @startuml
                                            !define ICONURL https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/v2.1.0
                                            !include ICONURL/common.puml

                                            skinparam componentStyle uml2

                                            actor User
                                            node "Client Application" as ClientApp {{
                                              [User Interface] as UI
                                            }}

                                            node "Server" as Server {{
                                              [Web Server] as WebServer
                                              [Application Server] as AppServer
                                              [Database] as DB
                                            }}

                                            database "External Services" as ExternalService {{
                                              [Library API]
                                            }}

                                            User --> UI
                                            UI --> WebServer : HTTP Request
                                            WebServer --> AppServer : Request
                                            AppServer --> DB : Database Query
                                            AppServer --> ExternalService : API Request
                                            DB --> AppServer : Database Response
                                            ExternalService --> AppServer : API Response
                                            AppServer --> WebServer : Response
                                            WebServer --> UI : HTTP Response
                                            UI --> User

                                            @enduml

                                            Create a deployment diagram following the syntax . \n
                                            If there are any errors or missing steps, start over from the beginning and continue \n
                                            until the code is completely error-free and completed.
                                            """ + f"< {prompt} >")

        return response.text

    elif option == "State diagram":
        guide_prompt = """
        Your role is to create a UML State diagram code for plantUML.
        you are an experienced software engineer, a systems analyst, a business analyst, or a UML State diagram designer .
        Your task is to create a plantUML code for comprehensive and detailed UML State diagram including all possible entities, attributes, methods, and relationships for the prompt delimited by ###.
        the generated plantUML code must follow the syntax and structure of plantUML code. ensure that there is no syntax and logical error because response provided will be forward to another api if error exists then api will crash.
        Follow all the theoretical and standard concepts required/Compulsory for making UML State diagram.
        Analyze the Example 1, having prompt with a detailed solution and steps for finding a detailed solution.
        plantUML State diagram code will start from @startuml and will end on @enduml

        you must follow the following steps to create a best and full uml code for comprehensive UML State diagram.
        perform all these steps one by one.
        /// Steps for creating UML State diagram:

        Step 1: Identify System Entities: Understand the system you're modeling and identify the entities (objects or components) that will be represented in the state diagram.

        Step 2: Identify States: Determine the possible states that each entity can be in during its lifecycle. These states should represent different conditions or situations of the entity.

        Step 3: Define Transitions: Identify the events or conditions that cause transitions between states. Define these transitions with appropriate triggers and actions. This could involve actions performed by the system or external stimuli.

        Step 4: Draw Initial State: Start by drawing the initial state of each entity. This is the state in which the entity exists when the system starts or when it is created.

        Step 5: Draw States: Draw each identified state as a rounded rectangle with the state name inside. These states should represent the different conditions or modes of the entity.

        Step 6: Draw Transitions: Draw arrows between states to represent transitions. Label each transition with the event or condition that triggers it. You may also include guards or conditions that must be satisfied for the transition to occur.

        Step 7: Add Actions: Optionally, you can include actions or activities associated with transitions. These actions represent what happens when a transition occurs, such as changing internal variables or sending messages.

        Step 8: Add Final State (Optional): If applicable, add final states to represent the end of the lifecycle of an entity. Final states are typically depicted as circles with a dot inside.

        Step 9: Review and Refine: Review the diagram to ensure that it accurately represents the system's behavior. Refine as necessary to improve clarity and completeness.

        Step 10: Validate: Validate the diagram with stakeholders or domain experts to ensure that it accurately captures the system's behavior and meets their requirements.

        Step 11: Document: Document the state diagram, including any assumptions made, in a clear and understandable manner. This documentation will help stakeholders understand the system's behavior as represented by the diagram.

        Step 12: Update as Needed: As the system evolves or new requirements emerge, update the state diagram to reflect these changes. Keeping the diagram up-to-date ensures that it remains a valuable tool for understanding the system's behavior.
        -> the diagram must fulfill the requirement of the plantUML State diagram code and also follow the latest rule for making uml State diagram.
        -> respond with the plantUML code.
        -> wait and compare the diagram with the plantUML State diagram syntax if it is not go to step 1 and repeat the process to generate plantUML State diagram again

        Example 1 ( UML State diagram for an online English tutor system ):
            prompt : UML State diagram for an online English tutor system.

        Steps of solution :

        Step 1: Identify System Entities

        System Users (Students, Tutors)
        Sessions
        Learning Materials
        Step 2: Identify States

        Student: Idle, Logged In, In Session
        Tutor: Idle, Logged In, In Session
        Session: Scheduled, In Progress, Completed
        Step 3: Define Transitions

        1. Idle -> Logged In (for both Student and Tutor)
        2. Logged In -> In Session (for both)
        3. In Session -> Completed
        Step 4: Draw Initial State

        Initial state is Idle for both Student and Tutor.

        Step 5: Draw States

        States: Idle, Logged In, In Session, Scheduled, In Progress, Completed, Available, Selected.

        Step 6: Draw Transitions

        Transitions would be: Idle -> Logged In (for both Student and Tutor), Logged In -> In Session (for both), In Session -> Completed.

        Step 7: Add Actions

        Actions can be added for transitions such as notifying the tutor when a student logs in, or sending reminders for scheduled sessions.

        Step 8: Add Final State

        Final state can be represented for the session as Completed.

        UML State Diagram Code:

        @startuml
        [*] --> Idle
        Idle --> Logged In : Student Login
        Idle --> Logged In : Tutor Login
        Logged In --> In Session : Start Session
        In Session --> [*] : End Session
        In Session --> Completed
        @enduml

        Step 9: Review and Refine

        Review the diagram with stakeholders for any missing states or transitions.

        Step 10: Validate

        Validate with the stakeholders to ensure completeness.

        Step 11: Document

        Document the assumptions made while creating the diagram.

        Step 12: Update as Needed

        Keep updating the diagram with changes in requirements.
        """ + f"< {prompt} >"

        response = model.generate_content(guide_prompt)

        return response.text
    


@app.route("/uml", methods=["POST"])
def uml():
    prompt = request.json["prompt"]
    option = request.json["option"]
    
    # Call the function to generate UML code
    uml_code = generate_uml_code(prompt, option)
    
    # Generate the image from the UML code
    try:
        image = plantuml.processes(uml_code)
    except Exception as e:
        print(f"Error generating UML: {str(e)}")  # Log the error
        return {"error": "Syntax error in UML code!"}

    img_io = io.BytesIO(image)
    img_io.seek(0)

    response = Response(img_io.getvalue(), mimetype='image/png')
    response.headers['Content-Disposition'] = 'attachment; filename=diagram.png'
    return response

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)