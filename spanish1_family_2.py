from lib import *
fn = "spanish1_family_2"

print("All answers and questions are masculine")
print("Questions with * do not directly swap to a feminine form")
questions = Game([], fn)
questions.worst_hole = -1
questions.repeat_probability = lambda s, r : 0.5


questions.add(Question.FRQ("stepdad*"           ,"el padrastro"       ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("stepmom*"           ,"la madrastra"       ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("mom"                ,"la madrea"          ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("halfbrother"        ,"el medio hermano"   ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("boy"                ,"el muchacho"        ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("child"              ,"el niño"            ,filtered_equals(nest(stripped, lowercased, accents_removed)), end_hint=" remember the ñ"))
questions.add(Question.FRQ("boyfriend"          ,"el novio"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("daughterinlaw*"     ,"la nuera"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("soninlaw*"          ,"el yerno"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("dad"                ,"el padre"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("parents"            ,"los padres"         ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("relatives"          ,"los parientes"      ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("journalist"         ,"el periodisto"      ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("cousin"             ,"el primo"           ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("programmer"         ,"el programador"     ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("nephew"             ,"el sobrino"         ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("dadinlaw"           ,"el suegro"          ,filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("uncle"              ,"el tío"             ,filtered_equals(nest(stripped, lowercased, accents_removed)), end_hint=" remember the í"))

questions.run()