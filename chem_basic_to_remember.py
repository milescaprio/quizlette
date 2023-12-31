## Edit this file to edit your quizlet.
## Make your own with the same format!

from lib import *
fn = "chem_basic_to_remember"

questions = Game([], fn)

questions.add(Question.MCQ("Ammonium"      ,  "NH4+1"       ,  ["NH4-1"], answer_count=2             ))
questions.add(Question.MCQ("Hydronium"     ,  "H3O+1"       ,  ["H3O-1", "OH-1", "OH+1"]             ))
questions.add(Question.MCQ("Hydroxide"     ,  "OH-1"        ,  ["OH+1", "H3O+1", "H3O-1"]            ))
questions.add(Question.MCQ("Nitrate"       ,  "NO3-1"       ,  ["NO3+1", "NO3-2", "NO3+2"]           ))
questions.add(Question.MCQ("Nitrite"       ,  "NO2-1"       ,  ["NO2+1", "NO2-2", "NO2+2"]           ))
questions.add(Question.MCQ("Sulfate"       ,  "SO4-2"       ,  ["SO4+1", "SO4-1", "SO4+2"]           ))
questions.add(Question.MCQ("Sulfite"       ,  "SO3-2"       ,  ["SO3+1", "SO3-1", "SO3+2"]           ))
questions.add(Question.MCQ("Phosphate"     ,  "PO4-3"       ,  ["PO4+1", "PO4-1", "PO4+2"]           ))
questions.add(Question.MCQ("Phosphite"     ,  "PO3-3"       ,  ["PO3+1", "PO3-1", "PO3+2"]           ))
questions.add(Question.MCQ("Carbonate"     ,  "CO3-2"       ,  ["CO3+1", "CO3-1", "CO3+2"]           ))
questions.add(Question.MCQ("BiCarbonate"   ,  "HCO3-1"      ,  ["HCO3+1", "HCO3-2", "HCO3+2"]        ))
questions.add(Question.MCQ("Cyanide"       ,  "CN-1"        ,  ["CN+1", "CN-2", "CN+2"]              ))
questions.add(Question.MCQ("Permanganate"  ,  "MnO4-1"      ,  ["MnO4+1", "MnO4-2", "MnO4+2"]        ))
questions.add(Question.MCQ("Acetate"       ,  "C2H3O2-1"    ,  ["C2H3O2+1", "C2H3O2-2", "C2H3O2+2"]  ))
questions.add(Question.MCQ("Peroxide"      ,  "O2-2"        ,  ["O2+1", "O2-1", "O2+2"]              ))

questions.add(Question.FRQ("NH4+1"     , "ammonium"         , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("H3O+1"     , "hydronium"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("OH-1"      , "hydroxide"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("NO3-1"     , "nitrate"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("NO2-1"     , "nitrite"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("SO4-2"     , "sulfate"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("SO3-2"     , "sulfite"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("PO4-3"     , "phosphate"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("PO3-3"     , "phosphite"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("CO3-2"     , "carbonate"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("HCO3-1"    , "bicarbonate"      , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("CN-1"      , "cyanide"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("MnO4-1"    , "permanganate"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("C2H3O2-1"  , "acetate"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("O2-2"      , "peroxide"         , filtered_equals(nest(stripped, lowercased))))

questions.add(Question.FRQ("HClO4"   ,  "perchloric acid"      , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("HCl"     ,  "hydrochloric acid"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("HBr"     ,  "hydrobromic acid"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("HI"      ,  "hydroiodic acid"      , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("HNO3"    ,  "nitric acid"          , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("H2SO4"   ,  "sulfuric acid"        , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("LiOH"    ,  "lithium hydroxide"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("NaOH"    ,  "sodium hydroxide"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("KOH"     ,  "potassium hydroxide"  , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("Ca(OH)2" ,  "calcium hydroxide"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("Sr(OH)2" ,  "strontium hydroxide"  , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("Ba(OH)2" ,  "barium hydroxide"     , filtered_equals(nest(stripped, lowercased))))

questions.add(Question.FRQ("perchloric acid"       , "HClO4"   , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("hydrochloric acid"     , "HCl"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("hydrobromic acid"      , "HBr"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("hydroiodic acid"       , "HI"      , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("nitric acid"           , "HNO3"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("sulfuric acid"         , "H2SO4"   , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("lithium hydroxide"     , "LiOH"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("sodium hydroxide"      , "NaOH"    , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("potassium hydroxide"   , "KOH"     , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("calcium hydroxide"     , "Ca(OH)2" , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("strontium hydroxide"   , "Sr(OH)2" , filtered_equals(nest(stripped, lowercased))))
questions.add(Question.FRQ("barium hydroxide"      , "Ba(OH)2" , filtered_equals(nest(stripped, lowercased))))

questions.add(Question.FRQ("Diatomic Acronym?"     , "HOFBrINCl" , filtered_equals(nest(stripped))))

questions.add(Question.FRQ("Mercury" , "Hg" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Silver"  , "Ag" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Lead"    , "Pb" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Tin"     , "Sn" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Copper"  , "Cu" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Iron"    , "Fe" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("Gold"    , "Au" , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))


questions.run()