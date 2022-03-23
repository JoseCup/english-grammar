from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
from parsimonious.grammar import Grammar
grammar = Grammar(
    """
    sentence       = (nounphrase ws verbphrase) / nounphrase
    nounphrase     = pronoun / cmplxnoun / (cmplxnoun ws prepphrase) / noun
    verbphrase     = cmplxverb / (cmplxverb ws prepphrase)
    prepphrase     = (prep ws cmplxnoun)
    cmplxnoun      = (article ws noun) / (article ws noun ws conjunction nounphrase) 
    cmplxverb      = (verb ws noun ws conjunctions) / (verb ws noun) / (verb ws (adj / article) ws noun) / verb / (verb ws nounphrase) 
    article        = "The" / "a" / "an" / "This" / "A" / "That"
    adj            = "smart" / "funny" / "smelly" / "different"/ "used"/ "important"/ "every"/ "large"/ "available"/ "popular"/ "able"/ "basic"/ "known"/ "various"/ "difficult"/ "several"/ "united"/ "historical"/ "hot"/ "useful"/ "mental"/ "scared"/ "additional"/ "emotional"/ "old"/ "political"/ "similar"/ "healthy"/ "financial"/ "medical"/ "traditional"/ "federal"/ "entire"/ "strong"/ "actual"/ "significant"/ "successful"/ "electrical"/ "expensive"/ "pregnant"/ "intelligent"/ "interesting"/ "poor"/ "happy"/ "responsible"/ "cute"/ "helpful"/ "recent"/ "willing"/ "nice"/ "wonderful"/ "impossible"/ "serious"/ "huge"/ "rare"/ "technical"/ "typical"/ "competitive"/ "critical"/ "electronic"/ "immediate"/ "aware"/ "educational"/ "environmental"/ "global"/ "legal"/ "relevant"/ "accurate"/ "capable"/ "dangerous"/ "dramatic"/ "efficient"/ "powerful"/ "foreign"/ "hungry"/ "practical"/ "psychological"/ "severe"/ "suitable"/ "numerous"/ "sufficient"/ "unusual"/ "consistent"/ "cultural"/ "existing"/ "famous"/ "pure"/ "afraid"/ "obvious"/ "careful"/ "latter"/ "unhappy"/ "acceptable"/ "aggressive"/ "boring"/ "distinct"/ "eastern"/ "logical"/ "reasonable"/ "strict"/ "administrative"/ "automatic"/ "civil"/ "former"/ "massive"/ "southern"/ "unfair"/ "visible"/ "alive"/ "angry"/ "desperate"/ "exciting"/ "friendly"/ "lucky"/ "realistic"/ "sorry"/ "ugly"/ "unlikely"/ "anxious"/ "comprehensive"/ "curious"/ "impressive"/ "informal"/ "inner"/ "pleasant"/ "sexual"/ "sudden"/ "terrible"/ "unable"/ "weak"/ "wooden"/ "asleep"/ "confident"/ "conscious"/ "decent"/ "embarrassed"/ "guilty"/ "lonely"/ "mad"/ "nervous"/ "odd"/ "remarkable"/ "substantial"/ "suspicious"/ "tall"/ "tiny"
    noun           = "boy" / "girl" / "flower"  / "computers" / "computer" / "science" / "pythons" / "python" /"act"/ "answer"/ "approve"/ "arrange"/ "break"/ "build"/ "coach"/ "color"/ "cough"/ "create"/ "complete"/ "cry"/ "dance"/ "describe"/ "draw"/ "drink"/ "eat"/ "edit"/ "enter"/ "exit"/ "imitate"/ "invent"/ "jump"/ "laugh"/ "lie"/ "listen"/ "paint"/ "plan"/ "play"/ "read"/ "replace"/ "run"/ "scream"/ "see"/ "shop"/ "shout"/ "sing"/ "skip"/ "sleep"/ "sneeze"/ "solve"/ "study"/ "teach"/ "touch"/ "turn"/ "walk"/ "win"/ "write"/ "whistle"/ "yank"/ "zip"
    pronoun        = "I" / "you" / "he" / "It" / "she" / "we"
    verb           = "loves" /  "likes" / "touches" / "likes" / "sees" / "love" / "act"/ "answer"/ "approve"/ "arrange"/ "break"/ "build"/ "coach"/ "color"/ "cough"/ "create"/ "complete"/ "cry"/ "dance"/ "describe"/ "draw"/ "drink"/ "eat"/ "edit"/ "enter"/ "exit"/ "imitate"/ "invent"/ "jump"/ "laugh"/ "lie"/ "listen"/ "paint"/ "plan"/ "play"/ "read"/ "replace"/ "run"/ "scream"/ "see"/ "shop"/ "shout"/ "sing"/ "skip"/ "sleep"/ "sneeze"/ "solve"/ "study"/ "teach"/ "touch"/ "turn"/ "walk"/ "win"/ "write"/ "whistle"/ "yank"/ "zip"
    conjunctions   = conjunction ws sentence
    conjunction   = "for" / "and" / "nor" / "but" / "or" / "yet" / "so"
    prep           = "with" / "in"
    ws             = ~"\s*"
    """)

print(grammar.parse("This boy loves python and computers"))
print("--------------------------------------------------------------------------------------------")
print(grammar.parse("That boy loves python but This girl loves science"))
print("--------------------------------------------------------------------------------------------")
print(grammar.parse("I love python"))
print("--------------------------------------------------------------------------------------------")
print(grammar.parse("I love python and computers"))
print("--------------------------------------------------------------------------------------------")



