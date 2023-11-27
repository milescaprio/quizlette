from lib import *
fn = "spanish1_verbs"

questions = Game([], fn)
questions.worst_hole = -1
questions.repeat_probability = lambda s, r : 0.5

questions.add(Question.FRQ("to dance"               ,"bailar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to look for"            ,"buscar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to walk"                ,"caminar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to sing"                ,"cantar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to have dinner"         ,"cenar",                      filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to buy"                 ,"comprar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to answer"              ,"contestar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to chat"                ,"conversar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to have breakfast"      ,"desayunar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to rest"                ,"descansar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to wish"                ,"desear",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to draw"                ,"dibujar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to teach"               ,"ensenar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to listen to music"     ,"escuchar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to wait for/hope"       ,"esperar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to study"               ,"estudiar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to explain"             ,"explicar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to talk"                ,"hablar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to arrive"              ,"llegar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to carry/wear"          ,"llevar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to look at/watch"       ,"mirar",                      filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to need"                ,"necesitar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to practice"            ,"practicar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to ask"                 ,"preguntar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to prepare"             ,"preparar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to return"              ,"regresar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to end/finish"          ,"terminar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to take/drink"          ,"tomar",                      filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to work"                ,"trabajar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to travel"              ,"viajar",                     filtered_equals(nest(stripped, lowercased))))

questions.run()