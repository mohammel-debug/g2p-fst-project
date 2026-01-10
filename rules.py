# Rules

## 1. Consonants

fsts['rule_pre'] = FST.re("$^rewrite('ˈ':'' | 'ˌ':'')") #accent removing 

fsts['rule_v_end'] = FST.re("$^rewrite(v:f / _ #)")  # THIS MUAT BE BEFORE THE RULE, OTHERWISE IT WONT WORK
fsts['rule_v'] = FST.re("$^rewrite(v:b)")  #verb, berb
fsts['rule_w'] = FST.re("$^rewrite(w:(gu))")  #win, guin
# $rule_ə @ fsts['rule_h_drop'] = FST.re("$^rewrite((h): )")  #helen, Elen?
#we cannot put 2 rules for one letter ;( - this comment seems to indicate a constraint or a known issue. With the next h rule I think it is enough, I would say that we say jelen rater than elen
fsts['rule_h'] = FST.re("$^rewrite(h:x)")  #heavy, jeby/hello,jelo
fsts['rule_ŋ'] = FST.re("$^rewrite(ŋ:n)")  #sing, sin
# @ $rule_r fsts['rule_r'] = FST.re("$^rewrite(ɹ:r)")  # in cases like part, we don't say pa:t but paRt. I don't know if this is the way to put it though
fsts['rule_j'] = FST.re("$^rewrite(j:ʝ)")  #you, ju / yes,jes / yellow,jelow
fsts['rule_z'] = FST.re("$^rewrite(z:s)")  #lazy, leisi
fsts['rule_ʒ'] = FST.re("$^rewrite(ʒ:ʃ)")  #leasure, lisher
#Spanish does not have voiced stops/fricatives at the end of syllables
fsts['rule_b_end'] = FST.re("$^rewrite(b:p / _ #)")  # club, clup
fsts['rule_g_end'] = FST.re("$^rewrite(ɡ:k / _ #)")  # bag, bak not working...now yes- the problem was this: g instead of ɡ.

# Rule for 's' at the beginning of a word, followed by a consonant
fsts['C'] = FST.re("b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z")
fsts['rule_s'] = FST.re("$^rewrite(s:(es) / # _ $C)", fsts)  #school

# full, ful / final, final(dark l does not exist in the end of words in spanish. 
#It's pronounced as normal l)
# @ $rule_ɫ fsts['rule_ɫ'] = FST.re("$^rewrite(ɫ:l)")

fsts['rule_ð'] = FST.re("$^rewrite(ð:d)")  #that, dat / father, fader
fsts['rule_θ'] = FST.re("$^rewrite(θ:t)")  # thought, tot

consonants_grammar = FST.re("$rule_pre @ $rule_v_end $rule_v @ $rule_w @ "
                            "$rule_h @ $rule_ŋ @ $rule_j @ $rule_z @ "
                            "$rule_ʒ @ $rule_b_end @ $rule_g_end @ $rule_s @ $rule_ð @ $rule_θ", fsts)

consonants_fst = lexicon_for_composition @ consonants_grammar

consonants_test = ['that', 'thought', 'give', 'verb', 'win', 'hello',
                  'sing', 'you', 'lazy', 'pleasure', 'club', 'bag',
                   'school']

for word in consonants_test:
    original_ipa = list(original_lexicon.generate(word))
    transformed_ipa = list(consonants_fst.generate(word))
    print(f"Word: {word}")
    print(f"Original IPA: {original_ipa}")
    print(f"Transformed: {transformed_ipa}")
    print("\n")

'''some are still not working'''

## 2. Diphthongs

'''fsts['rule_əʊ'] = FST.re("$^rewrite(əʊ:ou)")  # go, go
fsts['rule_eɪ'] = FST.re("$^rewrite(eɪ:ei)")  # day, de
fsts['rule_oʊ'] = FST.re("$^rewrite(oʊ:ou)")  # home, houm
fsts['rule_aɪ'] = FST.re("$^rewrite(aɪ:ai)") # time, taim
fsts['rule_aʊ'] = FST.re("$^rewrite(aʊ:au)")  # about, abaut
fsts['rule_ɔɪ'] = FST.re("$^rewrite(ɔɪ:oi)") # noise, nois
fsts['rule_ʊə'] = FST.re("$^rewrite(ʊə:u)") # hour
fsts['rule_eə'] = FST.re("$^rewrite(eə:ea)") # hair, jear'''
#Diphthongs rules are not working at all.

#We might need to seperate the vowels then join them together. 
'''fsts['rule_əʊ'] = FST.re("$^rewrite(ə:o)") @ FST.re("$^rewrite(ʊ:u)")#go
fsts['rule_eɪ'] = FST.re("$^rewrite(e:e)") @ FST.re("$^rewrite(ɪ:i)") #day
fsts['rule_oʊ'] = FST.re("$^rewrite(o:o)") @ FST.re("$^rewrite(ʊ:u)") #home
fsts['rule_aɪ'] = FST.re("$^rewrite(a:a)") @ FST.re("$^rewrite(ɪ:i)") #time
fsts['rule_aʊ'] = FST.re("$^rewrite(a:a)") @ FST.re("$^rewrite(ʊ:u)") #about
fsts['rule_ɔɪ'] = FST.re("$^rewrite(ɔ:o)") @ FST.re("$^rewrite(ɪ:i)") #noise
fsts['rule_ʊə'] = FST.re("$^rewrite(ʊ:u)") @ FST.re("$^rewrite(ə:o)")#  hour
fsts['rule_eə'] = FST.re("$^rewrite(e:e)") @ FST.re("$^rewrite(ə:a)") #hair
'''
#these rules will change all vowels. We have to add contex to them

fsts['rule_əʊ'] = FST.re("$^rewrite(ə:o / _ ʊ) @ $^rewrite(ʊ:u / o _)")
fsts['rule_eɪ'] = FST.re("$^rewrite(e:e / _ ɪ) @ $^rewrite(ɪ:i / e _)")
fsts['rule_oʊ'] = FST.re("$^rewrite(o:o / _ ʊ) @ $^rewrite(ʊ:u / o_)") 
fsts['rule_aɪ'] = FST.re("$^rewrite(a:a / _ ɪ) @ $^rewrite(ɪ:i / a _)")
fsts['rule_aʊ'] = FST.re("$^rewrite(a:a / _ ʊ) @ $^rewrite(ʊ:u / a _)")
fsts['rule_ɔɪ'] = FST.re("$^rewrite(ɔ:o / _ ɪ) @ $^rewrite(ɪ:i / o _)")
fsts['rule_ʊə'] = FST.re("$^rewrite(ʊ:u / _ ə) @ $^rewrite(ə:o / u _)")
fsts['rule_eə'] = FST.re("$^rewrite(e:e / _ ə) @ $^rewrite(ə:a / e _)")


diphthongs_grammar = FST.re("$rule_əʊ @ $rule_eɪ @ $rule_oʊ @ $rule_aɪ @ "
                            "$rule_aʊ @ $rule_ɔɪ @ $rule_ʊə @ $rule_eə", fsts)

diphthongs_fst = lexicon_for_composition @ diphthongs_grammar 

diphthongs_test = ['go', 'day', 'home', 'time', 'about', 'noise', 'hour', 'there']

for word in diphthongs_test:
    original_ipa = list(original_lexicon.generate(word))
    transformed_ipa = list(diphthongs_fst.generate(word))
    print(f"Word: {word}")
    print(f"Original IPA: {original_ipa}")
    print(f"Transformed: {transformed_ipa}")
    print("\n")

## Haxta aquí, todo bien. But once we run the following section, vowels, we losew everything bacause there is a conflict between vowels and diphthongs ;( 

## 3. Vowels


#vowels
# $rule_iː @ fsts['rule_iː'] = FST.re("$^rewrite((iː):i)")  # see, si
fsts['rule_ɪ'] = FST.re("$^rewrite(ɪ:i/ ! [a|e|ɔ] _)")  # shIt, shit
fsts['rule_æ'] = FST.re("$^rewrite(æ:a)")  # cat, cat
fsts['rule_ʌ'] = FST.re("$^rewrite(ʌ:a)")  # cup, cop I believe this is more /a/ than /o/
#  $rule_ɜː @ fsts['rule_ɜː'] = FST.re("$^rewrite((ɜː):(er))")  # bird, berd not working
#fsts['rule_ɐ'] = FST.re("$^rewrite(ɐ:a)") # about, abaout
#fsts['rule_ə'] = FST.re("$^rewrite(ə:a / ! _ ʊ))")  #
# $rule_ə1 @ fsts['rule_ə1'] = FST.re("$^rewrite(ə:o / _ n #)")
fsts['rule_ɒ'] = FST.re("$`rewrite(ɒ:o)") #hot or dog
fsts['rule_ʊ'] = FST.re("$^rewrite(ʊ:u / ! [ə|a|o] _)") # full not fʊl but ful
fsts['rule_uː'] = FST.re("$^rewrite((uː):u)")  # you, ju
fsts['rule_ɔ'] = FST.re("$^rewrite(ɔ:o)") #
fsts['rule_ɔː'] = FST.re("$^rewrite((ɔː):o)")  # thought, tot
#  @ $rule_ɑː fsts['rule_ɑː'] = FST.re("$^rewrite((ɑː):a)")  # car, car / bark, bark ...this is problematic as well. The rs are pronounced in English_Spanish


vowels_grammar = FST.re("$rule_ɪ @ $rule_æ @ $rule_ʌ @ $rule_ɒ @"
                        "$rule_ʊ @ $rule_uː @ $rule_ɔ @ $rule_ɔː", fsts)
'''

vowels_fst = lexicon_for_composition @ vowels_grammar

vowels_test = ['shit', 'cat', 'cup', 'hot', 'full', 'you', 'thought']

for word in vowels_test:
    original_ipa = list(original_lexicon.generate(word))
    transformed_ipa = list(vowels_fst.generate(word))
    print(f"Word: {word}")
    print(f"Original IPA: {original_ipa}")
    print(f"Transformed: {transformed_ipa}")
    print("\n")
