from lib import *

questions = []
questions.append(Question("HCIO4"   ,  "perchloric acid"      , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("HCl"     ,  "hydrochloric acid"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("HBr"     ,  "hydrobromic acid"     , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("HI"      ,  "hydroiodic acid"      , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("HNO3"    ,  "nitric acid"          , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("H2SO4"   ,  "sulfuric acid"        , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("LiOH"    ,  "lithium hydroxide"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("NaOH"    ,  "sodium hydroxide"     , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("KOH"     ,  "potassium hydroxide"  , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("Ca(OH)2" ,  "calcium hydroxide"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("Sr(OH)2" ,  "strontium hydroxide"  , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("Ba(OH)2" ,  "barium hydroxide"     , QuestionType.FRQ, nest(stripped, lowercased)))


questions.append(Question("perchloric acid"       , "HCIO4"   , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("hydrochloric acid"     , "HCl"     , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("hydrobromic acid"      , "HBr"     , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("hydroiodic acid"       , "HI"      , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("nitric acid"           , "HNO3"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("sulfuric acid"         , "H2SO4"   , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("lithium hydroxide"     , "LiOH"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("sodium hydroxide"      , "NaOH"    , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("potassium hydroxide"   , "KOH"     , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("calcium hydroxide"     , "Ca(OH)2" , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("strontium hydroxide"   , "Sr(OH)2" , QuestionType.FRQ, nest(stripped, lowercased)))
questions.append(Question("barium hydroxide"      , "Ba(OH)2" , QuestionType.FRQ, nest(stripped, lowercased)))


run_game(questions)