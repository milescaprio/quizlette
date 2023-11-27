## Edit this file to edit your quizlet.
## Make your own with the same format!

from lib import *
fn = "bone"

questions = Game([], fn)
questions.worst_hole = -1

questions.add(Question.FRQ("on the left of your right arm"               , "radius"               , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("on the right of you right arm"               , "ulna"                 , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("funny bone"                                  , "humorous"             , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("big front bottom leg"                        , "tibia"                , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("small back bottom leg"                       , "fibula"               , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("top thigh"                                   , "femur"                , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("collarbone"                                  , "clavicle"             , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("shoulderblade"                               , "scapula"              , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("in between ribs"                             , "sternum"              , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("big dingus"                                  , "pelvic"               , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("kneecap"                                     , "patella"              , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("l1 fingers"                                  , "carpals"              , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("l2 fingers"                                  , "metacarpals"          , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("l1 toes"                                     , "tarsals"              , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("l2 toes"                                     , "metatarsals"          , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))
questions.add(Question.FRQ("l3 fingers"                                  , "phalanges"            , filtered_equals(nest(stripped, lowercased)), reinforcements_needed=2))

questions.run()