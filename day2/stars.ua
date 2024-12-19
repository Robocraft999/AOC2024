# Experimental!
Input ← (
  &fras
  ⊜(□⊜(⋕)⊸≠@ )⊸≠@\n
)

RowSafe ← (
  ⟜⧻°□
  ↘1↻¯1-:⊸↻1
  .
  /××>0:⊸<4⌵
  ×
  ⌵/+±
  =+1
)

RowSafe₂ ← (
  °□
  ↯ ⊟ .:⟜⧻
  ⊞(≠) ⊃⇡⇡ :⟜⧻
  ≡(⊸▽)
  ⊙◌
  >0 /+≡RowSafe
)

Part₁ ← /+≡(RowSafe °□)

Part₂ ← /+≡RowSafe₂

Part₂ Input "testinput.txt"

⍤⟜≍ 2 Part₁ Input "testinput.txt"
⍤⟜≍ 379 Part₁ Input "input.txt"
⍤⟜≍ 4 Part₂ Input "testinput.txt"
⍤⟜≍ 430 Part₂ Input "input.txt"
