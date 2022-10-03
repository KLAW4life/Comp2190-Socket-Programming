import random

AgentA_codes = []
AgentB_codes = []

predefined = ["AJK78", "KTV90", "NEL55", "DFG28"]

AgentA = "2975"
AgentB = "6144"

# Write code that will Generate all possible connection codes for the Agents and store them in their respective arrays. 
for pre in predefined:
    AgentA_codes.append(pre+AgentA)
    AgentB_codes.append(pre+AgentB)


questions = [("I saw a purple Kangaroo yesterday, did you?", "Only after the sun went down"),
             ("What did Eve say when she ate the fruit?", "Nothing"),
             ("What do you call a fish wearing a bowtie?", "Sofishticated"),
             ("What did the ocean say to the beach?", "Nothing it just waved"),
             ("Why did God save men but not fallen angels?", "Good Question")]

#This function should return a random instance from the questions array. 
def getSecretQuestion():
    ran_q = random.choice(questions)
    return(ran_q)

#This function checks the answer to the question goven by the client
def getSecretAnswer(question,answer):
    q_ans = question[-1]
    if answer == q_ans:
        return (True)
    else:
        return(False)

#This function must check the connection code given by the client (Agent) and return the name of the Agent (Agent A or B). 
# If the code is invalid the function should return -1.
def check_conn_codes(connCode):
    found = -1
    for i in AgentA_codes:
        if connCode == i:
            found = 1
    for j in AgentB_codes:
      if connCode == j:
        found = 2

    if found == 1:
      return("Agent A")
    elif found == 2:
      return("Agent B")
    else:
      return(found)
    


    
