questions = [" Whats the time speed?"," Whats the Medicine Symboll?"," Whats the Ceaser code?"," Who was Alan turing?"];
answers = (("a) 300,000 km/h", "b) 1,080,000 km/h", "c) 299,792,458 m/s","d) 150,000 m/s"),
          ("a) Caduceus (staff with two snakes and wings)","b) Rod of Asclepius (staff with one snake)", "c) Maltese Cross ","d) Cup of Hippocrates"),
          ("a) A substitution cipher that shifts the letters of the alphabet ","b) A mathematical code used by Julius Caesar for accounting", "c) A data compression method ","d) A genetic code related to Caesar's lineage"),
          ("a) A British mathematician who helped decode Nazi codes in World War II," "b) A physicist who formulated the theory of relativity","c) A Greek philosopher known for his Aristotelian logic","d) An engineer responsible for the invention of the radio"),)
alter = 0; n = 0; score = 0; guesses = []; Rguesses = ["C","B","A","A"]
 
for question in questions:
    print("------------------------------")
    print(question)
    for answear in answers[alter]:
        print(answear)
        
    guess = guesses.append(input("A,B,C or D: "))
    alter+=1

while n < len(guesses):
    if guesses[n] == Rguesses[n]:
        print(f"{n+1}.{guesses[n]}) is Right ✅")
        score+= 250
    else:
        print(f"{n+1}.{guesses[n]}) is Wrong ❌")
        score-=100
    n+=1
print(f"Your final score is: {score} Points")
