from lib import *
fn = "apspanish_unit2"

print("Answer all questions in the masculine form if both are possible.")
questions = Game([], fn)
questions.worst_hole = -1
questions.repeat_probability = lambda a, b : 1.0  

questions.add(Question.FRQ("heritage"             ,       "el acervo",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("town"                 ,       "la aldea",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("area"                 ,       "el ámbito",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("threat"               ,       "la amenaza",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("approval"             ,       "aprobación",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("assimilation"         ,       "la asimilación",            filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("subject/matter/issue" ,       "el asunto",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("lack"                 ,       "la carencia",               filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("social class"         ,       "la  clase socioeconómica",  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("behavior"             ,       "el comportamiento",         filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("coexistence"          ,       "la convivencia",            filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("right"                ,       "el derecho",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("alienation"           ,       "la enajenación",            filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("ethnicity"            ,       "la etnicidad",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("stranger"             ,       "el forastero",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("foreigner"            ,       "el extranjero",             filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("gender"               ,       "el género",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("native"               ,       "la indígena",               filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("heritage/assets"      ,       "el patrimonio",             filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("role"                 ,       "el papel",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("diversity"            ,       "la pluridad",               filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("prejudice"            ,       "el prejuicio",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("race"                 ,       "la raza",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("resources"            ,       "los recursos",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("risk"                 ,       "el riesgo",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("temp worker"          ,       "el temporero",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("xenophobia"           ,       "la xenofobia",              filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to accept"            ,       "acoger",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("adapt"                ,       "adaptarse",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to threaten"          ,       "amenazar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to lack"              ,       "carecer de",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to hunt"              ,       "cazar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to develop"           ,       "desarollar",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to arise/come from"   ,       "emanar",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to enrich"            ,       "enriquecer",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to promote (alt),"    ,       "fomentar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to enjoy"             ,       "gozar",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to inherit"           ,       "heredar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to flee"              ,       "huir",                      filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to manage"            ,       "lograr",                    filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to promote"           ,       "promover",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to reject"            ,       "rechazar",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to recognize"         ,       "reconocer",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to endure"            ,       "sobrellevar",               filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to tend  to"          ,       "soler",                     filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("to overcome"          ,       "superar",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("literate"             ,       "alfabeto",                  filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("isolated"             ,       "aislado",                   filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("illiterate"           ,       "analfabeto",                filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("daily"                ,       "cotidiano",                 filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("outstanding"          ,       "destacado",                 filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("hidden"               ,       "escondido",                 filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("deep"                 ,       "hondo",                     filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("shy"                  ,       "huraño",                    filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("retired"              ,       "jubilado",                  filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("latin descent"        ,       "latinx",                    filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("located"              ,       "ubicado",                   filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("despite"              ,       "a pesar de",                filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("still"                ,       "aún",                       filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("although"             ,       "aunque",                    filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("reject/ignore"        ,       "darle la espalda",          filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("in any case"          ,       "de todos modos",            filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("he likes"             ,       "le cae bien",               filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("i like"               ,       "me cae bien",               filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("to get along with"    ,       "llevarse bien con",         filtered_equals(nest(stripped, lowercased)))) 
questions.add(Question.FRQ("by accident"          ,       "por casualidad",            filtered_equals(nest(stripped, lowercased)))) 
questions.run()

#errors 
#darle la epalda
#por 