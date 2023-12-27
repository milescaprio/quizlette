from lib import *
fn = "spanish1_family_1"

print("All answers and questions are masculine")

questions = Game([], fn)
questions.worst_hole = -1
questions.repeat_probability = lambda s, r : 0.5

questions.add(Question.FRQ("grandpa"            ,"el abuelo"              ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("friend"             ,"el amigo"               ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("last name"          ,"el apellido"            ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("artist"             ,"la artista"             ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("great grandpa"      ,"el bisabuelo"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("brother in law"     ,"el cuñado"              ,filtered_equals(nest(stripped, lowercased, accents_removed)), end_hint=" remember the ñ"))
questions.add(Question.FRQ("doctor (version 1)" ,"el doctor"              ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("doctor (version 2)" ,"el médico"              ,filtered_equals(nest(stripped, lowercased, accents_removed)), end_hint=" remember the é"))
questions.add(Question.FRQ("spouse"             ,"el esposo"              ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("family"             ,"la familia"             ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("twin"               ,"el gemelo"              ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("people"             ,"la gente"               ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("stepbrother"        ,"el hermanastro"         ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("brother"            ,"el hermano"             ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("stepson"            ,"el hijastro"            ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("son"                ,"el hijo"                ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("children"           ,"los hijos"              ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("engineer"           ,"el ingeniero"           ,filtered_equals(nest(stripped, lowercased))))                           

questions.run()